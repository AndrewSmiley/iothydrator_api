import atexit
import time
import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
#GPIO.setup(23, GPIO.IN)
#GPIO.setmode(23,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
clicks = 0
GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.OUT)

def my_callback(channel):
    global clicks
    print 'click'
    clicks = clicks + 1


GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback)


def exit_handler():
    #    if clicks != 0:
    #        hertz = 1000.0000 / clicks
    #    else:
    #        hertz = 0
    #    flow_rate = hertz / (60 * 7.5)
    print "mother fuckin genius %s ml" % (clicks * 2.25)

#    print "something was poured and the volume was %s litres"%(flow_rate * (clicks / 1000.0000))
#    print 'My application is ending!'
atexit.register(exit_handler)
#GPIO.output(18, GPIO.HIGH)
#while clicks < 10:
#	continue	
#GPIO.output(18, GPIO.LOW)

# main loop
while True:
    time.sleep(0.5)
#    if GPIO.input(23):
#        print "2.25 ML poured"
#        clicks = clicks +1
#    else:
#        continue
#        print "not pouring"
#        clicks = clicks +1
