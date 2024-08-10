from machine import UART
from time import sleep

# Configure UART
uart = UART(1, baudrate=9600, tx=17, rx=16)

while True:
    data_to_send = "Hello from Board 1!"
    uart.write(data_to_send)
    sleep(1)
