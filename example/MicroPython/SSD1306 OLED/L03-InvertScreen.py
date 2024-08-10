# Import Library
from ssd1306 import SSD1306_I2C
from machine import Pin,SoftI2C
from time import sleep

# Pin Setup 
oled_Pin = SoftI2C(scl=Pin(22),sda=Pin(21))

# Screen Resolution 
oled_ScreenWidth = 128
oled_ScreenHeight = 64

# OLED Interface 
oled = SSD1306_I2C(oled_ScreenWidth,oled_ScreenHeight,oled_Pin)

# Set text and position
x1_postion = 0
y1_postion = 0
x2_postion = 20
y2_postion = 20
first_text = 'Normal'
second_text = 'Inverted'

# Set and display the first text to OLED
oled.text(first_text,x1_postion,y1_postion)
oled.show()
sleep(1)

# Clear entire screen then invert the screen color
oled.fill(0)   
oled.invert(1) # odd number is invert 
oled.show()

# Set and display the first text to OLED
oled.text(second_text,x2_postion,y2_postion)
oled.show()




