# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
import json
import datetime
from django.http import HttpResponse, request, HttpRequest
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from myapp.models import Account, User, Session, Dweet, Like, Comment, Follower

import requests

ES_ENDPOINT = "http://127.0.0.1:9200/dweet_search/_search"


def hello(request):
    text = "hello ! Everyone, this is my 1st project."
    return HttpResponse(text)


def signup_submit(request):
    errors = {}
    if request.method == 'POST':
        print request.body
        body = json.loads(request.body)
        errors = validate_signup(body)
        if errors and errors['error']:
            print "========= Errors ==============="
            print errors
            return getResonse(errors, 424)
        else:
            signup_data = update_signup(body)
            if (has_value(signup_data, "error")):
                errors['error'] = "error"
                errors['account'] = signup_data['error']
                return getResonse(errors, 424)
            elif not (has_value(signup_data, "email")):
                print "======= API ERROR (NO EMAIL FOUND) ============"
                errors['error'] = 'error'
                errors['account'] = "Internal Error - API error"
                return getResonse(errors, 424)
            else:
                account_id = str(uuid.uuid4())
                ac = Account(account_id=account_id, account_email=signup_data["email"],
                             login_password=signup_data["password"], account_status="active")
                first_name = signup_data["first_name"]
                last_name = signup_data["last_name"]
                created_time = str(datetime.datetime.now())
                user = User(user_id=account_id, user_first_name=first_name, user_last_name=last_name,
                            user_profile_name=signup_data['profile_name'], created_time=created_time,
                            modified_time=created_time)
                try:
                    ac.save()
                    user.save()
                    return getResonse({"status": "success"}, 201)
                except Exception as e:
                    print e
                    return getResonse({}, 500)



    else:
        errors['error'] = 'error'
        errors['account'] = "Methosd not allowed"
        return getResonse(errors, 405)


def login_submit(request):
    errors = {}
    if request.method == 'POST':
        body = json.loads(request.body)
        errors = validate_login(body)
        if (errors and errors['error']):
            print "=========== VALIDATION ERRORS ============="
            print errors
            return errors
        else:
            hash = pbkdf2_sha256.using(rounds=8000, salt=b"10").hash(body['password'])
            print "hash : ", hash
            account = Account.objects.filter(account_email=body['email'], login_password=hash).values()
            print "========== GET response ================ "
            print account
            if (account and len(account) > 0):
                response_json = init_session(account[0])
                if 'error' in response_json:
                    errors['error'] = response_json['error']
                    return getResonse(errors, 500)
                print "======== SESSION INITIALIZED ============"
                print response_json
                return getResonse(response_json, 201)
            else:
                print "===== Username/Password is incorrect =========="
                errors['password'] = 'Username/Password is incorrect'
                return getResonse(errors, 403)

    else:
        errors['error'] = 'Internal Error'
        return getResonse(errors, 500)


def dweet(request):
    errors = {}
    valid, data = validate_session(request)
    print "data : ", data
    if not valid:
        return getResonse(data, 424)
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            dweet_id = 'd_' + str(uuid.uuid4())
            created_time = str(datetime.datetime.now())
            dweet_data = body['dweet_data']
            account_id = data
            dweet = Dweet(dweet_id=dweet_id, created_time=created_time, dweet_data=dweet_data
                          , account_id=account_id)
            dweet.save()
            return getResonse({"status": "success"}, 201)
        except KeyError as ke:
            print ke
            return getResonse({"status": "failed", "data_missing": ke.message}, 422)
        except Exception as e:
            print e
            return getResonse({"status": "failed"}, 500)
    else:
        return getResonse({"status": "failed"}, 405)


def like(request):
    errors = {}
    valid, data = validate_session(request)
    if not valid:
        return data
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            account_id = data
            entity_id = body['entity_id']
            like = Like(account_id=account_id, entity_id=entity_id)
            like.save()
            return getResonse({"status": "success"}, 201)
        except KeyError as ke:
            print ke
            return getResonse({"status": "failed", "data_missing": ke.message}, 422)
        except Exception as e:
            print e
            return getResonse({"status": "failed"}, 500)
    else:
        return getResonse({"status": "failed"}, 405)


