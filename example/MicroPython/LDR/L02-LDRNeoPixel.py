# ---Import Library---
from machine import Pin,ADC
from neopixel import NeoPixel
from time import sleep

# ---Pin Setup---
ldr_Pin = ADC(Pin(36))
np_Pin = NeoPixel(Pin(23,Pin.OUT),2) 

# ---Main Program---
while True:
    # Read LDR Analog Value 
    ldr_val = ldr_Pin.read()     # range min 0 - max 4095
    print('LDR Value:',ldr_val)
    
    # LDR Change Value Event
    if ldr_val > 2000:           # if too dark       
        np_Pin[0] = (10,10,10)   # set rgb to 10% (white 10%)
        np_Pin.write()           # write the setting rgb value to NeoPixel
    else:                        # if not dark
        np_Pin[0] = (0,0,0)      # set rgb to 0% 
        np_Pin.write()           # write the setting rgb value to NeoPixel
    sleep(0.1)                   # delay 0.1 sec




