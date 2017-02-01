#
# #include "LiquidCrystal.h"
# # LiquidCrystal lcd(7, 8, 9, 10, 11, 12);
#
# # which pin to use for reading the sensor? can use any pin!
# #define FLOWSENSORPIN 2
#
# # count how many pulses!
# pulses = 0
# # track the state of the pulse pin
# lastflowpinstate
# # you can try to keep time of how long it is between pulses
# lastflowratetimer = 0
# # and use that to calculate a flow rate
# flowrate = 0
# # Interrupt is called once a millisecond, looks for any pulses from the sensor!
# SIGNAL(TIMER0_COMPA_vect) {
# uint8_t x = digitalRead(FLOWSENSORPIN);
#
#   if (x == lastflowpinstate) {
#     lastflowratetimer++;
#     return; # nothing changed!
#   }
#
#   if (x == HIGH) {
#     #low to high transition!
#     pulses++;
#   }
#   lastflowpinstate = x;
#   flowrate = 1000.0;
#   flowrate /= lastflowratetimer;  # in hertz
#   lastflowratetimer = 0;
# }
#
# void useInterrupt(boolean v) {
#   if (v) {
#     # Timer0 is already used for millis() - we'll just interrupt somewhere
#     # in the middle and call the "Compare A" function above
#     OCR0A = 0xAF;
#     TIMSK0 |= _BV(OCIE0A);
#   } else {
#     # do not call the interrupt function COMPA anymore
#     TIMSK0 &= ~_BV(OCIE0A);
#   }
# }
#
# void setup() {
#    Serial.begin(9600);
#    Serial.print("Flow sensor test!");
#    lcd.begin(16, 2);
#
#    pinMode(FLOWSENSORPIN, INPUT);
#    digitalWrite(FLOWSENSORPIN, HIGH);
#    lastflowpinstate = digitalRead(FLOWSENSORPIN);
#    useInterrupt(true);
# }
#
# void loop()                     # run over and over again
# {
#   lcd.setCursor(0, 0);
#   lcd.print("Pulses:"); lcd.print(pulses, DEC);
#   lcd.print(" Hz:");
#   lcd.print(flowrate);
#   #lcd.print(flowrate);
#   Serial.print("Freq: "); Serial.println(flowrate);
#   Serial.print("Pulses: "); Serial.println(pulses, DEC);
#
#   # if a plastic sensor use the following calculation
#   # Sensor Frequency (Hz) = 7.5 * Q (Liters/min)
#   # Liters = Q * time elapsed (seconds) / 60 (seconds/minute)
#   # Liters = (Frequency (Pulses/second) / 7.5) * time elapsed (seconds) / 60
#   # Liters = Pulses / (7.5 * 60)
#   float liters = pulses;
#   liters /= 7.5;
#   liters /= 60.0;
#
# """
#   # if a brass sensor use the following calculation
#   float liters = pulses;
#   liters /= 8.1;
#   liters -= 6;
#   liters /= 60.0;
# """
#   Serial.print(liters); Serial.println(" Liters");
#   lcd.setCursor(0, 1);
#   lcd.print(liters); lcd.print(" Liters        ");
#
#   delay(100);
# set up the flow meter
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
pouring = False
lastPinState = False
pinState = 0
lastPinChange = int(time.time() * 1000)
pourStart = 0
pinChange = lastPinChange
pinDelta = 0
hertz = 0
flow = 0
litersPoured = 0
pintsPoured = 0
# main loop
while True:
    currentTime = int(time.time() * 1000)
    if GPIO.input(4):
        pinState = True
    else:
        pinState = False
    # If we have changed pin states low to high...
    if (pinState != lastPinState and pinState == True):
        if (pouring == False):
            pourStart = currentTime
        pouring = True
        # get the current time
        pinChange = currentTime
        pinDelta = pinChange - lastPinChange
        if (pinDelta < 1000):
            # calculate the instantaneous speed
            hertz = 1000.0000 / pinDelta
            flow = hertz / (60 * 7.5)  # L/s
            litersPoured += flow * (pinDelta / 1000.0000)
            pintsPoured = litersPoured * 2.11338
        if (pouring == True and pinState == lastPinState and (currentTime - lastPinChange) > 3000):
            # set pouring back to false, tweet the current amt poured, and reset everything
            pouring = False
            if (pintsPoured > 0.1):
                pourTime = int((currentTime - pourStart) / 1000) - 3
                litersPoured = 0
                pintsPoured = 0
