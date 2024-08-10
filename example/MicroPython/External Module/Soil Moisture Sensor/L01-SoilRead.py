# ---Import Library---
from machine import Pin, ADC
from time import sleep

# ---Pin Setup---
soilPin = ADC(Pin(36))

while True:
    # Read soil moisture value
    soil_moisture = soilPin.read()

    # You can map the ADC value to a meaningful range if needed
    # For example, if the sensor output ranges from dry (high ADC value) to wet (low ADC value),
    # you can use a linear mapping like this:
    moisture_percent = (4095 - soil_moisture) / 4095 * 100

    # Print the values
    print("ADC Value:", soil_moisture)
    print("Moisture Percentage:", moisture_percent, "%")

    # Add a delay before the next reading
    sleep(1)

