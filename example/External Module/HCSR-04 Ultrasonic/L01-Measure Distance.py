# ---Import Library---
from machine import Pin
from hcsr04 import HCSR04
from time import sleep

# ---Pin Setup---
ultrasonic = HCSR04(trigger_pin=18,echo_pin=19)

# ---Main Program---
while True:
    # Read the distance from the ultrasonic sensor
    distance = ultrasonic.distance_cm()
        
    print("Distance: ",distance," cm.")
    sleep(1)
