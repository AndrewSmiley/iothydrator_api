"""
/******************************************************************************
Force_Sensitive_Resistor_Example.ino
Example sketch for SparkFun's force sensitive resistors
  (https://www.sparkfun.com/products/9375)
Jim Lindblom @ SparkFun Electronics
April 28, 2016

Create a voltage divider circuit combining an FSR with a 3.3k resistor.
- The resistor should connect from A0 to GND.
- The FSR should connect from A0 to 3.3V
As the resistance of the FSR decreases (meaning an increase in pressure), the
voltage at A0 should increase.

Development environment specifics:
Arduino 1.6.7
******************************************************************************/
const int FSR_PIN = A0; // Pin connected to FSR/resistor divider

// Measure the voltage at 5V and resistance of your 3.3k resistor, and enter
// their value's below:
const float VCC = 4.98; // Measured voltage of Ardunio 5V line
const float R_DIV = 3230.0; // Measured resistance of 3.3k resistor

void setup()
{
  Serial.begin(9600);
  pinMode(FSR_PIN, INPUT);
}

void loop()
{
  int fsrADC = analogRead(FSR_PIN);
  // If the FSR has no pressure, the resistance will be
  // near infinite. So the voltage should be near 0.
  if (fsrADC != 0) // If the analog reading is non-zero
  {
    // Use ADC reading to calculate voltage:
    float fsrV = fsrADC * VCC / 1023.0;
    // Use voltage and static resistor value to
    // calculate FSR resistance:
    float fsrR = R_DIV * (VCC / fsrV - 1.0);
    Serial.println("Resistance: " + String(fsrR) + " ohms");
    // Guesstimate force based on slopes in figure 3 of
    // FSR datasheet:
    float force;
    float fsrG = 1.0 / fsrR; // Calculate conductance
    // Break parabolic curve down into two linear slopes:
    if (fsrR <= 600)
      force = (fsrG - 0.00075) / 0.00000032639;
    else
      force =  fsrG / 0.000000642857;
    Serial.println("Force: " + String(force) + " g");
    Serial.println();

    delay(500);
  }
  else
  {
    // No pressure detected
  }
}
"""
import time
from grovepi import *

SLOPE = -0.0071
VCC = 4.98;  # Measured voltage of Ardunio 5V line
R_DIV = 3230.0;  # Measured resistance of 3.3k resistor
pinMode(2, "INPUT")
while True:

    fsrADC = analogRead(2)
    print fsrADC
    if fsrADC != 0:
        fsrV = float(fsrADC * VCC / 1023.0)
        print ("Voltage: %s V Verified" % (fsrV))
        fsrR = (fsrV / 1.0) * 1000  # float(R_DIV * (VCC / fsrV - 1.0))
        print ("Resistance: %s ohms" % (fsrR))
        fsrG = float(1.0 / fsrR)

        if (fsrR <= 600):
            force = (fsrG - 0.00075) / 0.0000032639
            print("Force: %s g" % (force))
        else:
            force = fsrG / 0.0000032639 * 2  # force = fsrG / 0.000000642857#  (fsrR/SLOPE)+60#fsrG / SLOPE#0.00000642857;
            # force = force
            print("Force: %s g" % (force))
    else:
        print "no pressure detected"

    time.sleep(1)
