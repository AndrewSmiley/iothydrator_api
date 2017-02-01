from grovepi import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

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
    except KeyboardInterrupt:  # Stop the buzzer before stopping
        GPIO.output(18, GPIO.HIGH)
        break
    except (IOError, TypeError) as e:
        print("Error")
