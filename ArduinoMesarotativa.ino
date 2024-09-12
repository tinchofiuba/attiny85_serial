#include <SoftwareSerial.h>
SoftwareSerial tiny85(0,2); //serial p0=RX, p2=TX

#define enable 3 //motor habilitado==LOW, inHabilitado==HIGH , de por si este pin tiene una pullDown en el driver!
#define pasos 4 //pin para controlar la velocidad de giro del motor, no bajar de 800us, empieza a vibrar
#define selecDir 1 //pin para seleccionar la dirección

int velocidad,delayHigh,delayLow,pulso;

void movimientoMotor()
{ 
digitalWrite(pasos,HIGH);
delayMicroseconds(delayHigh);
digitalWrite(pasos,LOW);
delayMicroseconds(delayLow);   
delay(pulso);
  }



void setup() {
  pinMode(0,OUTPUT);
  pinMode(2,OUTPUT);
  tiny85.begin(9600);
  pinMode(enable,OUTPUT);
  digitalWrite(enable,LOW);
  pinMode(pasos,OUTPUT);  
  pinMode(selecDir,OUTPUT);
  digitalWrite(selecDir,LOW);
}

void loop() {
//si recibo un mensaje por serial (9600 baud) apago el motor (enable==HIGH)
  if(tiny85.available()>0)
  {
  //leo el mensaje y lo guardo en la variable velocidad
    int velocidad=tiny85.read();
    //escribo por el serial para que lo pueda leer desde la pc, recibiendolo pyhton
    tiny85.write(velocidad);
    //si velocidad es igual a 1200, apago el motor
    if(velocidad==1200)
    {
      digitalWrite(enable,HIGH);
    }
    else:
    {
      digitalWrite(enable,LOW);
      digitalWrite(enable,HIGH);
      delay(1000);
      digitalWrite(enable,LOW);
    }

  }

  delayHigh=1000; //delay de alta en uSegundos
  delayLow=1000;  //delay de baja en uSegundos
  pulso=0; //pulso en miliSegundos
  movimientoMotor();
}
      
 /////////////////////////////////FIN DE LOOP/////////////////////////////////////////
