# ---Import Library---
from network import WLAN,STA_IF
from simple import MQTTClient
from time import sleep

# Network Credential
ssid = 'iMakeEDU'
password = 'imake1234'

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

# MQTT Credential
# (Depending on the broker connection requirement)
# (Some broker might require more connection credential)
client_ID = 'username_1991'
broker = 'broker.hivemq.com'

# MQTT Callback Function
# This function must be called with client.set_callback() only 
def on_message(topic,msg):
    # decode the incoming data type
    # from byte to normal text
    topic,msg = topic.decode('utf8'),msg.decode('utf8')
    print('message from ',topic ,msg)


# Set MQTT Profile
client = MQTTClient(client_ID,broker)

# Sets the function for receiving data from the broker.
client.set_callback(on_message)

# ---Start MQTT Connection---
print('Broker Connecting...')
client.connect()
print('Broker Connected!')

# ---Subscribe topic---
# The subscribe topic must be the same topic as the publisher
# otherwise the client can not recieve the data
topic = '@msg/data'
client.subscribe(topic)
print('Waiting')
# ---Main Program---
while True:
    # Checks any messsage are sent from broker or not 
    # if it true, the function that setting with .set_callback() will be called
    client.check_msg()
    sleep(0.5)
