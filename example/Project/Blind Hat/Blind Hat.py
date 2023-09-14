from machine import *
from time import sleep
from hcsr04 import HCSR04
from ssd1306 import SSD1306_I2C
from neopixel import NeoPixel
import _thread

ultrasonic = HCSR04(trigger_pin=18,echo_pin=19)
oled = SSD1306_I2C(128,64,SoftI2C(scl=Pin(22),sda=Pin(21)))
np = NeoPixel(Pin(23,Pin.OUT),2) 

buzzer = PWM(Pin(32))
buzzer_beeping = False

def beep_buzzer():
    global buzzer_beeping
    while True:
        if buzzer_beeping:
            buzzer.freq(1000)
            buzzer.duty(512)
            sleep(0.1)
            buzzer.duty(0)
            sleep(0.1)
        else:
            buzzer.duty(0)

_thread.start_new_thread(beep_buzzer, ())

while True:
    distance = ultrasonic.distance_cm()
    print(distance)
    if distance > 0 and distance <300:
        np[0],np[1] = (0,255,0),(0,255,0)
        if distance < 60:
            np[0],np[1] = (255,255,0),(255,255,0)
        if distance < 30:
            np[0],np[1] = (255,0,0),(255,0,0)
            buzzer_beeping = True
        else:
            buzzer_beeping = False
        np.write()
    else:
        np[0],np[1] = (0,0,0),(0,0,0)
        
    distance_text = '{:.2f}'.format(distance)
    oled.text('Distance(cm)',25,0,1)
    oled.text(distance_text, 43, 30, 1)
    oled.show()
    oled.text('Distance(cm)',25,0,0)
    oled.text(distance_text, 43, 30, 0)
    sleep(0.1)


