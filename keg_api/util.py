__author__ = 'andrewsmiley'
from models import *
from grovepi import *
import RPi.GPIO as GPIO
# from multiprocessing import Process
import threading
clicks = 0
ml_per_oz=0.0338140225589
_flowmeter_gpio_pin=23
# 18=18

def click_incrementer(channel):
    global clicks
    clicks = clicks + 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)
GPIO.add_event_detect(23, GPIO.FALLING, callback=click_incrementer)
GPIO.setmode(GPIO.BCM)

dht_sensor_port = 7
dht_sensor_type = 1


def ounces_to_ml(oz):
    return oz/ ml_per_oz
def ml_to_ounces(ml):
    return ml * ml_per_oz
def run_pour(pour_id):
    pour=Pour.objects.get(id=pour_id)
    try:
        GPIO.output(18, GPIO.LOW)
        while clicks*2.25 < ounces_to_ml(volume):
            pour.actual_volume = ml_to_ounces(clicks*2.25)
            pour.save()
        pour.status = Status.objects.get(description="Complete")
        pour.save()
        clicks=0 #reset clicks to 0
    except:
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
    t = threading.Thread(target=run_pour, args=(pour.id,))
    t.start()
    # p = Process(target=run_pour, args=(pour.id,))
    # p.start()

    return pour.id
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
    return float(float(pour.actual_volume)/float(pour.volume)*100.0)

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


