### Message API Topic
---
A Message API Topic is a topic designed for communicating to another device through the Netpie that subscribes to the same topic.

To publish the data from the first device to the second device through the Netpie, the device needs to be in the same device group. 

### Device Grouping
---

1. Click the device group menu on the left.
2. Click the "create" button at the top left. 
3. Enter the name of the group, then click Create (description and tag are optional).

![](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/netpie-group-create.png?raw=true)

4.Back to the device list, select your device you want to group, then click move at the top right.
5.Select the device group name. 

![](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/netpie-group-move.png?raw=true)

![](https://raw.githubusercontent.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/5292274f5628f522451e37177ceb4bbf754b6d74/doc/netpie-group-moved.png)

### Publish Data with Message API Topic
---
To publish data to the Message API Topic, you must publish to the topic that begins with @msg/ followed by your topic name and format of the publishing data is String.

For example, @msg/data, @msg/house/bedroom/light, @msg/farm/waterpump, etc.

Follow the instructions below to publish the data with the Message API Topic.

1. Create a new .py file and copy the following code: (Download the full code here).
2. Replace the SSID and password with your wifi SSID and wifi password.
3. Replace the client_ID, token, and secret with your client_ID, token, and secret.
4. Run your code.

```python
# ---Import Library---
from network import WLAN,STA_IF
from simple import MQTTClient
from machine import Pin
from time import sleep

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
    client.publish('@msg/data','Hello, This is a message from ESP32')
    sleep(1)
```
### Subscribe to the Message API Topic.
---
You need to subscribe to the same topic as the publisher to get the published data.

Follow the instructions below to get the published data with the Message API Topic.

1. Create a new .py file and copy the following code: (Download the full code here).
2. Replace the SSID and password with your wifi SSID and wifi password.
3. Replace the client_ID, token, and secret with your client_ID, token, and secret (another device).
4. Run your code.

```python
# ---Import Library---
from network import WLAN,STA_IF
from simple import MQTTClient

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
# Use @private to get all of the data from Device Shadow
# This topic will activate only when you publish data to '@shadow/data/get' 
topic = '@msg/data'
client.subscribe(topic)

# --- Main Program---
while True:
    # Checks any messsage are sent from broker or not 
    # if it true, the function that setting with .set_callback() will be called
    client.check_msg()
```




