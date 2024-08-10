# ---Import Library---
from machine import Pin,ADC
from time import sleep

# ---Pin Setup---
ldr_Pin = ADC(Pin(36))

# ---Main Program---
while True:
    # Read LDR Analog Value 
    ldr_val_12 = ldr_Pin.read()     # range min 0 - max 4095 
    ldr_val_16 = ldr_Pin.read_u16() # range min 0 - max 65535 
    
    print('raw analog 12bit value:{}',ldr_val_12)
    print('raw analog 12bit value:{}',ldr_val_16)
    sleep(0.1)                      # delay 0.1 sec



