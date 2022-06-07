### What is Netpie 
---
NETPIE is an IoT cloud-based platform-as-a-service that helps connect your IoT devices together seamlessly by pushing the complexity from the hands of application developers or device manufacturers to the cloud.

![]([https://netpie.io/static/media/NETPIE2020_Bg_banner.bb43c58c.png](https://raw.githubusercontent.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/aea13b65b52dc46e196bd7f733ed4f85fbd0d19f/doc/NETPIE2020_Bg_banner.bb43c58c.png))

### Feature
---
1. Capability to connect with any hardware platforms and applications regardless of computer languages involved.
2. Flexible ID/authorization management in which users can conveniently and dynamically add, drop and group their authorized devices based on their needs. This feature is very powerful for the users that build IoT products for third-party use such as IoT consumer product company
3. Virtual database that stores the latest status and sensing data for each individual device. Writing application to interact with IoT devices can become much easier
4. Trigger/notification functions and data preparation for storage that can be done on the platform instead of hard coding onto the end devices or the applications themselves.
5. API (Application Program Interface) enabling data and devices on NETPIE 2020 to communicate and work with external devices, applications, web services.

### Free Quota
---
A free account, you can access the following features.

1. Set up up to 10 connected devices.
2. 9,000,000 real-time messages per month
3. Make up to 9 dashboards.

All service usage will be reset every month.
For more details, you can visit the service usage in your Netpie account.
https://portal.netpie.io/usage

![](https://raw.githubusercontent.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/95d5930348c373a2cd9116ce170583754518628b/doc/netpie-usage.png)

### Netpie 2015 or Netpie 2020?
---
| Comparison  | Netpie 2015  |Netpie 2020   |
| ------------ | ------------ | ------------ |
|  Design philosophy |  Device-centric|  Platform-centric |
|Commercial-ability|Need to re-program hardware to migrate to a commercial platform|Commercial-ready. Migration to a commercial platform is smooth and painless|
|Suitable usage|Project-based (device makers are device users)|Mass production (device makers are not device users), Project-based (device makers are device users)|
|Target user|Makers, hobbyists, students|Startups, makers of IoT products, hobbyists, students|
|Communication protocol|Microgear (modified MQTT, modified WebSocket) , HTTP|Native MQTT, Native WebSocket, HTTP, CoAP|
|Programming language|Limited to Microgear libraries (e.g., Arduino, Javascript, Python, Node.js, Android)|All programming languages with MQTT library support|
|Hardware support|Limited to those with Microgear support (e.g., esp32, esp8266, Arduino mega 2560, embedded Linux)|Unlimited as long as it supports MQTT|
|Device identity and group|Use APPID. Device identity and group must be programmed into firmware.|No more APPID. Device identity and group can be adjusted anytime even after product is sold/installed.|
|Rate limit|Everyone is subject to the same rate limit, for example 4 data-points per minute, and 10 real-time messages per second.|Rate limit is measured per month, allowing for dynamic burst usage, for example 1 million data-points per month, and 9 million real-time messages per month.|
|Trigger & Action|Set triggers for action by programming into IoT devices|Can set triggers and event hooks in cloud platform|









