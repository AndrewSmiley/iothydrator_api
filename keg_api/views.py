__author__ = 'pridemai'
from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from models import Pour, User, Status
from util import *
# import Image
import json
import datetime
def index(request):
    return render(request, 'index.html', {'test': "my data"})

def start_pour(request, volume=1, user_id=1):
    # pour = Pour()
    # pour.volume = volume
    # pour.user = User.objects.get(id=1)
    # pour.date= str((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)
    # pour.status = Status.objects.get(description="In Progress")
    # pour.save()
    return HttpResponse(json.dumps({"result":True, "pour_id":start_pi_pour(volume)}))


def stop_pour(request):
    return HttpResponse(json.dumps({"result":stop_pi_pour()}))

def pour_status(request, pour_id=1):
#    pour_id = Pour.objects.last().id
    p = Pour.objects.get(id=int(pour_id))
#     pour_id=p.id
    print "progress for pour #%s: %s "%(pour_id, get_pour_percentage(pour_id))
    return HttpResponse(json.dumps({"result":True, "percentage":get_pour_percentage(pour_id), "status":p.status.description, "volume_expected":p.volume, "volume_poured":p.actual_volume}))

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
    for p in Pour.objects.all():
        pours.append({"pour_id":p.id, "status":"Completed", "user_id":p.user.id, "timestamp":p.date, "volume": p.actual_volume,"user_full_name":"%s %s"%(p.user.first_name,p.user.last_name)})
    return HttpResponse(json.dumps({"result":True, "pours":pours}))

def user_info(request, user_id=1):
    user = User.objects.get(id=user_id)
    return HttpResponse(json.dumps({"result": True, "sso": user.sso, "first_name":user.first_name, "last_name":user.last_name}))

def user_photo(request, user_id=1):
    # https://f4.bcbits.com/img/0003428886_10.jpg
    image_data = open("rumham.jpg", "rb").read()
    return HttpResponse(image_data, content_type="image/png")
def dt_overview(request):
    return HttpResponse(json.dumps({"result":"true","days_in_keg":get_days_to_keg_empty(), "days_in_c02":get_days_in_tank(), "days_in_lines":get_days_in_lines()}))

def dt_optimal_maintenance_time(request):
    omt_range= get_optimal_maintenance_range()
    return HttpResponse(json.dumps({"result":"true", "omt_start":omt_range[0], "omt_end":omt_range[-1]}))
