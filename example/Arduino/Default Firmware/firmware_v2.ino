/*
Author      : Teeraphat Kullanankanjana
Version     : 1.0
Date        : 10/08/2567
Description : This code is designed for the KMITL IIoT Dev Board V2. It demonstrates various features
              including RGB LED control, buzzer, relays, sensors, motors, and MAX485 communication. 
              The code utilizes an OLED display to show the current mode and status of the components.
              The user can navigate through different demo modes using buttons, where each mode 
              highlights specific functionalities of the board.
Copyright (C) 2024 Teeraphat Kullanankanjana. All rights reserved.
*/

#include <Wire.h>
#include <Adafruit_NeoPixel.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "DHT.h"

// Pin definitions for various components on the KMITL IIoT Dev Board
#define SW1_PIN 35          // Switch 1
#define SW2_PIN 2           // Switch 2
#define SW3_PIN 0           // Switch 3
#define LED_PIN 23          // RGB LED
#define LDR_PIN 36          // Light Dependent Resistor
#define POT_PIN 39          // Potentiometer
#define OPTO_PIN 34         // Opto-isolator
#define BUZZER_PIN 33       // Buzzer
#define IR_PIN 25           // Infrared Sensor
#define RELAY1_PIN 14       // Relay 1
#define RELAY2_PIN 12       // Relay 2
#define DHT_PIN 32          // DHT11 Sensor
#define MAX_DIR_PIN 5       // MAX485 Direction Pin
#define MAX_IN_PIN 17       // MAX485 Input Pin
#define MAX_OUT_PIN 16      // MAX485 Output Pin
#define MOTOR_1A_PIN 19     // Motor 1A
#define MOTOR_1B_PIN 18     // Motor 1B
#define MOTOR_2A_PIN 27     // Motor 2A
#define MOTOR_2B_PIN 26     // Motor 2B

#define mode_limit 9        // Total number of demo modes

#define SCREEN_WIDTH 128    // OLED display width, in pixels
#define SCREEN_HEIGHT 64    // OLED display height, in pixels

// OLED display object connected to I2C
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

// NeoPixel object for controlling the RGB LED
Adafruit_NeoPixel pixels(3, LED_PIN, NEO_GRB + NEO_KHZ800); 

// DHT11 sensor object for temperature and humidity readings
DHT dht(DHT_PIN, DHT11);

unsigned int demo_mode = 0; // Variable to keep track of the current demo mode

// Button states
int but_1_last_state = HIGH;
int but_2_last_state = HIGH;
int but_3_last_state = HIGH;
int but_1_state = HIGH;
int but_2_state = HIGH;
int but_3_state = HIGH;

int rgb[3][4] = {{0, 0, 0, 0}, {0, 0, 0, 0}}; // RGB values for two LEDs

int color_diff = 0;           // Variable for color adjustments
int rgb_select = 0;           // To track which color (R, G, B) is being adjusted
int buzzer_freq = 2000;       // Frequency for the buzzer
int motor_freq = 800;         // Frequency for the motor
int relay1_state = 0;         // State of Relay 1 (ON/OFF)
int relay2_state = 0;         // State of Relay 2 (ON/OFF)
int opto_state = 0;           // State of the opto-isolator

int motor_select = 0;         // To track which motor is being adjusted
int motor_value[2] = {0, 0};  // Speed values for two motors

unsigned char tmp_counter = 0;         // Counter for button presses
unsigned char last_tmp_counter = 0;    // Last counter value
unsigned long last_press_time = 0;     // Last time a button was pressed

void setup() {
  Serial.begin(115200); // Initialize serial communication at 115200 baud

  // Initialize the OLED display
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { 
    Serial.println(F("SSD1306 allocation failed"));
    for (;;); // Stop if OLED initialization fails
  }
  delay(1000); // Delay to allow OLED to initialize

  // Display an initial message on the OLED
  display.clearDisplay();
  display.setTextSize(1);               
  display.setTextColor(SSD1306_WHITE);  
  display.setCursor(0, 0);              

  display.println(F("Hello, PerfecXX!"));
  display.println(F("initializing..."));

  // Initialize MAX485 communication
  Serial2.begin(9600, SERIAL_8N1, MAX_IN_PIN, MAX_OUT_PIN);

  // Set pin modes for switches and other components
  pinMode(SW1_PIN, INPUT_PULLUP);
  pinMode(SW2_PIN, INPUT_PULLUP);
  pinMode(SW3_PIN, INPUT_PULLUP);

  pinMode(OPTO_PIN, INPUT);
  pinMode(POT_PIN, INPUT);
  pinMode(LDR_PIN, INPUT);

  pinMode(RELAY1_PIN, OUTPUT);
  digitalWrite(RELAY1_PIN, LOW);
  pinMode(RELAY2_PIN, OUTPUT);
  digitalWrite(RELAY2_PIN, LOW);
  pinMode(LED_PIN, OUTPUT);

  pinMode(MAX_DIR_PIN, OUTPUT);
  digitalWrite(MAX_DIR_PIN, LOW);

  // Initialize NeoPixel (RGB LED)
  pixels.begin();
  pixels.clear();

  // Configure PWM channels for buzzer and motors
  ledcAttachPin(BUZZER_PIN, 1);
  ledcSetup(1, buzzer_freq, 8);
  ledcWrite(1, 0);

  ledcAttachPin(MOTOR_1A_PIN, 2);
  ledcSetup(2, motor_freq, 8);
  ledcWrite(2, 0);

  ledcAttachPin(MOTOR_1B_PIN, 3);
  ledcSetup(3, motor_freq, 8);
  ledcWrite(3, 0);

  ledcAttachPin(MOTOR_2A_PIN, 4);
  ledcSetup(4, motor_freq, 8);
  ledcWrite(4, 0);

  ledcAttachPin(MOTOR_2B_PIN, 5);
  ledcSetup(5, motor_freq, 8);
  ledcWrite(5, 0);

  // Initialize DHT sensor
  dht.begin();

  // Set initial colors for RGB LEDs
  pixels.setPixelColor(0, pixels.Color(0, 0, 0));
  pixels.setPixelColor(1, pixels.Color(0, 0, 0));
  pixels.show();

  // Display the initial screen
  display.display();
  delay(2000);

  // Save the last state of buttons
  but_1_last_state = but_1_state;
  but_2_last_state = but_2_state;
  but_3_last_state = but_3_state;
}

