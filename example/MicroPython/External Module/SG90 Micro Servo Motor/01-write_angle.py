from machine import Pin
from servo import Servo

servo = Servo(Pin(23))
servo.write_angle(0)
