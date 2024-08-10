from neopixel import NeoPixel
from machine import Pin

np_Pin = NeoPixel(Pin(23,Pin.OUT),2) # 2 is number of NeoPixel

while True:
    text = input("Enter something:")
    if text == "on":
        np_Pin[0] = (10,0,0) 
        np_Pin[1] = (0,0,10) 
        np_Pin.write()
    elif text == "off":
        np_Pin[0] = (0,0,0) 
        np_Pin[1] = (0,0,0) 
        np_Pin.write()
