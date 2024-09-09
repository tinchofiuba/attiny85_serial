import serial
import time

ser=serial.Serial('/dev/ttyUSB0',9600) #o COM X en Windows

time.sleep(2) #espera 2 segundos para darle tiempo al puerto para que se inicie, por las dudas.

while True:
    entrada=input("Ingresar ordenes para el motor: (x,y,V1,V2)")
    entrada.split(",")
    if len(entrada)!=4:
        print("Error en la cantidad de argumentos")
        continue
    else:
        #si cada argumento es un número entero, entonces se envía el mensaje
        try:
            x=int(entrada[0])
            y=int(entrada[1])
            V1=int(entrada[2])
            V2=int(entrada[3])
            mje="("+str(x)+","+str(y)+","+str(V1)+","+str(V2)+")"
            ser.write(mje.encode())
            ser.close()
        except:
            print("Error en los argumentos")
            continue

