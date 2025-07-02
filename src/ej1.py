'''
Claro, aquí tienes un enunciado claro y educativo para ese fragmento de código, ideal para principiantes:
📝 Enunciado: Calculadora de Operaciones Básicas
Crea un programa en Python que realice lo siguiente:
Solicite al usuario que ingrese dos números enteros.
Convierta ambos valores a tipo int.
Calcule las cuatro operaciones básicas entre esos números:
Suma
Resta
Multiplicación
División
Muestre todos los resultados utilizando un mensaje multi-línea ("""texto""") con formato claro y amigable, incluyendo
los números introducidos y los resultados de cada operación.
🧪 Ejemplo de salida esperada:

Ingresa primer número: 8
Ingresa segundo número: 3

Para los números 8 y 3,
El resultado de la suma es 11,
El resultado de la resta es 5,
El resultado de la multiplicación es 24,
El resultado de la división es 2.6666666666666665

'''
n1 = input("Ingreas primer número: ")
n2 = input("Ingresa segundo número: ")
# convertimos los datos que introduce el usuario a int (entero)
n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""
Para los números {n1} y {n2},
El resultado de la suma es {suma},
El resultado de la resta es {resta},
El resultado de la multiplicación es {multiplicacion},
El resultado de la división es {division}
"""

print(mensaje)