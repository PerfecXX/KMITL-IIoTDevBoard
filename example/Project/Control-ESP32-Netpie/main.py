# ---Import Library---
from network import WLAN,STA_IF
from simple import MQTTClient
from json import dumps
from machine import Pin,ADC,PWM,SoftI2C,reset
from dht import DHT11
from ssd1306 import SSD1306_I2C
from neopixel import NeoPixel
from time import sleep

# OLED Function
def oled_show(text,x_pos,y_pos):
    oled.text(text,x_pos,y_pos)
    oled.show()

def oled_clear():
    oled.fill(0)
    oled.show()
    

# MQTT Callback Function
def on_message(topic,msg):
    topic,msg = topic.decode('utf8'),msg.decode('utf8')
    print('message from ',topic ,msg)
    if msg == 'buzzer-on':
        beep = PWM(buzzer,freq,duty)
        sleep(0.5)
        beep.deinit()
    elif msg == 'led1-on':
        np[0] = (0,0,1)
        np.write()
    elif msg == 'led1-off':
        np[0] = (0,0,0)
        np.write()
    elif msg == 'relay1-on':
        relay1.value(1)
    elif msg == 'relay1-off':
        relay1.value(0)
    elif msg == 'relay2-on':
        relay2.value(1)
    elif msg == 'relay2-off':
        relay2.value(0)

# ---Pin Setup---
np = NeoPixel(Pin(23,Pin.OUT),2)
btn1 = Pin(15,Pin.IN,Pin.PULL_UP)
btn2 = Pin(2,Pin.IN,Pin.PULL_UP)
btn3 = Pin(0,Pin.IN,Pin.PULL_UP)
btn4 = Pin(4,Pin.IN,Pin.PULL_UP)
pot = ADC(Pin(39))
ldr = ADC(Pin(36))
dht = DHT11(Pin(13))
oled = SSD1306_I2C(128,64,SoftI2C(scl=Pin(22),sda=Pin(21)))
buzzer = Pin(32,Pin.OUT)
relay1 = Pin(14,Pin.OUT)
relay2 = Pin(27,Pin.OUT)

# Buzzer Variable
freq = 3000
duty = 1000

# Network Credential
ssid = ''     # change
password = '' # change

try:
    # Network Interface 
    wlan = WLAN(STA_IF)
    wlan.active(True)

    # ---Start Network Connection---
    print('Connecting...')
    oled_show('WiFi Connecting',0,0)
    wlan.connect(ssid,password)
    while not wlan.isconnected():
        pass

    # Connection Config
    print('Connected!')
    oled_show('WiFi Connected',0,10)
    print('IP:',wlan.ifconfig()[0],
          '\nSubnet Mask:',wlan.ifconfig()[1],
          '\nDefault Gateway:',wlan.ifconfig()[2],
          '\nDNS:',wlan.ifconfig()[3])

    # Netpie MQTT Credential
    # (Get all credential from Netpie)
    client_ID = ''               # <== change
    token = ''                   # <== change
    secret = ''                  # <== change
    broker = 'mqtt.netpie.io'
    shadow = '@shadow/data/update'
    msg = '@msg/data'
       
        
    # Set MQTT Profile
    client = MQTTClient(client_ID,broker,
                        user=token,
                        password=secret)

    # Sets the function for receiving data from the broker.
    client.set_callback(on_message)

    # ---Start MQTT Connection---
    print('MQTT Connecting...')
    oled_show('MQTT Connecting...',0,20)

    client.connect()
    oled_show('MQTT Connected',0,30)
    print('MQTT Connected!')

        
    # Subscribe to topic
    client.subscribe(msg)
    oled_clear()
    oled_show('Working...',0,30)
    # ---Main Program---
    while True:
        # Check message from Netpie
        client.check_msg()
        # ---Read Sensor/Module---
        # NeoPixel
        r1,g1,b1 = np[0]
        r2,g2,b2 = np[1] 
        
        # DHT11
        dht.measure()
        temperature = dht.temperature()
        humidity = dht.humidity()
        # LDR
        ldr_val = ldr.read()
        # Button
        btn1_state = btn1.value()
        btn2_state = btn2.value()
        btn3_state = btn3.value()
        btn4_state = btn4.value()
        # Potentiometer
        pot_val = pot.read()
        # Relay
        relay1_state = relay1.value()
        relay2_state = relay2.value()
        
        # ---Show values of sensor---
        print('Temperature:{} °C Humidity:{} %RH'.format(temperature,humidity))
        print('btn1:{} btn2:{} btn3:{} btn4:{}'.format(btn1_state,btn2_state,btn3_state,btn4_state))
        print('LDR:{} POT:{}'.format(ldr_val,pot_val))
        print('Relay1:{} Relay2:{}'.format(relay1_state,relay2_state))
        
        # ESP32 On-Board Control
        if btn1_state == 0:
            np[0] = (r1,not g1,b1)
            np.write()
        if btn3_state ==0:
            relay1.value(not relay1_state)
        if btn4_state ==0:
            relay2.value(not relay2_state)
        
        if ldr_val > 2000:
            np[1] = (1,1,1)
            np.write()
        else:
            np[1] = (0,0,0)
            np.write()
        
        #---Publish Data to Netpie---
        client.publish(shadow,dumps({
            'data':{
                'Temperature':temperature,
                'Humidity': humidity,
                'LDR':ldr_val,
                'Potentiometer':pot_val,
                'Button':{
                    'Button1':btn1_state,
                    'Button2':btn2_state,
                    'Button3':btn3_state,
                    'Button4':btn4_state,
                    },
                'Relay':{
                    'Relay1':relay1_state,
                    'Relay2':relay2_state,
                    },
                'NeoPixel':{
                    'NeoPixel1':{
                        'Red':r1,
                        'Green':g1,
                        'Blue':b1
                        },
                    'NeoPixel2':{
                        'Red':r2,
                        'Green':g2,
                        'Blue':b2
                        }
                    }
                }
            }))
        
        # Delay
        sleep(0.5)
except OSError as errorCode:
    print('Error Code: ',errorCode)
    oled_clear()
    oled_show('Error {}'.format(errorCode),0,10)
    oled_show('Restarting...'.format(errorCode),0,20)
    sleep(5)
    reset()
