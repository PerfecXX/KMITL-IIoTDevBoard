### ESP32 Compatibility 
---
The ESP32 Devkitc V4 has the most compatibility with the KMITL AIoT Development Board. 
However, other ESP32 boards of the same size and number of pins can be used as well.
### ESP32 Devkitc V4 Pinout
---

![](https://raw.githubusercontent.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/e8b1702f366df84dbe1966acc9b5bd7ccfc49736/doc/pinout.png)

|   GPIO|Input   |Output   |Notes   |
| ------------ | ------------ | ------------ | ------------ |
|0   |pulled up   |OK   |outputs PWM signal at boot|
|1   |TX PIN   |OK   |debug output at boot   |
|2   |OK   |OK   |connected to on-board LED   |
|3   |OK   |RX pin   |HIGH at boot   |
|4   |OK   |OK   |   |
|5   |OK   |OK   |outputs PWM signal at boot   |
|6   |X   |X   |connected to the integrated SPI flash|
|7   |X   |X   |connected to the integrated SPI flash|
|8   |X   |X   |connected to the integrated SPI flash|
|9   |X   |X   |connected to the integrated SPI flash|
|10   |X   |X   |connected to the integrated SPI flash|
|11   |X   |X   |connected to the integrated SPI flash|
|12   |OK   |OK   |boot fail if pulled high   |
|13   |OK   |OK   |   |
|14   |OK   |OK   |outputs PWM signal at boot     |
|15   |OK   |OK   |outputs PWM signal at boot     |
|16   |OK   |OK   |   |
|17   |OK   |OK   |   |
|18   |OK   |OK   |   |
|19   |OK   |OK   |   |
|21   |OK   |OK   |   |
|22   |OK   |OK   |   |
|23   |OK   |OK   |   |
|25   |OK   |OK   |   |
|26   |OK   |OK   |   |
|27   |OK   |OK   |   |
|32   |OK   |OK   |   |
|33   |OK   |OK   |   |
|34   |OK   |  - |input only   |
|35   |OK   |  - |input only   |
|36   |OK   |  - |input only   |
|39   |OK   | -  |input only   |

### KMITL AIoT Development Board Pin Reference 
---

![](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/aiot-module.png?raw=true)

The following ESP32 GPIO are connected with the KMITL AIoT Development Board.

|   GPIO |   Module/Sensor | Notes|
| ------------ | ------------ | ------------ |
|0                  |Button                              |Button 3|
|2                  |Button                              |Button 2|
|4                  |Button                              |Button 4|
|5                  |MAX485                           |MAX DIR|
|13                |DHT11                              |DHT11 Data|
|14                |Relay                                |Relay 1|
|15                |Button                              |Button 1|
|16                |MAX485                           |MAX Out|
|17                |MAX485                           |MAX In|
|21                |SSD1306                          |SSD1306 SDA|
|22                |SSD1306                          |SSD1306 SCL|
|23                |NeoPixel                          |NeoPixel Signal|
|27                |Relay                                |Relay 2|
|26                |IR Sensor                         |IR Sensor|
|32                |Buzzer                             |Buzzer PWM|
|34                |PC817 Opto Isolator       |OPTO IN1 signal |
|35                |PC817 Opto Isolator       |OPTO IN2 signal |
|36                |LDR                                 |LDR signal |
|39                |W103 Potentiometer      |POT signal |




