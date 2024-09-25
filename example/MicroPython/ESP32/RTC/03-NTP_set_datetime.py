# --- Import Library
from network import STA_IF,WLAN
from ntptime import settime
from time import localtime,time
from machine import RTC

# --- Show Current Time---
rtc = RTC()
print("Board's current time:", rtc.datetime())

# ---Network Credential---
ssid = 'your_ssid'
password = 'your_password'

# --- Connect to WIFI---
wlan = WLAN(STA_IF)
wlan.active(True)

if not wlan.isconnected():
    print("Connecting to wifi:", ssid)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass

print("Connection successful")
print("WiFi Config:", wlan.ifconfig())

#---Automatically fetches time from NTP server---
print("Fetching time from NTP server...")
settime()

#---Adjust for Asia/Bangkok timezone (UTC+7)---
current_time = localtime(time() + 7 * 3600)

#---Show the time we got from the NTP server (adjusted for timezone)---
print("Time from NTP server:", current_time)

#---Set the RTC with the current time---
rtc.datetime((current_time[0], current_time[1], current_time[2], 0, current_time[3], current_time[4], current_time[5], 0))
print("RTC set to:", rtc.datetime())


