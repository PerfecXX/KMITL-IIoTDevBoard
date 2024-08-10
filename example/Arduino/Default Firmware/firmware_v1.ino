/*
Author      : Teeraphat Kullanankanjana
Version     : 1.0
Date        : 10/08/2567
Description : Example program for IIOT Dev Board V1 demonstrating various hardware functionalities, including OLED display, RGB LEDs, Buzzer, Relays, Optocouplers, Analog sensors, DHT sensor, and MAX485 communication.
Copyright (C) 2024 Teeraphat Kullanankanjana. All rights reserved.
*/

#include <Wire.h>
#include <Adafruit_NeoPixel.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "DHT.h"

// Pin Definitions
#define SW1_PIN 15
#define SW2_PIN 2
#define SW3_PIN 0
#define SW4_PIN 4
#define LED_PIN 23
#define LDR_PIN 36
#define POT_PIN 39
#define OPTO1_PIN 34
#define OPTO2_PIN 35
#define BUZZER_PIN 32
#define IR_PIN 26
#define RELAY1_PIN 14
#define RELAY2_PIN 27
#define DHT_PIN 13
#define MAX_DIR_PIN 5
#define MAX_IN_PIN 17
#define MAX_OUT_PIN 16

// Constants
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
#define mode_limit 8 // Number of demo modes

// Objects
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);
Adafruit_NeoPixel pixels(3, LED_PIN, NEO_GRB + NEO_KHZ800);
DHT dht(DHT_PIN, DHT11);

// Global Variables
unsigned int demo_mode = 0;
int but_1_last_state = HIGH;
int but_2_last_state = HIGH;
int but_3_last_state = HIGH;
int but_4_last_state = HIGH;
int but_1_state = HIGH;
int but_2_state = HIGH;
int but_3_state = HIGH;
int but_4_state = HIGH;
char last_get_char = '0';

int rgb[2][3] = {{0, 0, 0}, {0, 0, 0}}; // Two RGB LEDs
int last_demo_state = HIGH;
int rgb_select = 0;
int buzzer_freq = 2000;
int relay1_state = 0;
int relay2_state = 0;
int opto1_state = 0;
int opto2_state = 0;
unsigned char tmp_counter = 0;
unsigned char last_tmp_counter = 0;

void setup() {
  // Initialize Serial Communication
  Serial.begin(115200);

  // Initialize OLED Display
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;); // Don't proceed, loop forever
  }
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println(F("Hello, Haruhi!"));
  display.println(F("initializing..."));
  display.display();

  // Initialize NeoPixel
  pixels.begin();
  pixels.clear();
  pixels.show();

  // Initialize DHT Sensor
  dht.begin();

  // Initialize Pins
  pinMode(SW1_PIN, INPUT_PULLUP);
  pinMode(SW2_PIN, INPUT_PULLUP);
  pinMode(SW3_PIN, INPUT_PULLUP);
  pinMode(SW4_PIN, INPUT_PULLUP);
  pinMode(OPTO1_PIN, INPUT);
  pinMode(OPTO2_PIN, INPUT);
  pinMode(POT_PIN, INPUT);
  pinMode(LDR_PIN, INPUT);
  pinMode(RELAY1_PIN, OUTPUT);
  digitalWrite(RELAY1_PIN, LOW);
  pinMode(RELAY2_PIN, OUTPUT);
  digitalWrite(RELAY2_PIN, LOW);
  pinMode(LED_PIN, OUTPUT);
  pinMode(MAX_DIR_PIN, OUTPUT);
  digitalWrite(MAX_DIR_PIN, LOW);

  // Initialize Buzzer
  ledcAttachPin(BUZZER_PIN, 1);
  ledcSetup(1, buzzer_freq, 8);
  ledcWrite(1, 0);

  delay(2000);
}

void loop() {
  // Update Button States
  but_1_state = digitalRead(SW1_PIN);
  but_2_state = digitalRead(SW2_PIN);
  but_3_state = digitalRead(SW3_PIN);
  but_4_state = digitalRead(SW4_PIN);

  // Handle Button Presses
  handleButtonPresses();

  // Update Display Based on Current Demo Mode
  updateDisplay();

  // Save Last Button States
  but_1_last_state = but_1_state;
  but_2_last_state = but_2_state;
  but_3_last_state = but_3_state;
  but_4_last_state = but_4_state;
  last_demo_state = demo_mode;
  last_tmp_counter = tmp_counter;

  delay(20);
}

