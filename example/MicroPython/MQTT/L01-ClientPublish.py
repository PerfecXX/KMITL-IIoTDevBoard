# ---Import Library---
from network import WLAN,STA_IF
from simple import MQTTClient

# Network Credential
ssid = ''
password = ''

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
client_ID = ''
broker = 'broker.hivemq.com'

# Set MQTT Profile
client = MQTTClient(client_ID,broker)

# ---Start MQTT Connection---
print('Broker Connecting...')
client.connect()
print('Broker Connected!')

# --- Publish data to broker---
topic = '@msg/data'
message = 'test!'
print('publish {} to {}'.format(message,topic))
client.publish(topic,message)





