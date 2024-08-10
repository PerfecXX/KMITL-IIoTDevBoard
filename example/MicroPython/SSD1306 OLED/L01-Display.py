# Import Library
from ssd1306 import SSD1306_I2C
from machine import Pin,SoftI2C

# Pin Setup
oled_Pin = SoftI2C(scl=Pin(22),sda=Pin(21))

# Screen Resolution 
oled_ScreenWidth = 128
oled_ScreenHeight = 64

# OLED Interface 
oled = SSD1306_I2C(oled_ScreenWidth,oled_ScreenHeight,oled_Pin)

# Set text and position
x_postion = 0
y_postion = 0
text = 'Hello World!'
oled.text(text,x_postion,y_postion)
# Display text to OLED 
oled.show()