/**
 * Handles button presses and updates the demo mode and other states accordingly.
 */
void handleButtonPresses() {
  if (but_1_state != but_1_last_state && but_1_state == LOW) {
    demo_mode = (demo_mode + 1) % (mode_limit + 1);
  }
  if (but_2_state != but_2_last_state && but_2_state == LOW) {
    tmp_counter++;
  }
  if (but_3_state != but_3_last_state && but_3_state == LOW) {
    tmp_counter--;
  }
  if (but_4_state != but_4_last_state && but_4_state == LOW) {
    // Functionality for button 4 press in each mode is handled in updateDisplay()
  }
}

/**
 * Updates the OLED display based on the current demo mode.
 */
void updateDisplay() {
  switch (demo_mode) {
    case 0:
      displayDefaultMode();
      break;
    case 1:
      displayRGBMode();
      break;
    case 2:
      displayBuzzerMode();
      break;
    case 3:
      displayRelayMode();
      break;
    case 4:
      displayOptoMode();
      break;
    case 5:
      displayAnalogMode();
      break;
    case 6:
      displayDHTMode();
      break;
    case 7:
      displayMAX485ReceiverMode();
      break;
    case 8:
      displayMAX485SenderMode();
      break;
  }
}

/**
 * Display functions for each demo mode.
 * These functions handle the specific display logic for each mode.
 */

void displayDefaultMode() {
  display.clearDisplay();
  display.setCursor(0, 0);
  display.println(F("IIOT DEV Board EX"));
  display.println(F("Demo 1 : Display"));
  display.print(F("Char(a-z) -> "));
  int num = abs(tmp_counter) % 26;
  display.printf("%c", 'a' + num);
  display.setCursor(0, 64 - 9);
  display.print(F("SW1:Next SW2:U SW3:D"));
  display.display();
}

