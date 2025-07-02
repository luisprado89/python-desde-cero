#Imprime un texto en pantalla (cadena de texto / string)
print("Hola Mundo!!") # tipo: str

#Puedes repetir una cadena usando el operador * (repite 4 veces)
print("Hola Mundo "* 4) # tipo str, repetido en este caso 4 veces

# Comentarios con # no se ejecutan
# Esta línea está comentada y no da error
# print("Esto no se ejecuta")

# Si intentamos ejecutar código incorrecto, obtenemos un error:
# La siguiente línea está comentada porque causaría un error de sintaxis
# print lalala

# para hacer comentarios de mas de una lina a la vez podemos usar ''' ''' y todo lo que este dentro sera comentario no se ejecutara
'''
Error que generaría si se descomenta la línea anterior:
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
'''

# TIPOS DE DATOS BÁSICOS EN PYTHON:

# Cadena de texto (string o str)
mensaje = "Hola, soy un texto"
print(mensaje) # tipo: str

# Número entero (integer)
edad = 35
print("Edad: ",edad) # tipo: int

# Número deciman (float)
altura = 1.75
print("Altura: ",altura) # tipo: float

# Valor lógico (booleano)
mayor_de_edad = True
print("¿Mayor de edad?: ",mayor_de_edad) # tipo: bool

# Tipo None (sin valor)
nada = None
print("Valor de nada: ",nada) # Tipo: NoneType

print("--------------------------------")
# En Python, se puede comprobar el tipo de datos de una variable utilizando la función type().
# La función type() devuelve el tipo de datos de una variable como un objeto de tipo type.

print("Ahora imprimimos también el tipo de dato más el valor ")
print("mensaje:",mensaje,"-> tipo:",type(mensaje)) # mensaje: Hola, soy un texto -> tipo: <class 'str'>
print("edad:",edad,"-> tipo:",type(edad)) # edad: 35 -> tipo: <class 'int'>
print("altura:",altura,"-> tipo:",type(altura)) # altura: 1.75 -> tipo: <class 'float'>
print("mayor_de_edad:",mayor_de_edad,"-> tipo:",type(mayor_de_edad)) # mayor_de_edad: True -> tipo: <class 'bool'>
print("nada:",nada,"-> tipo:",type(nada)) # nada: None -> tipo: <class 'NoneType'>
