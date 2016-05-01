#include <OneWire.h>
#include <DS18B20.h>

#define ONEWIRE_PIN 4

String request ="";
//byte request = 0;
byte address[8] = {0x28, 0xFF, 0x88, 0x17, 0x43, 0x4, 0x0, 0xED};

OneWire onewire(ONEWIRE_PIN);
DS18B20 t_sensor(&onewire);

void setup() {
  while(!Serial);
  Serial.begin(9600);

  t_sensor.begin();
  t_sensor.request(address);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available())
  {
      request = Serial.read();

      switch(request.toInt())
      {
        case 49:
        if(t_sensor.available())
        {
          Serial.print(t_sensor.readTemperature(address));
          t_sensor.request(address);
        }

      }

//      
//      Serial.print("char: ");
//      Serial.println(number,DEC);
  }

}
