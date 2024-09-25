# ---Import Library---
from machine import RTC

# ---Create RTC Instance---
rtc = RTC()

# ---Get current time---
current_datetime = rtc.datetime()
print("Date and time before manual set: ",current_datetime)

# ---Example Time Value---
year = 2024
month = 9
day = 25
weekday = 2
hours = 15
minutes = 7
seconds = 48
subseconds = 81163
# ---Set the board date and time ---
rtc.datetime((year, month, day, weekday, hours, minutes, seconds, subseconds))
print("Time now manual set to : ",rtc.datetime())
