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
#todo lo que esta abajo lo repito indefinidamente

while True:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    # Esperar un momento para asegurarse de que la conexión esté establecida
    time.sleep(2)

    # Enviar un mensaje al Arduino
    ser.write(b'Hello ')
    time.sleep(5)
    ser.write(b'Hello Arduino')
    if ser.in_waiting > 0:
        try:
            response = ser.readline().decode('utf-8').strip()
            print("okokok")
        except UnicodeDecodeError:
            response = ser.readline().decode('latin-1').strip()
            print("hay algo raro")
        print(f"Respuesta del Arduino: {response}")
    # Cerrar el puerto serial
ser.close()