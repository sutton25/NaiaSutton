const int greenPin = 2;  // Green LED
const int redPin = 3;    // Red LED
const int buzzerPin = 4; // Buzzer

void setup() {
  Serial.begin(9600); // Initialize serial communication
  pinMode(greenPin, OUTPUT);
  pinMode(redPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);

  // Ensure LEDs and buzzer are off by default
  digitalWrite(greenPin, LOW);
  digitalWrite(redPin, LOW);
  digitalWrite(buzzerPin, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    String message = Serial.readStringUntil('\n');
    message.trim(); // Remove any trailing spaces or newlines

    if (message == "ON") {
      // If "Naia" is detected, turn on the green LED and turn off the red LED and buzzer
      digitalWrite(greenPin, HIGH);
      digitalWrite(redPin, LOW);
      digitalWrite(buzzerPin, LOW);
      Serial.println("Green LED ON");
    } 
    else if (message == "OFF") {
      // If "Not Naia" is detected, turn on the red LED and buzzer
      digitalWrite(greenPin, LOW);
      digitalWrite(redPin, HIGH);
      digitalWrite(buzzerPin, HIGH);
      Serial.println("Red LED ON and Buzzer ON");
    } 
    else if (message == "EXIT") {
      // Turn off all outputs for exiting
      digitalWrite(greenPin, LOW);
      digitalWrite(redPin, LOW);
      digitalWrite(buzzerPin, LOW);
      Serial.println("Exiting...");
    }
  }
}