void loop() {
  // Read the state of the buttons
  but_1_state = digitalRead(SW1_PIN);
  but_2_state = digitalRead(SW2_PIN);
  but_3_state = digitalRead(SW3_PIN);

  // Handle button 1 press (long press to change mode)
  if (but_1_state != but_1_last_state && but_1_state == LOW) {
    last_press_time = millis();
  }

  if (but_1_state == LOW && (millis() - last_press_time) > 1500) { // If button held for > 1.5 seconds
    last_press_time = millis();
    demo_mode++; // Change to the next demo mode
    if (demo_mode > mode_limit) {
      demo_mode = 0; // Loop back to the first mode
    }
  }

  // Handle button 2 and button 3 presses (for adjusting values)
  if (but_2_state != but_2_last_state && but_2_state == LOW) {
    tmp_counter++;
  }

  if (but_3_state != but_3_last_state && but_3_state == LOW) {
    tmp_counter--;
  }

  // Display different content based on the current demo mode
  if (demo_mode == 0) { // Default mode (display mode)
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println(F("IIOTV2 DEV Board EX"));
    display.println(F("Demo 1 : Display"));
    display.print(F("Char(a-z) -> "));
    int num = tmp_counter;
    if (num < 0) num = -num;
    if (num > 26) num = num % 26;
    display.printf("%c", 'a' + (num % 26));
    display.setCursor(0, 64 - 27);
    display.print(F("HOLD SW1 1 SEC to GO!"));
    display.setCursor(0, 64 - 9);
    display.print(F("SW2:UP SW3:DOWN"));
    display.display();
  }
  else if (demo_mode == 1) { // RGB LED control
    // Update RGB values based on button presses
    rgb[rgb_select / 2][rgb_select % 2] += (last_tmp_counter - tmp_counter) * 5;
    if (rgb[rgb_select / 2][rgb_select % 2] < 0) rgb[rgb_select / 2][rgb_select % 2] = 0;
    if (rgb[rgb_select / 2][rgb_select % 2] > 255) rgb[rgb_select / 2][rgb_select % 2] = 255;

    // Update the colors on the RGB LEDs
    pixels.setPixelColor(0, pixels.Color(rgb[0][0], rgb[0][1], rgb[0][2]));
    pixels.setPixelColor(1, pixels.Color(rgb[1][0], rgb[1][1], rgb[1][2]));
    pixels.show();

    // Display RGB values on the OLED
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println(F("IIOTV2 DEV Board EX"));
    display.println(F("Demo 2 : RGB LED"));
    display.setCursor(0, 20);
    display.printf("RGB1 = %03d,%03d,%03d\n", rgb[0][0], rgb[0][1], rgb[0][2]);
    display.printf("RGB2 = %03d,%03d,%03d\n", rgb[1][0], rgb[1][1], rgb[1][2]);
    display.display();
  }
  else if (demo_mode == 2) { // Buzzer control
    ledcWrite(1, 120); // Initialize buzzer with a base duty cycle

    // Display the buzzer mode on the OLED
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println(F("IIOTV2 DEV Board EX"));
    display.println(F("Demo 3 : Buzzer"));
    display.setCursor(0, 20);

    // Handle button 1 press to cycle between frequency and duty cycle adjustment
    if (but_1_last_state != but_1_state && but_1_state == LOW) {
      rgb_select++;
      if (rgb_select > 2) rgb_select = 0;
    }

    // Adjust buzzer frequency or duty cycle based on button presses
    if (rgb_select == 0) { // Adjust frequency
      buzzer_freq += (last_tmp_counter - tmp_counter) * 5;
      if (buzzer_freq < 0) buzzer_freq = 0;
      if (buzzer_freq > 2000) buzzer_freq = 2000;
      ledcWriteTone(1, buzzer_freq);
    } else { // Adjust duty cycle
      int buzzer_duty = ledcRead(1);
      buzzer_duty += (last_tmp_counter - tmp_counter) * 5;
      if (buzzer_duty < 0) buzzer_duty = 0;
      if (buzzer_duty > 255) buzzer_duty = 255;
      ledcWrite(1, buzzer_duty);
    }

    // Display the current frequency or duty cycle on the OLED
    display.printf("Buzzer %s : %d\n", rgb_select == 0 ? "Freq" : "Duty", ledcRead(1));
    display.display();
  }
  else if (demo_mode == 3) { // Relay control
    // Toggle relay states with button presses
    if (but_1_last_state != but_1_state && but_1_state == LOW) {
      relay1_state = !relay1_state;
      digitalWrite(RELAY1_PIN, relay1_state);
    }

    if (but_2_last_state != but_2_state && but_2_state == LOW) {
      relay2_state = !relay2_state;
      digitalWrite(RELAY2_PIN, relay2_state);
    }

    // Display the relay states on the OLED
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println(F("IIOTV2 DEV Board EX"));
    display.println(F("Demo 4 : Relay"));
    display.setCursor(0, 20);
    display.printf("Relay 1 : %s\n", relay1_state ? "ON" : "OFF");
    display.printf("Relay 2 : %s\n", relay2_state ? "ON" : "OFF");
    display.display();
  }
  else if (demo_mode == 4) { // LDR sensor reading
    int ldr_val = analogRead(LDR_PIN); // Read LDR value
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println(F("IIOTV2 DEV Board EX"));
    display.println(F("Demo 5 : LDR"));
    display.setCursor(0, 20);
    display.printf("LDR Value : %d\n", ldr_val);
    display.display();
  }
  else if (demo_mode == 5) { // Potentiometer reading
    int pot_val = analogRead(POT_PIN); // Read potentiometer value
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println(F("IIOTV2 DEV Board EX"));
    display.println(F("Demo 6 : POT"));
    display.setCursor(0, 20);
    display.printf("POT Value : %d\n", pot_val);
    display.display();
  }
  else if (demo_mode == 6) { // Opto-isolator state
    int opt_val = digitalRead(OPTO_PIN); // Read opto-isolator state
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println(F("IIOTV2 DEV Board EX"));
    display.println(F("Demo 7 : OPT"));
    display.setCursor(0, 20);
    display.printf("OPT Value : %s\n", opt_val == HIGH ? "HIGH" : "LOW");
    display.display();
  }
  else if (demo_mode == 7) { // IR sensor state
    int ir_val = digitalRead(IR_PIN); // Read IR sensor state
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println(F("IIOTV2 DEV Board EX"));
    display.println(F("Demo 8 : IR Sensor"));
    display.setCursor(0, 20);
    display.printf("IR Value : %s\n", ir_val == HIGH ? "HIGH" : "LOW");
    display.display();
  }
  else if (demo_mode == 8) { // DHT11 sensor readings
    float h = dht.readHumidity();  // Read humidity from DHT11 sensor
    float t = dht.readTemperature(); // Read temperature from DHT11 sensor
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println(F("IIOTV2 DEV Board EX"));
    display.println(F("Demo 9 : DHT11 Sensor"));
    display.setCursor(0, 20);
    display.printf("Temp : %.1fC\n", t);
    display.printf("Humidity : %.1f%%\n", h);
    display.display();
  }
  else if (demo_mode == 9) { // Motor control
    // Cycle through motor selection with button 1
    if (but_1_last_state != but_1_state && but_1_state == LOW) {
      motor_select++;
      if (motor_select > 3) motor_select = 0;
    }

    // Adjust motor speeds based on button presses
    motor_value[motor_select / 2] += (last_tmp_counter - tmp_counter) * 5;
    if (motor_value[motor_select / 2] < 0) motor_value[motor_select / 2] = 0;
    if (motor_value[motor_select / 2] > 255) motor_value[motor_select / 2] = 255;

    if (motor_select == 0) ledcWrite(2, motor_value[0]);
    if (motor_select == 1) ledcWrite(3, motor_value[0]);
    if (motor_select == 2) ledcWrite(4, motor_value[1]);
    if (motor_select == 3) ledcWrite(5, motor_value[1]);

    // Display motor speeds on the OLED
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println(F("IIOTV2 DEV Board EX"));
    display.println(F("Demo 10 : Motor"));
    display.setCursor(0, 20);
    display.printf("Motor 1 : %d\n", motor_value[0]);
    display.printf("Motor 2 : %d\n", motor_value[1]);
    display.display();
  }

  // Update button states
  but_1_last_state = but_1_state;
  but_2_last_state = but_2_state;
  but_3_last_state = but_3_state;
  last_tmp_counter = tmp_counter;
}
