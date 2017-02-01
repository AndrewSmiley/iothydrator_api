from grovepi import *
import RPi.GPIO as GPIO

clicks = 0

GPIO.setmode(GPIO.BCM)


def my_callback(channel):
    global clicks
    print 'click'
    clicks = clicks + 1


GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback)

button_pin = 4  # Port for Button

pinMode(button_pin, "INPUT")  # Assign mode for Button as input
GPIO.setup(18, GPIO.OUT)

while True:
    try:
        button_status = digitalRead(button_pin)  # Read the Button status
        if button_status:  # If the Button is in HIGH position, run the program
            GPIO.output(18, GPIO.LOW)
        else:  # If Button is in Off position, print "Off" on the screen
            GPIO.output(18, GPIO.HIGH)
            if clicks != 0:
                print "Amount Poured %s ml" % (clicks * 2.25)
                clicks = 0
    except KeyboardInterrupt:  # Stop the buzzer before stopping
        GPIO.output(18, GPIO.HIGH)
        break
    except (IOError, TypeError) as e:
        print("Error")

