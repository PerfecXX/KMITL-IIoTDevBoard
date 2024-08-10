# ---Import Library--- 
from dcmotor import DCMotor
from machine import Pin,PWM
from time import sleep

# Function for movement
def forward():
    left_wheel.forward(60)
    right_wheel.forward(60)

def backward():
    left_wheel.backwards(60)
    right_wheel.backwards(60)

def stop():
    left_wheel.stop()
    right_wheel.stop()

# ---Pin Setup---
motor_pin1 = Pin(33, Pin.OUT) 
motor_pin2 = Pin(32, Pin.OUT)
motor_pin3 = Pin(26,Pin.OUT)
motor_pin4 = Pin(25,Pin.OUT)
enable_pin = PWM(Pin(13),15000)

# Wheel Setup
left_wheel = DCMotor(motor_pin1,motor_pin2,enable_pin)
right_wheel = DCMotor(motor_pin3,motor_pin4,enable_pin)

while True:
    print('Forward!')
    forward()
    sleep(1)
    print('Stop!')
    stop()
    sleep(1)
    print('Backward!')
    backward()
    sleep(1)
    print('Stop')
    stop()
    sleep(1)