def comment(request):
    errors = {}
    valid, data = validate_session(request)
    if not valid:
        return data
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            comment_id = 'c_' + str(uuid.uuid4())
            dweet_id = body['dweet_id']
            comment_data = body['comment']
            created_time = str(datetime.datetime.now())
            account_id = data
            comment = Comment(comment_id=comment_id, dweet_id=dweet_id, comment_data=comment_data,
                              created_time=created_time, account_id=account_id)
            comment.save()
            return getResonse({"status": "success"}, 201)
        except KeyError as ke:
            print ke
            return getResonse({"status": "failed", "data_missing": ke.message}, 422)
        except Exception as e:
            print e
            return getResonse({"status": "failed"}, 500)
    else:
        return getResonse({"status": "failed"}, 405)


def isValidUser(user_id):
    users = User.objects.filter(user_id=user_id).values('user_id')
    if users and len(users) > 0:
        return True
    else:
        return False


def follow(request):
    errors = {}
    valid, data = validate_session(request)
    if not valid:
        return getResonse({"status": "invalid"}, 422)
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            user_id = data
            followed_user_id = body['followed_user_id']

            if user_id != followed_user_id and isValidUser(user_id) and isValidUser(followed_user_id):
                follower = Follower(user_id=user_id, followed_user_id=followed_user_id)
                follower.save()
                return getResonse({"status": "success"}, 201)
            else:
                raise Exception("Invalid userInfos !! ")
        except KeyError as ke:
            print ke
            return getResonse({"status": "failed", "data_missing": ke.message}, 422)
        except Exception as e:
            print e
            return getResonse({"status": "failed"}, 500)
    else:
        return getResonse({"status": "failed"}, 405)


def feed(request):
    errors = {}
    valid, data = validate_session(request)
    print "Valid"
    if not valid:
        return getResonse({"status": "failed"}, 422)
    if request.method == 'GET':
        try:
            user_id = data
            dweetsCursor = Dweet.objects.filter(
                account_id=Follower.objects.filter(user_id=user_id).values('followed_user_id')).values()
            dweets = []
            for i in range(0, len(dweetsCursor)):
                dweet = dweetsCursor[i]
                dweet['created_time'] = str(dweet['created_time'])
                dweets.append(dweet)

            print dweets

            return getResonse({"status": "success", "data": dweets}, 200)
        except KeyError as ke:
            print ke
            return getResonse({"status": "failed", "data_missing": ke.message}, 422)
        except Exception as e:
            print e
            return getResonse({"status": "failed"}, 500)

    else:
        return getResonse({"status": "failed"}, 405)


def searchDweet(request):
    errors = {}
    valid, data = validate_session(request)
    print "Valid"
    if not valid:
        return getResonse({"status": "failed"}, 422)
    if request.method == 'GET':
        try:
            keywords = request.GET.get('q')
            print keywords
            sort_query = {
                "sort": [
                    {
                        "created_time": {"order": "desc"}
                    }
                ],
                "query" : {
                    "bool":{
                        "must" : [
                            {"match" : {"content" : keywords} },
                            {"match" : {"django_ct": "myapp.dweet"} }
                        ]
                    }
                }
            }

            query =ES_ENDPOINT
            sort_query=json.dumps(sort_query)
            response = requests.get(query,data=sort_query)
            result = response.content
            result = json.loads(result)
            results = result['hits']['hits']
            final_res = []
            for r in results:
                entry = r['_source']
                dweet = {}
                dweet['dweet'] = entry['content']
                dweet['created_time'] = entry['created_time']
                dweet['dweet_id'] = entry['dweet_id']
                final_res.append(dweet)

            return getResonse({"status": "success", "data": final_res}, 200)
        except KeyError as ke:
            print ke
            return getResonse({"status": "failed", "data_missing": ke.message}, 422)
        except Exception as e:
            print e
            return getResonse({"status": "failed"}, 500)

    else:
        return getResonse({"status": "failed"}, 405)


