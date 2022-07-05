### Netpie Free Board
---
After you publish your data to the device shadow, you can visualize the data with a widget in Netpie Free Board.

![](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/netpie-freeboard-Detail.png?raw=true)

### Create Free Board
---

1. On the left-side menu, select `Free Board`.
2. Click the `Create` button on the right-top menu. 
3. Enter a Free Board name, then click `create` (description is optional).

![](https://raw.githubusercontent.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/a34d0f8880a35582034cd26cf3e1d546473276f8/doc/netpie-freeboard-create.png)

### DataSources
---
Datasource is the source of the data from the Netpie device that you want to visualize in the Netpie widget. For example, the data from Device Shadow, the data from Subscribe topic.

### Create The Datasources
---

1. After creating the free board, open it.
2. Click the `Add` at the top-right of the window.
3. Enter the datasource name.
4. Enter the `ID` and `token` of the device you want to read.
5. Enter the `subscribed topic` (optional, if you want to read the data from a subscribed topic)
6. Click `Save` (The rest are optional, no need to specify yet).

![](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/netpie-freeboard-datasource-create.png?raw=true)

### Create the Widget 
---

1. Click ADD PANE in the right-side menu.
2. Click the wrench icon in the empty pane to configure the pane name and number of columns in the pane.
3. Inside the empty pane, click + and select a widget type (in this example, let's start with the Text widget).
4. Fill in the widget title in the titile field.
5. In the value field, select your data sources, then navigate to the value you want to visualize in the widget.
6. Click `Save` (Other options are optional).

![](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/netpie-widget-text-create-demo.png?raw=true)

![](https://raw.githubusercontent.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/f95d1d3b364a29a6a24a50897e34ed4adbd7aa29/doc/netpie-widget-text-success-demo.png)

###Add more widgets
---
You can add more widgets by clicking `+` in the widget pane or adding the new widget pane and repeating the previous step. 

![](https://raw.githubusercontent.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/bfd6fece41accff9d7c413e9de2e67b23d9a7e06/doc/netpie-widget-move.png)


### Saving Freeboard
---
After you create or modify your dashboard, do not forget to click the Save menu at the left. The fact that the Netpie does not auto save your session means you need to do a manual save every time you change.  

![](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard/blob/main/doc/netpie-widget-save.png?raw=true)
