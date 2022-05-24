# ---Import Library---
from network import WLAN,STA_IF

# Network Credential
ssid = ''
password = ''

# Network Interface 
wlan = WLAN(STA_IF)
wlan.active(True)

# Start Connection
print('Connecting...')
wlan.connect(ssid,password)
while not wlan.isconnected():
    pass

# Connection Config
print(wlan.ifconfig())
