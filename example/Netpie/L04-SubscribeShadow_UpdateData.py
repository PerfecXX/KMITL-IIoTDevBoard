# ---Import Library---
from network import WLAN,STA_IF
from simple import MQTTClient
from json import dumps
from machine import Pin
from dht import DHT11

# ---Pin Setup---
dht = DHT11(Pin(13))

# Network Credential
ssid = ''     # change
password = '' # change

# Network Interface 
wlan = WLAN(STA_IF)
wlan.active(True)

# ---Start Network Connection---
print('Connecting...')
wlan.connect(ssid,password)
while not wlan.isconnected():
    pass

# Connection Config
print('Connected!')
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

# MQTT Callback Function
# This function must be called with client.set_callback() only 
def on_message(topic,msg):
    # decode the incoming data type
    # from byte to normal text
    topic,msg = topic.decode('utf8'),msg.decode('utf8')
    print('message from ',topic ,msg)
    
# Set MQTT Profile
client = MQTTClient(client_ID,broker,
                    user=token,
                    password=secret)

# Sets the function for receiving data from the broker.
client.set_callback(on_message)

# ---Start MQTT Connection---
print('Broker Connecting...')
client.connect()
print('Broker Connected!')

# ---Subscribe topic---
# Use @shadow/data/updated to get the updated Shadow data
topic = '@shadow/data/updated'
client.subscribe(topic)

# --- Main Program---
while True:
    # Checks any messsage are sent from broker or not 
    # if it true, the function that setting with .set_callback() will be called
    client.check_msg()
    
    # Read sensor value
    dht.measure()
    temp = dht.temperature()
    hum = dht.humidity()
    
    # Publish to Shadow
    client.publish('@shadow/data/update',dumps({
        'data':{
            'Temperature':temp,
            'Humidity' : hum,
            }}))
