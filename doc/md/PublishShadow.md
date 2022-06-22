### Publish Data to Netpie with MQTT 
---
Netpie has 2 topics to publish the data from your device.
1. Shadow API Topic
2. Message API Topic

### Shadow API Topic 
---
Netpie Shadow is where the published data is stored in JSON format and can be used in many Netpie features. For example,
- Schema (Data Validation & Data Transformation)
- Trigger (Event Hook)
- Feed (Timeseries Data)
- Free Board (Data Visualization) 

![](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/netpie-shadow-empty.png?raw=true)

Before you publishing your data to Shadow, make sure your ESP32 are able and ready to connect with Netpie.
If you are not sure, please see [Connect Your Device to Netpie with MicroPython](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/netpie-upy-connection.md "Connect Your Device to Netpie with MicroPython").

To publish the data to Netpie Shadow, you need to publish to the `@shadow/data/update` topic and the format of the publishing data is JSON format.

The structure of the payload for Netpie Shadow is 
```python
{'data': {
		'field name 1': Value 1,
		'field name 2': Value 2,
		'field name 3': Value 3,...,
		'field name n': Value n
	}}
```

Follow this instruction to publish the data from ESP32 to Shadow.

1. Create a new .py file and copy the following code: (Download the full code [here](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/example/Netpie/L02-PublishShadow.py "here")).
2. Replace the SSID and password with your wifi SSID and wifi password.
3. Replace the client_ID, token, and secret with your client_ID, token, and secret.

```python
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

# Set MQTT Profile
client = MQTTClient(client_ID,broker,
                    user=token,
                    password=secret)

# ---Start MQTT Connection---
print('Broker Connecting...')
client.connect()
print('Broker Connected!')

# --- Main Program---
while True:
    # Reading Sensor
    dht.measure()
    # Set temperature/humidity
    temp = dht.temperature()
    hum = dht.humidity()
    # Publish to Netpie Shadow 
    client.publish('@shadow/data/update',dumps({
        'data':{
            'Temperature':temp,
            'Humidity' : hum,
            }}))
```
4.Run your code.

5.Return to Netpie and look at Device Shadow. It will show the published data (if it is not shown, try to refresh the web page).

![Published data](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/netpie-shadow-data.png?raw=true "Published data")

That is, now you can store the published data in the Netpie Shadow.

