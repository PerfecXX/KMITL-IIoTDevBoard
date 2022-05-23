# ---Import Library---
from neopixel import NeoPixel
from machine import Pin

# ---Pin Setup---
np_Pin = NeoPixel(Pin(23,Pin.OUT),2) # 2 is number of NeoPixel

# --- Main Program ---
np_Pin[0] = (10,0,0) # set RGB 1 to 10% red 
np_Pin[1] = (0,0,10) # set RGB 2 to 10% blue
np_Pin.write()       # write the setting rgb value to NeoPixel