void displayRGBMode() {
  if (but_4_state != but_4_last_state && but_4_state == LOW) {
    rgb_select = (rgb_select + 1) % 6;
  }
  if (last_tmp_counter != tmp_counter) {
    updateRGBValues();
  }
  display.clearDisplay();
  display.drawLine((rgb_select / 3) * 50, 28 + (rgb_select % 3) * 10, 38 + (rgb_select / 3) * 50, 28 + (rgb_select % 3) * 10, SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println(F("IIOT DEV Board EX"));
  display.println(F("Demo 2 : LED RGB"));
  displayRGBValues();
  display.setCursor(0, 64 - 9);
  display.print(F("SW4:Select SW2&3:Col"));
  display.display();
}

void displayBuzzerMode() {
  if (last_tmp_counter != tmp_counter) {
    buzzer_freq += (last_tmp_counter - tmp_counter) * 25;
    buzzer_freq = constrain(buzzer_freq, 100, 5000);
  }
  if (but_4_state != but_4_last_state) {
    if (but_4_state == LOW) {
      ledcSetup(1, buzzer_freq, 8);
      ledcWrite(1, 128);
    } else {
      ledcWrite(1, 0);
    }
  }
  display.clearDisplay();
  display.setCursor(0, 0);
  display.println(F("IIOT DEV Board EX"));
  display.println(F("Demo 3 : BUZZER"));
  display.setCursor(0, 20);
  display.print(F("Frequency : "));
  display.print(buzzer_freq);
  display.setCursor(0, 64 - 9);
  display.print(F("SW1:Next SW4:PLAY"));
  display.setCursor(0, 64 - 19);
  display.print(F("SW2:Up  SW3:Down"));
  display.display();
}

void displayRelayMode() {
  if (but_3_state != but_3_last_state) {
    relay1_state = (relay1_state == 0) ? 1 : 0;
    digitalWrite(RELAY1_PIN, relay1_state);
  }
  if (but_4_state != but_4_last_state) {
    relay2_state = (relay2_state == 0) ? 1 : 0;
    digitalWrite(RELAY2_PIN, relay2_state);
  }
  display.clearDisplay();
  display.setCursor(0, 0);
  display.println(F("IIOT DEV Board EX"));
  display.println(F("Demo 4 : RELAY"));
  display.setCursor(0, 20);
  display.print(F("Relay 1 : "));
  display.print(relay1_state ? "ON" : "OFF");
  display.setCursor(0, 30);
  display.print(F("Relay 2 : "));
  display.print(relay2_state ? "ON" : "OFF");
  display.setCursor(0, 64 - 9);
  display.print(F("SW3:ON/OFF Relay 1"));
  display.setCursor(0, 64 - 19);
  display.print(F("SW4:ON/OFF Relay 2"));
  display.display();
}

void displayOptoMode() {
  opto1_state = digitalRead(OPTO1_PIN);
  opto2_state = digitalRead(OPTO2_PIN);
  display.clearDisplay();
  display.setCursor(0, 0);
  display.println(F("IIOT DEV Board EX"));
  display.println(F("Demo 5 : OPTO"));
  display.setCursor(0, 20);
  display.print(F("Opto 1 : "));
  display.print(opto1_state ? "HIGH" : "LOW");
  display.setCursor(0, 30);
  display.print(F("Opto 2 : "));
  display.print(opto2_state ? "HIGH" : "LOW");
  display.setCursor(0, 64 - 9);
  display.print(F("SW1:Next SW2:Up SW3:D"));
  display.display();
}

void displayAnalogMode() {
  int ldr_value = analogRead(LDR_PIN);
  int pot_value = analogRead(POT_PIN);
  display.clearDisplay();
  display.setCursor(0, 0);
  display.println(F("IIOT DEV Board EX"));
  display.println(F("Demo 6 : Analog"));
  display.setCursor(0, 20);
  display.print(F("LDR  : "));
  display.print(ldr_value);
  display.setCursor(0, 30);
  display.print(F("POT  : "));
  display.print(pot_value);
  display.setCursor(0, 64 - 9);
  display.print(F("SW1:Next SW2:Up SW3:D"));
  display.display();
}

void displayDHTMode() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  display.clearDisplay();
  display.setCursor(0, 0);
  display.println(F("IIOT DEV Board EX"));
  display.println(F("Demo 7 : DHT"));
  display.setCursor(0, 20);
  display.print(F("Temp : "));
  display.print(t);
  display.println(" *C");
  display.print(F("Humid: "));
  display.print(h);
  display.println(" %");
  display.setCursor(0, 64 - 9);
  display.print(F("SW1:Next SW2:Up SW3:D"));
  display.display();
}

void displayMAX485ReceiverMode() {
  digitalWrite(MAX_DIR_PIN, LOW); // Set to receive mode
  char recv_char;
  if (Serial2.available()) {
    recv_char = Serial2.read();
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println(F("IIOT DEV Board EX"));
    display.println(F("Demo 8 : MAX485 Recv"));
    display.setCursor(0, 20);
    display.print(F("Received: "));
    display.println(recv_char);
    display.display();
    delay(1000);
  }
}

void displayMAX485SenderMode() {
  digitalWrite(MAX_DIR_PIN, HIGH); // Set to send mode
  if (but_4_state != but_4_last_state && but_4_state == LOW) {
    last_get_char = (char)('a' + (rand() % 26));
    Serial2.print(last_get_char);
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println(F("IIOT DEV Board EX"));
    display.println(F("Demo 9 : MAX485 Send"));
    display.setCursor(0, 20);
    display.print(F("Sent: "));
    display.println(last_get_char);
    display.display();
  }
}

/**
 * Updates the RGB values based on the current tmp_counter and rgb_select.
 */
void updateRGBValues() {
  if (rgb_select < 3) {
    rgb[0][rgb_select] = abs(tmp_counter) % 256;
  } else {
    rgb[1][rgb_select - 3] = abs(tmp_counter) % 256;
  }
  pixels.setPixelColor(0, pixels.Color(rgb[0][0], rgb[0][1], rgb[0][2]));
  pixels.setPixelColor(1, pixels.Color(rgb[1][0], rgb[1][1], rgb[1][2]));
  pixels.show();
}

/**
 * Displays the RGB values on the OLED screen.
 */
void displayRGBValues() {
  display.printf("RGB LED1 : (%03d,%03d,%03d)\n", rgb[0][0], rgb[0][1], rgb[0][2]);
  display.printf("RGB LED2 : (%03d,%03d,%03d)\n", rgb[1][0], rgb[1][1], rgb[1][2]);
}
