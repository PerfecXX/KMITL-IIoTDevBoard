# ---Import Library---
from machine import Pin
from time import sleep

# ---Pin Setup---
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
    print('btn1:{} btn2:{} btn3:{} btn4 {}'.format(btn1_state,btn2_state,btn3_state,btn4_state))
    sleep(0.1) # Delay 0.1 Sec
    
