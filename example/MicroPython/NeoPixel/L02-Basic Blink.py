# ---Import Library---
from neopixel import NeoPixel
from machine import Pin 
from time import sleep
# ---Pin Setup---
np_Pin = NeoPixel(Pin(23,Pin.OUT),2)

# --- Main Program ---
while True:                 
    np_Pin[0] = (10,0,0)  # set rgb1 to 10% red
    np_Pin[1] = (0,0,10)  # set rgb2 to 10% blue
    np_Pin.write()        # write the setting rgb value to NeoPixel 
    sleep(1)              # delay 1 sec 
    np_Pin[0] = (0,0,0)   # set rgb1 to 0% rgb (off)
    np_Pin[1] = (0,0,0)   # set rgb2 to 0% rgb (off)
    np_Pin.write()        # write the setting rgb value to NeoPixel
    sleep(1)              # delay 1 sec
    





