'''
import serial

# Inicializar el objeto 'ser' con los parámetros adecuados
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
except serial.SerialException as e:
    print(f"Error al inicializar el puerto serial: {e}")
    ser = None

while True:
    entrada = input("Ingrese los valores separados por comas: ")
    entrada = entrada.split(",")
    if len(entrada) != 4:
        print("Error en la cantidad de argumentos")
        continue
    else:
        # Si cada argumento es un número entero, entonces se envía el mensaje
        try:
            x = int(entrada[0])
            y = int(entrada[1])
            V1 = int(entrada[2])
            V2 = int(entrada[3])
            mje = f"({x},{y},{V1},{V2})"
            ser.write(mje.encode())
        except ValueError:
            print("Error en los argumentos")
            continue
        except serial.SerialException as e:
            print(f"Error al escribir en el puerto serial: {e}")
            continue
        
    if ser and ser.in_waiting > 0:
        try:
            print(ser.readline().decode())
        except Exception as e:
            print(f"Error al leer desde el puerto serial: {e}")
    else:
        print("No hay respuesta")
        continue

# No cerrar el puerto serial dentro del bucle
# ser.close() debería llamarse fuera del bucle si es necesario
'''

import serial
import time

def main():
    # Configurar el puerto serial (reemplaza '/dev/ttyUSB0' con el puerto correcto)
    ser = serial.Serial('/dev/ttyS4', 9600, timeout=0.5)

    # Esperar un momento para asegurarse de que la conexión esté establecida
    time.sleep(0.3)
    print("INGRESAR ORDENES PARA EL MOTOR:")
    print("-------------------------------")
    print("PRIMERO SE ENVIA EL DELAY DE ENERGIZACION DEL MOTOR, LUEGO LA DIRECCION DE GIRO Y FINALMENTE EL ESTADO--->"+"1000,1,1")
    print("--LA VELOCIDAD DEBE AUMENTA AL DISMINUIR EL VALOR DEL DELAY (MAYOR A 800 SIEMPRE)")
    print("--GIRA EN SENTIDO HORARIO SI EL VALOR ES 1 Y ANTIHORARIO SI ES 0")
    print("--EL ESTADO DEBE SER 1 PARA ENCENDER EL MOTOR Y 0 PARA APAGARLO")
    while True:
        # Pedir al usuario que ingrese un array
        array_to_send = input("Ingresar array de ordenes (para enviar al Arduino (por ejemplo, '1000,1000,0,1') o 'exit' para salir: ")
        if array_to_send.lower() == 'exit':
            break

        # Enviar el array al Arduino
        ser.write(array_to_send.encode())
        time.sleep(1)  # Esperar un segundo antes de leer la respuesta

        # Leer la respuesta del Arduino
        if ser.in_waiting > 0:
            try:
                response = ser.readline().decode('utf-8').strip()
                print("Se decodifico según utf-8")
            except UnicodeDecodeError:
                response = ser.readline().decode('latin-1').strip()
                print("Se decodifico según latin-1")
            print(f"Respuesta del Arduino: {response}")

        # Esperar un momento antes de enviar el siguiente array
        time.sleep(0.3)

    # Cerrar el puerto serial
    ser.close()

if __name__ == "__main__":
    main()