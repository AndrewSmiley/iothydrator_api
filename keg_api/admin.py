__author__ = 'pridemai'
from django.contrib import admin
from models import *
admin.site.register(User)
admin.site.register(Pour)
admin.site.register(Status)
admin.site.register(Part)