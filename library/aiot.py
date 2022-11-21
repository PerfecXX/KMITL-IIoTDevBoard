# Import Library
try :
    from machine import *
    from time import sleep
    from ssd1306 import SSD1306_I2C
    from simple import MQTTClient
    from network import WLAN,STA_IF
    from dht import DHT11
    from neopixel import NeoPixel
    
except ImportError:
    print("Error: Library Not Found")
    
class AIOT():
    """
    Create instance and setup all AIoT pin
    For more detail: https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard
    """
    def __init__(self):
        self.__buzzFreq = 500
        self.__buzzDuty = 0
        self.__temperature = 0
        self.__humidity = 0
        self.__oledScreenWidth = 128
        self.__oledScreenHeight = 64
        
        self.__oledPin = SoftI2C(scl=Pin(22),sda=Pin(21))
        self.__oled = SSD1306_I2C(self.__oledScreenWidth,
                                 self.__oledScreenHeight,
                                 self.__oledPin)
        self.__relay1Pin = Pin(14,Pin.OUT)
        self.__relay2Pin = Pin(27,Pin.OUT)
        self.__buzzerPin = Pin(32,Pin.OUT)
        self.__neopixelPin = NeoPixel(Pin(23,Pin.OUT),2)
        self.__dhtPin = DHT11(Pin(13))
        self.__btn1Pin = Pin(15,Pin.IN,Pin.PULL_UP)
        self.__btn2Pin = Pin(2,Pin.IN,Pin.PULL_UP)
        self.__btn3Pin = Pin(0,Pin.IN,Pin.PULL_UP)
        self.__btn4Pin = Pin(4,Pin.IN,Pin.PULL_UP)
        self.__potPin = ADC(Pin(39))
        self.__ldrPin = ADC(Pin(36))
        self.author()
        
    def rgb_setColor(self,index,color):
        """
        Set an RGB color to a specific position. 
        -------------------------------------------
        Parameter:
        index(int) -> 0 or 1 => Position of RGB LED
        color(tuple) -> (r,g,b) => color of RGB LED
        ---
        r(int) -> 0 to 255 => intensity of the red color
        g(int) -> 0 to 255 => intensity of the green color
        b(int) -> 0 to 255 => intensity of the blue color
        """
        self.__neopixelPin[index] = (color[0],color[1],color[2])
    def rgb_show(self):
        self.__neopixelPin.write()
    def rgb_off(self,index):
        if index == 0:
            self.__neopixelPin[0] = (0,0,0)
        elif index ==1:
            self._neopixelPin[1] = (0,0,0)
        elif index == 'all':
            self.__neopixelPin[0] = (0,0,0)
            self.__neopixelPin[1] = (0,0,0)
        self.rgb_show()
    
    def get_dht(self):
        self.__dhtPin.measure()
        self.temperature = self.__dhtPin.temperature()
        self.humidity = self.__dhtPin.humidity()
    def author(self):
        print('Welcome to KMITL AIoT Development Board Version 1')
        print('For more detail,please visit')
        print('https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard ')
        
        
board = AIOT()
board.rgb_setColor(0,(255,0,0))
board.rgb_setColor(1,(0,255,0))
board.rgb_show()
sleep(1)
board.rgb_off('all')
        

