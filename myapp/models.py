# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Account(models.Model):
    account_id = models.CharField(max_length=50, primary_key=True)
    account_email = models.CharField(max_length=50, unique=True)
    account_status = models.CharField(max_length=50)
    login_password = models.CharField(max_length=1024)

    class Meta:
        db_table = 'account'


class User(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    user_first_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    user_profile_name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'user'


class Dweet(models.Model):
    account_id = models.CharField(max_length=50)
    dweet_data = models.TextField()
    dweet_id = models.CharField(max_length=50, primary_key=True)
    created_time = models.DateTimeField()

    class Meta:
        db_table = 'dweet'


class Like(models.Model):
    account_id = models.CharField(max_length=50)
    entity_id = models.CharField(max_length=50)  # Entity can be any dweet and comment

    class Meta:
        db_table = 'like'
        unique_together = ("account_id", "entity_id")


class Comment(models.Model):
    account_id = models.CharField(max_length=50)
    dweet_id = models.CharField(max_length=50)
    comment_id = models.CharField(max_length=50, primary_key=True)
    comment_data = models.TextField()
    created_time = models.DateTimeField()

    class Meta:
        db_table = 'comment'


class Follower(models.Model):
    user_id = models.CharField(max_length=50)
    followed_user_id = models.CharField(max_length=50)

    class Meta:
        db_table = 'follower'
        unique_together = ("user_id", "followed_user_id")

class Session(models.Model):
    session_id = models.CharField(max_length=254, primary_key=True)
    created_time = models.DateTimeField()
    account_id = models.CharField(max_length=50)
    last_used_time = models.DateTimeField()

    class Meta:
        db_table = 'session'
