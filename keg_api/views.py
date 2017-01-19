__author__ = 'pridemai'
from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from models import Pour, User
from util import *
# import Image
import json

def index(request):
    return render(request, 'index.html', {'test': "my data"})

def start_pour(request, volume=1, user_id=1):
    return HttpResponse(json.dumps({"result":True}))

def stop_pour(request):
    return HttpResponse(json.dumps({"result":True}))

def pour_status(request, pour_id=1):
    return HttpResponse(json.dumps({"result":True, "percentage":5, "status":"Completed", "volume_expected":32, "volume_poured":"30"}))

def authenticate(request, sso=''):
    if User.objects.filter(sso=sso).count() != 0:

        return HttpResponse(json.dumps({"result":True, "id":User.objects.get(sso=sso).id}))
    else:
        new_user = User()
        new_user.sso = sso
        #todo fetch the user information
        new_user.first_name = 'andrew'
        new_user.last_name = 'smiley'
        new_user.save()
        return HttpResponse(json.dumps({"result":True, "id":new_user.id}))

def system_info(request):
    health ={}
    health['sensors'] = {"flowmeter":get_flowmeter_status(), "pressure_sensor": get_pressure_sensor_status(), "thermo":get_thermo_status()}
    health["keg"]= {'temperature': get_keg_temperature(), 'percentage': get_keg_percentage()}
    health['c02']={'percentage': get_c02_percentage()}

    return HttpResponse(json.dumps({"result":True,"health":health}))

def pour_history(request):
    pours=[]
    for i in range(1, 3):
        pours.append({"pour_id":i, "status":"Completed", "user_id":i, "timestamp":"123456783", "volume": 32})
    return HttpResponse(json.dumps({"result":True, "pours":pours}))

def user_info(request, user_id=1):
    return HttpResponse(json.dumps({"result": True, "sso": "212543871", "first_name":"Andrew", "last_name":"Smiley"}))

def user_photo(request, user_id=1):
    # https://f4.bcbits.com/img/0003428886_10.jpg
    image_data = open("rumham.jpg", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

    # file = cStringIO.StringIO(urllib.urlopen(URL).read())
    # img = Image.open(file)
    # return HttpResponse(image_data, mimetype="image/png")