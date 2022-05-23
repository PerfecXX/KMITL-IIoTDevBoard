# ---Import Library---
from neopixel import NeoPixel
from machine import Pin
from time import sleep

# ---Pin Setup---
np_Pin = NeoPixel(Pin(23,Pin.OUT),2)
btn1_Pin = Pin(15,Pin.IN,Pin.PULL_UP)
btn2_Pin = Pin(2,Pin.IN,Pin.PULL_UP)
btn3_Pin = Pin(0,Pin.IN,Pin.PULL_UP)
btn4_Pin = Pin(4,Pin.IN,Pin.PULL_UP)

# ---Main Program---
while True:
    # Read Button State 
    btn1_state = btn1_Pin.value() # button 1
    btn2_state = btn2_Pin.value() # button 2
    btn3_state = btn3_Pin.value() # button 3
    btn4_state = btn4_Pin.value() # button 4
    
    # Button Pressed Event 
    # if button pressed the button state value will change from 1 to 0 (Active Low)
    if btn1_state == 0:       # check when button 1 is pressed
        print('Button 1 pressed!') 
        np_Pin[0] = (0,10,0)  # set rgb1 to green 10%
        np_Pin.write()        # write the setting rgb value to NeoPixel

    if btn2_state == 0:       # check when button 2 is pressed
        print('Button 2 pressed!') 
        np_Pin[0] = (0,0,0)   # set rgb1 to 0% rgb 
        np_Pin.write()        # write the setting rgb value to NeoPixel

    if btn3_state == 0:       # check when button 3 is pressed
        print('Button 3 pressed!')
        np_Pin[1] = (20,10,0) # set rgb1 to red 20% and green 10% 
        np_Pin.write()        # write the setting rgb value to NeoPixel

    if btn4_state == 0:       # check when button 4 is pressed
        print('Button 4 pressed!')
        np_Pin[1] = (0,0,0)   # set rgb1 to 0% rgb
        np_Pin.write()        # write the setting rgb value to NeoPixel

    sleep(0.1) # Delay 0.1 Sec
    

