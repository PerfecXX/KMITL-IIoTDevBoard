### MicroPython Firmware
---
MicroPython is not flashed onto the ESP32 or ESP8266 boards by default. The first thing you need to do to start programming your boards with MicroPython is upload the firmware.

### Download ESP32 MicroPython Firmware
---
1. Go to the ESP32 MicroPython Downloads page: [https://micropython.org/download/esp32/](https://micropython.org/download/esp32/)

2. Scroll your mouse to the very bottom of the web then you should see `Firmware (Compiled with IDF 3.x)`.

3. Select the lastest release to download `.bin` files. 

4. The firmware (.bin) should be downloaded. 

![](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/firmware-download-site.png?raw=true)

### Download and Installing USB Driver. 
---
Before you connect the Micro USB to your computer, you should install the USB Driver first, otherwise Thonny might not find your USB port.

The driver is different depending on the chip on the ESP32. 
But the most ESP32 use CP210x USB to UART Bridge VCP Drivers.
Click [here](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers "here") to nevigate to the download page.

For Windows, select `CP210x Windows Drivers`, then the driver should start downloading. 
For Mac OSX, the driver should be built in with the OS, so there is no need to download it.
![](https://raw.githubusercontent.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/fbab363e6a284c9983e892830b173cca073b5e75/doc/cp210x-download-page.png)

After downloading the CP210x Driver, complete the installation by running the installer.

### Installing ESP32 MicroPython Firmware 
---
1. Connect the Micro USB to the ESP32.
2. Open Thonny IDE.
3. Click the `Run` menu on the top of the window.
4. Then in the dropdown menu click `Select Interpreter`
5. In the option window,change the The same interpreter which run Thonny (Default Interpreter) to `MicroPython ESP32`.
6. Then select your computer port for your ESP32 port.

![](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/thonny-port-selection.png?raw=true)

7. After the port is selected,  click `Install or update firmware` on the right bottom. 
8. In the port entry, select your ESP32 port.
9. Then in the firmware entry, browse to your firmware file (.bin).
10. After that, press and hold the `Boot` button on the ESP32, then click `Install` and wait until done.
![](https://raw.githubusercontent.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/61f80500054531d114dc88d9ec66fc62c792996e/doc/thonny-firmware-flash.png)
11. Close the option window and go back to Thonny IDE. 
12. The Shell should prompt  `MicroPython v<version> on <last update>` and `ESP32 module with ESP32`.Then the left-buttom menu will show `boot.py` inside the `MicroPython Device` window. 
(If you do not see the MicroPython Device window, click the `view` menu on the top, then on the dropdown select the `File` menu. The window should appear.)

![](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/thonny-show-shell.png?raw=true)

### Testing your MicroPython 
---
1. Click the `New` menu on the top (or Ctrl+N) to create a new file, then save it as `main.py` 
2. After that, in the editor coppy the following code.
```python
from machine import Pin
print('Hello World!')
```
3. Save the new file by click `save` (Ctrl+S) to `This computer` 
and `Run` (F5).
4. In the Shell will display `Hello Wolrd`.

![](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/thonny-test-code.png?raw=true)

### Deploy your code
---
When you finish the code and want to save it on the ESP32.
1. Right click the `main.py` in `This computer` window.
2. Select `upload to` and wait until the upload is complete.
3. The upload file will show in `MicroPython Device`  window.

![](https://raw.githubusercontent.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/108f84a37b152ec172c88c07c38d63f28a25e0d5/doc/upload-to-upython-decive.png)

### Upload External Library 
