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

![](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/KMITL-AIoT-Dev-Board-Layout.jpeg)

The following ESP32 GPIO are connected with the KMITL AIoT Development Board.

|Sensor/Module  |GPIO   |
| ------------ | ------------ |
|Button 1|15|
|Button 2|2|
|Button 3|0|
|Button 4|4|
|Relay 1|14|
|Relay 2|27|
|DHT11 Data|13|
|SSD1306 OLED SDA|21|
|SSD1306 OLED SCL|22|
|NeoPixel Signal|23|
|Buzzer PWM|32|
|LDR Signal|36|
|W103 Potentiometer Signal|39|
|IR Sensor|26|
|MAX485 Out|16|
|MAX485 In|17|
|MAX485 Dir|5|
|PC817 Opto Isolator 1 Signal|34|
|PC817 Opto Isolator 2 Signal|35|








