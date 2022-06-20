### Connect Your Device to Netpie with MicroPython.
---
Before connecting to Netpie, we need to connect to the internet first.
Then connect to Netpie with the MQTT Protocol.
The ESP32 is capable of connecting to the internet via a wireless network.

1. Create a new .py file and copy the following code: (Download the full code [here](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/example/Netpie/L01-ConnectionTest.py "here")).
2. Replace the SSID and password with your wifi SSID and wifi password.
3. Replace the client_ID, token, and secret with your client_ID, token, and secret.

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
    
    # Set MQTT Profile
    client = MQTTClient(client_ID,broker,
                        user=token,
                        password=secret)
    # ---Start MQTT Connection---
    print('Broker Connecting...')
    client.connect()
    print('Broker Connected!')
```
4.Download `simple.py` (Micorpython MQTT library) [Here](https://github.com/micropython/micropython-lib/blob/master/micropython/umqtt.simple/umqtt/simple.py "Here").
5.Then, upload `simple.py` to your board and run the code.
6.If the connection is successful, the Netpie device status will change to green. 

![Netpie Device ](https://raw.githubusercontent.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/28e8c6fb486f822cee39fac4060e1d0bfd18ade5/doc/netpie-connection-test-ok.png "Netpie Device ")



