# ---Import Library---
from machine import Pin
from dht import DHT11
from time import sleep

# ---Pin Setup---
dht_Pin = DHT11(Pin(13))

# ---Main Program---
while True:
    # Reading Sensor Value
    dht_Pin.measure()
    temperature = dht_Pin.temperature() # read the measured temperature.
    humidity = dht_Pin.humidity()       # read the measured humidity.
    
    print('Temperature: {} Humidity {}'.format(temperature,humidity))
    sleep(0.1)                          # delay 0.1 sec
    