def searchDweeter(request):
    errors = {}
    valid, data = validate_session(request)
    print "Valid"
    if not valid:
        return getResonse({"status": "failed"}, 422)
    if request.method == 'GET':
        try:
            keywords = request.GET.get('q')
            print keywords
            sort_query = {
                "sort": [
                    {
                        "modified_time": {"order": "desc"}
                    }
                ],
                "query": {
                    "bool": {
                        "should": [
                            {"match": {"user_first_name": keywords}},
                            {"match": {"user_last_name": keywords}}
                        ],
                        "minimum_should_match": 1,
                        "must" : [
                            {"match": {"django_ct": "myapp.user"}}
                        ]
                    }
                }
            }

            query = ES_ENDPOINT
            sort_query = json.dumps(sort_query)
            response = requests.get(query, data=sort_query)
            result = response.content
            result = json.loads(result)
            results = result['hits']['hits']
            final_res = []
            for r in results:
                entry = r['_source']
                print entry
                dweet = {}
                dweet['user_last_name'] = entry['user_last_name']
                dweet['user_first_name'] = entry['user_first_name']
                dweet['user_profile_name'] = entry['user_profile_name']
                dweet['modified_time'] = entry['modified_time']
                final_res.append(dweet)

            return getResonse({"status": "success", "data": final_res}, 200)
        except KeyError as ke:
            print ke
            return getResonse({"status": "failed", "data_missing": ke.message}, 422)
        except Exception as e:
            print e
            return getResonse({"status": "failed"}, 500)

    else:
        return getResonse({"status": "failed"}, 405)


def has_value(obj, field):
    result = False
    if obj and get_value(obj, field):
        result = True

    return result


def get_value(obj, field):
    value = ""
    try:
        value = obj.get(field)
    except Exception as e:
        print e
        pass

    return value


def getResonse(content, status):
    return HttpResponse(json.dumps(content), content_type="application/json", status=status)


def update_signup(form):
    print form
    hash = pbkdf2_sha256.using(rounds=8000, salt=b"10").hash(form['password'])
    form['password'] = hash

    print "=============== SIGNUP POST REQUEST ========================="
    return form
    # return post_to_apigateway(url, data)


def validate_signup(form):
    error = {}

    if 'profile_name' not in form:
        error['error'] = "error"
        error['profile_name'] = "Please specify your profile_name"

    if 'email' not in form:
        error['error'] = "error"
        error['email'] = "Please specify an email id"

    if 'password' not in form:
        error['error'] = "error"
        error['password'] = "Please specify a password"

    return error


def validate_login(form):
    error = {}
    if not form['email']:
        error['error'] = "error"
        error['email'] = "Please specify an email id"
    if not form['password']:
        error['error'] = "error"
        error['password'] = "Please specify a password"

    return error


def init_session(account):
    print "========== INIT SESSION ==========="
    print account
    response = {}

    session = {}
    session['session_id'] = uuid.uuid4()
    session['created_time'] = str(datetime.datetime.now())
    session['account_id'] = account['account_id']
    session['last_used_time'] = session['created_time']

    print session
    sess = Session(session_id=session['session_id'],
                   created_time=session['created_time'],
                   account_id=session['account_id'],
                   last_used_time=session['last_used_time']
                   )

    try:
        sess.save()
        response['session_id'] = str(session['session_id'])
        response['account_id'] = session['account_id']
    except Exception as e:
        response['error'] = e.message
        print e
    return response


def validate_account_verification(form):
    error = {}
    if not form['password']:
        error['error'] = "error"
        error['password'] = "Please specify a password"
    if not form['cpassword']:
        error['error'] = "error"
        error['cpassword'] = "Please confirm your password"

    if form['password'] != form['cpassword']:
        error['error'] = "error"
        error['match'] = "Passwords do not match!"

    print error
    return error


def validate_session(request):
    errors = {}
    try:
        session_id = request.META['HTTP_SESSION_ID']
        account_id = request.META['HTTP_ACCOUNT_ID']
        sess = Session.objects.filter(session_id=session_id, account_id=account_id).values()
        td = datetime.timedelta(minutes=30)

        if not sess or len(sess) == 0 or datetime.datetime.now() - (
                sess[0]['last_used_time'].replace(tzinfo=None)) > td:
            errors['error'] = "Invalid Session"
            return (False, errors)
        sess[0]['last_used_time'] = str(datetime.datetime.now())
        sessObj = Session.objects.filter(session_id=session_id).update(last_used_time=sess[0]['last_used_time'])
        return (True, account_id)
    except Exception as e:
        print e
        errors['error'] = e.message
        return (False, errors)
