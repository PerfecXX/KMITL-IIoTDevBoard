# ---Import Library---
from network import STA_IF,WLAN

# ---Setup Wireless LAN Interface---
wlan = WLAN(STA_IF) # Set WLAN interface to Station Mode
wlan.active(True)   # Activate WLAN Interface
scan = wlan.scan()  # Scan nearby Wireless Network and return as list 

# ---Main Program---
for wifi in scan:
    print('SSID:',wifi[0].decode('utf8')) # Wireless SSID 
    print('Channel:',wifi[2])             # Connection Channel
    print('Signal Strength:',wifi[3])     # RSSI (Received Signal Strength Indicator)
    print('---')
