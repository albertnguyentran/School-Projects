#include "DHT.h"
#define DHTTYPE DHT11
int dht_pin = 6;
DHT dht(dht_pin, DHTTYPE); //create object
void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop(){
  delay(2000);
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);
  float heat_index_F = dht.computeHeatIndex(f, h);
  float heat_index_C = dht.computeHeatIndex(t, h, false);
  if (isnan(h)  isnan(t)  isnan(f)) {
    Serial.println("Not able to Read");
    return;
  }

  Serial.print("Humidity is ");
  Serial.print(h);
  Serial.print("\n");
  Serial.print("Temperature is");
  Serial.print("\t");
  Serial.print(t);
  Serial.print(" Degree Celcius");
  Serial.print("\t");
  Serial.print(f);
  Serial.print("Heat index is");
  Serial.print(heat_index_C);
  Serial.print("Degree Celcius");
}