/* Running lights
 
 The circuit:
 * LEDs attached to 2nd, 3rd, 4th, 5th and 6th pins
   having 1k ohm resistors in between.
 */

int ledPins[] = {2, 3, 4, 5, 6};
int numberOfPins = sizeof(ledPins);

void setup()
{
  for (int i = 0; i < numberOfPins; i++)
  {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop()
{
  digitalWrite(ledPins[0], HIGH);
  delay(160);
  digitalWrite(ledPins[0], LOW);
  
  digitalWrite(ledPins[1], HIGH);
  delay(80);
  digitalWrite(ledPins[1], LOW);
  
  digitalWrite(ledPins[2], HIGH);
  delay(80);
  digitalWrite(ledPins[2], LOW);
  
  digitalWrite(ledPins[3], HIGH);
  delay(80);
  digitalWrite(ledPins[3], LOW);
  
  digitalWrite(ledPins[4], HIGH);
  delay(160);
  digitalWrite(ledPins[4], LOW);

  digitalWrite(ledPins[3], HIGH);
  delay(80);
  digitalWrite(ledPins[3], LOW);

  digitalWrite(ledPins[2], HIGH);
  delay(80);
  digitalWrite(ledPins[2], LOW);  
  
  digitalWrite(ledPins[1], HIGH);
  delay(80);
  digitalWrite(ledPins[1], LOW);
}

