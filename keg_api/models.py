__author__ = 'pridemai'

from django.db import models
import datetime
class User(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    sso = models.CharField(max_length=10)

class Status(models.Model):
    description = models.CharField(max_length=200)
    code = models.IntegerField(default=0)

class Pour(models.Model):
    date = models.CharField(max_length=50, default=str((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000))
    volume = models.IntegerField()
    user = models.ForeignKey(User)
    status = models.ForeignKey(Status)

