## The Dweeter
Dweeter is an RESTFul web app that is similar to twitter with following functionalities:-
- View all the dweets from followed folks 
- Add new dweets 
- Like someone's dweet 
- Comment on the dweet 
- Search dweeters 
- Follow new dweeters 
- Search dweets 
- Create new account (Auth) 


## API Documentation
### SignUp API:   `/signup` 
```
curl -X POST 
-d '{"email":<email>,"password":<password>,"first_name":<firstname>,"last_name":<lastname>,"profile_name":<profilename>}' 
'http://localhost:8000/myapp/signup'
```

### Login API:   `/login` 
If email-password combination is correct, 
This api returns the `account-id` corresponding to the below emailId and a new `session-id`, with a 30 mins validity,
renewable after every use.  
```
curl -X POST
-d '{
"email":<emailid>,
"password":<password>
}'
'http://localhost:8000/myapp/signup'
```

### Dweet API: `/dweet`
```curl -X POST 
-H 'session-id:<session-id>'
-H 'account-id:<account-id>'
-d '{
"dweet_data":<dweet data>
}'
'http://127.0.0.1:8000/myapp/dweet'
```

### Comment API: `/comment`
```curl -X POST 
-H 'session-id:<session-id>'
-H 'account-id:<account-id>'
-d '{
"dweet_id":<dweet-id>,
"comment":<comment>
}'
'http://127.0.0.1:8000/myapp/comment'
```


### Like API: `/like`
```
curl -X POST
-H 'session-id:<session-id>'
-H 'account-id:<account-id>'
-d '{
"entity_id":<anyTweetId or CommentId>
}'
'http://127.0.0.1:8000/myapp/like'
```

### Follow API: `/follow`
```
curl -X POST
-H 'session-id:<session-id>'
-H 'account-id:<account-id>'
-d '{
"followed_user_id":<userIdToBeFollowed>
}'
'http://127.0.0.1:8000/myapp/follow
```

## Get Dweets from followed Dweeters in your Feed `/feed`
```
curl -X GET
-H 'session-id:<session-id>'
-H 'account-id:<account-id>'
'http://127.0.0.1:8000/myapp/feed
```

### Search Dweets API: `/searchDweet`
```
curl -X GET
-H 'session-id:<session-id>'
-H 'account-id:<account-id>'
'http://127.0.0.1:8000/myapp/searchDweet?q=<keywords>
```

### Search Users API: `/searchUsers`
```
curl -X GET
-H 'session-id:<session-id>'
-H 'account-id:<account-id>'
'http://127.0.0.1:8000/myapp/searchUsers?q=<name>
```

  

