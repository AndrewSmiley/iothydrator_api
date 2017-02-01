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
    predix_status =models.BooleanField(default=False)
    actual_volume=models.FloatField(default=0.0)

    def __str__(self):
        return str(self.id)

class Part(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_added  = models.CharField(max_length=50, default=str((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000))
    cost = models.FloatField(default=0.0)
    part_code = models.IntegerField(default=1)
