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
topic = '@private/#'
client.subscribe(topic)

# --- Main Program---
while True:
    # Checks any messsage are sent from broker or not 
    # if it true, the function that setting with .set_callback() will be called
    client.check_msg()
	
    # Publish to Shadow (Requesting Shadow data)
	# No need to enter any message
    client.publish('@shadow/data/get','')
