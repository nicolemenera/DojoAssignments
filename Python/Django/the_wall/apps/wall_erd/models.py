from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class User(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()
  password = models.CharField(max_length=30)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
  messages = models.TextField()
  user = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
  comment = models.TextField()
  user = models.ForeignKey(User)
  message = models.ForeignKey(Message)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
