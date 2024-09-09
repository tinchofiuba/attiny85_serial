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
  //intento leer algún mensaje desde el maestro
   if (tiny85.available() > 0) 
   {
    String mensaje = tiny85.readStringUntil('\n'); // Leeo el mensaje completo
    int valores[4]; //array para guardar los valores de la cadena 
    int index = 0; //indice que uso para el ciclo
    char* token = strtok(mensaje.c_str(), ",");
    while (token != NULL && index < 4) 
    {
    valores[index] = atoi(token); //guardo el token en el array
    token = strtok(NULL, ",");
    index++;
    }

  delayHigh=1000; //delay de alta en uSegundos
  delayLow=1000;  //delay de baja en uSegundos
  pulso=500; //pulso en miliSegundos
  movimientoMotor();
}
      
 /////////////////////////////////FIN DE LOOP/////////////////////////////////////////
