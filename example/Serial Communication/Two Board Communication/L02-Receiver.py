from machine import UART
from time import sleep


# Configure UART
uart = UART(1, baudrate=9600, tx=17, rx=16)

while True:
    if uart.any():
        received_data = uart.read()
        print("Received Data:", received_data)
    sleep(1)
