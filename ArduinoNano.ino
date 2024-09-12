//si recibo un mensaje por serial (9600 baud) prendo el led de blink. Pero en este caso uso un arduiono nano
#include <SoftwareSerial.h>

void loop() {
  //si recibo un mensaje por serial (9600 baud) prendo el led de blink
  if(tiny85.available()>0)
  {
    int velocidad=tiny85.read();
    tiny85.write(velocidad);
    if(velocidad==1200)
    {
      digitalWrite(13,HIGH);
    }
    else:
    {
      digitalWrite(13,LOW);
      digitalWrite(13,HIGH);
      delay(1000);
      digitalWrite(13,LOW);
    }
  }
  delay(1000);
}