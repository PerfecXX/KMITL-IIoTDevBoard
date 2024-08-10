# ---Import Library---
from network import WLAN,STA_IF

# Network Credential
ssid = 'replace_with_your_ssid'
password = 'replace_with_your_password'

# Network Interface 
wlan = WLAN(STA_IF)
# Activate the station mode
wlan.active(True)
# Check if the devices are already connected or not.
# If it is not connected, then start the connection.
if not wlan.isconnected():
   print("Connecting to wifi: ", ssid)
   wlan.connect(ssid, password)
   # Wait until your devices are connected.
   while not wlan.isconnected():
       pass
print("Connection successful")

# Connection Config
print(wlan.ifconfig())
