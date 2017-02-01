from grovepi import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

button_pin = 4  # Port for Button

pinMode(button_pin, "INPUT")  # Assign mode for Button as input
GPIO.setup(18, GPIO.OUT)
while True:
    GPIO.output(18, GPIO.LOW)


