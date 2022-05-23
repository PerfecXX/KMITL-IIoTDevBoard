# ---Import Library---
from machine import Pin,ADC
from time import sleep

# ---Pin Setup---
pot_Pin = ADC(Pin(39))

# To read voltages above the reference voltage,
# apply input attenuation with the atten keyword
pot_Pin.atten(ADC.ATTN_11DB)  # Set Attenuation to 11dB (150mV-2450mV)

# ---Main Program---
while True:
    # Read Potentiometer analog value
    pot_val = pot_Pin.read()
    print(pot_val)
    sleep(0.1)
    
