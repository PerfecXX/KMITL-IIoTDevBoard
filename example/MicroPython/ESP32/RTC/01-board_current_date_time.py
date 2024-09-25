# ---Import Library---
from machine import RTC

# Create RTC Instance
rtc = RTC()
current_datetime = rtc.datetime()
print("Board's current time:", current_datetime)
