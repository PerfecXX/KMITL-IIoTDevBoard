# ---Import Library---
from neopixel import NeoPixel
from machine import Pin
from time import sleep

# ---Pin Setup---
np_Pin = NeoPixel(Pin(23,Pin.OUT),2)
btn1_Pin = Pin(15,Pin.IN,Pin.PULL_UP)
btn2_Pin = Pin(2,Pin.IN,Pin.PULL_UP)

# ---Main Program---
while True:
    
    # Read NeoPixel State
    r1,g1,b1 = np_Pin[0]
    r2,g2,b2 = np_Pin[1]
    
    # Read Button State 
    btn1_state = btn1_Pin.value() # button 1
    btn2_state = btn2_Pin.value() # button 2
    
    # Button 1 Toggle Red NeoPixel 1
    if btn1_state == 0:
        r1,g1,b1 = not r1,not g1,not b1
        np_Pin[0] = (r1*10,g1*0,b1*0)
        np_Pin.write()
        
    # Button 2 Toggle Green NeoPixel 2    
    if btn2_state == 0:
        r2,g2,b2 = not r2,not g2,not b2
        np_Pin[1] = (r2*0,g2*10,b2*0)
        np_Pin.write()
        
    # Delay 0.1 Second
    sleep(0.1)
