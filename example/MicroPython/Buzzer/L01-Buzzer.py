# ---Import Library---
from machine import Pin,PWM
from time import sleep

# ---Pin Setup---
buzzer_Pin = Pin(32,Pin.OUT)
freq = 1500                      # If the frequency is high, there will be a squealing sound.
duty = 100                       # Volume level

# ---Main Program---
beep = PWM(buzzer_Pin,freq) # Play Buzzer with frequency
beep.duty(duty)             # Set the duty     
sleep(0.5)                        # Beep length
beep.deinit()                     # Stop Playing
