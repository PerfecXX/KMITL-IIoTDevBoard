# ---Import Library---
from neopixel import NeoPixel
from machine import Pin

# ---Pin Setup---
np_Pin = NeoPixel(Pin(23,Pin.OUT),2) # 2 is Number of NeoPixel

# --- Main Program ---
np_Pin[0] = (10,0,0) # Set RGB 1 to 10% red 
np_Pin[1] = (0,0,10) # Set RGB 2 to 10% blue
np_Pin.write()       # Light up the Neo Pixel 
