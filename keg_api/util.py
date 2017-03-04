__author__ = 'andrewsmiley'
from models import *
try:
    from grovepi import *
    import RPi.GPIO as GPIO
except:
    print "Running in local environment: Using Stubs"
    from grovepi import *
    import GPIO

import math
# from multiprocessing import Process
import threading
clicks = 0
ml_per_oz=0.0338140225589

_flowmeter_gpio_pin=23
# 18=18

def click_incrementer(channel):
    global clicks
    # print "click %s" %(clicks)
    clicks = clicks + 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)
GPIO.add_event_detect(23, GPIO.FALLING, callback=click_incrementer)
GPIO.setmode(GPIO.BCM)

dht_sensor_port = 7
dht_sensor_type = 1


def ounces_to_ml(oz):
    return float(oz)* 29.5735296
def ml_to_ounces(ml):
    return float(ml)* ml_per_oz


def run_pour(pour_id, volume):
    pour=Pour.objects.get(id=pour_id)
    global clicks

    try:
        GPIO.output(18, GPIO.LOW)
        while clicks < round(ounces_to_ml(int(volume)-1)/2.25):
            # print "ounces poured %s" %(ml_to_ounces(clicks*2.25))
            pour.actual_volume = ml_to_ounces(clicks*2.25)
            pour.save()
        pour.status = Status.objects.get(description="complete")
        pour.save()
        clicks=0 #reset clicks to 0
    except:
        import traceback
        traceback.print_exc()
        clicks=0
        pour.status = Status.objects.get(description="Error")
        pour.actual_volume = ml_to_ounces(clicks*2.25)
        pour.save()
        pass
    GPIO.output(18, GPIO.HIGH)

def start_pi_pour(volume):
    pour = Pour()
    pour.volume = volume
    pour.actual_volume = 0.0
    pour.user = User.objects.last()
    pour.date= str((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)
    pour.status = Status.objects.get(description="In Progress")
    pour.keg = Keg.objects.last()
    pour.save()
    #fuck tuples
    t = threading.Thread(target=run_pour, args=(pour.id,volume))
    t.start()
    return pour.id
    # p = Process(target=run_pour, args=(pour.id,))
    # p.start()
def stop_pi_pour():
    try:
        GPIO.output(18, GPIO.HIGH)
        pour = Pour.objects.last()
        pour.status = Status.objects.get(description="Stopped")
        pour.save()
        return True
    except:
        return False

def get_pour_percentage(pour_id):
    pour = Pour.objects.get(id=int(pour_id))
    res = (float(int(math.ceil(pour.actual_volume)))/float(pour.volume)*100.0)
    if res >= 98:
        GPIO.output(18, GPIO.HIGH)
        pour.status = Status.objects.get(description="complete")
        pour.save()
    return res

def get_thermo_status():
    [temp, hum] = dht(dht_sensor_port, dht_sensor_type)
    return temp is not None


def get_keg_temperature():
    [temp, hum] = dht(dht_sensor_port, dht_sensor_type)
    return float(temp * 9 / 5 + 32)

def get_flowmeter_status():
    return True
def get_pressure_sensor_status():
    return {"ps0":True, "ps1":True, "ps2":True}
def get_keg_percentage():
    total_volume = 0.0
    for p in Pour.objects.filter(keg=Keg.objects.last()):
        total_volume = total_volume+float(p.actual_volume)



    return (float(total_volume)/float(Keg.objects.last().volume))*100

def get_c02_percentage():
    return 80 #just going to stub this in

def get_days_to_keg_empty():
    return 3

def get_days_in_tank():
    return 6

def get_days_in_lines():

    return 45

def get_optimal_maintenance_range():
    return ['6PM', "7AM"]


