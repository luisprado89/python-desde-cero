# Python Basics Cheat Sheet

Una guía completa con términos básicos, palabras reservadas, funciones integradas, operadores, métodos de cadenas, estructuras de control y verificadores/conversores de tipos en Python.

---

## Tabla de contenidos

- [Glosario](#glosario)
- [Palabras reservadas](#palabras-reservadas)
- [Funciones integradas](#funciones-integradas)
- [Operadores](#operadores)
- [Métodos de cadenas (strings)](#métodos-de-cadenas-strings)
- [Estructuras de control](#estructuras-de-control)
- [Verificadores y conversores de tipos](#verificadores-y-conversores-de-tipos)

---

## Glosario

| Término             | Definición                                                                                 |
|---------------------|--------------------------------------------------------------------------------------------|
| **Algoritmo**       | Conjunto de pasos ordenados para resolver un problema o realizar una tarea específica.     |
| **Variable**         | Espacio en memoria que almacena un valor modificable durante la ejecución.                  |
| **Tipo de dato**     | Característica que determina qué valores puede almacenar una variable.                      |
| **Entero**           | Tipo de dato para números enteros (positivos o negativos).                                 |
| **Flotante**         | Tipo de dato para números decimales, con parte fraccionaria.                               |
| **Cadena o String**  | Tipo de dato que almacena texto (letras, números, símbolos).                               |
| **Booleano**         | Tipo de dato con valores de verdad: `True` o `False`.                                     |
| **Operador**         | Símbolo para realizar operaciones entre variables o valores.                              |
| **Condición**        | Estructura para tomar decisiones según expresiones booleanas.                            |
| **Bucle**            | Estructura que repite un bloque de código mientras se cumpla una condición.               |
| **Iteración**        | Cada vuelta o repetición de un bucle.                                                     |
| **Función**          | Bloque reutilizable de código que realiza una tarea específica.                           |
| **Parámetro**        | Valor que recibe una función para trabajar.                                              |
| **Argumento**        | Valor enviado a una función al llamarla.                                                 |
| **Retorno**          | Valor que devuelve una función con `return`.                                            |
| **Comentario**       | Texto para documentar el código, no se ejecuta.                                          |
| **Palabras reservadas** | Palabras con significado especial en Python (no se pueden usar como identificadores).  |
| **Indentación**      | Espacio en blanco al inicio de línea para definir bloques de código en Python.            |
| **Inicializar variable** | Darle un primer valor a una variable, definiendo su tipo dinámicamente.               |

---

## Palabras reservadas básicas en Python

| Palabra   | Descripción                                                            |
|-----------|------------------------------------------------------------------------|
| `if`      | Condicional para tomar decisiones.                                    |
| `else`    | Caso alternativo si el `if` es falso.                                |
| `elif`    | Evalúa múltiples condiciones de forma secuencial.                    |
| `for`     | Recorre una secuencia (listas, rangos).                              |
| `while`   | Repite mientras una condición sea verdadera.                         |
| `and`     | Operador lógico AND.                                                  |
| `or`      | Operador lógico OR.                                                   |
| `not`     | Operador lógico NOT (negación).                                      |
| `in`      | Comprueba pertenencia a una secuencia.                               |
| `is`      | Comprueba identidad (mismo objeto).                                  |
| `match`   | Estructura condicional basada en patrón (Python 3.10+).              |
| `case`    | Casos dentro de `match`.                                             |
| `break`   | Sale inmediatamente de un bucle.                                     |
| `continue`| Salta a la siguiente iteración del bucle.                           |
| `pass`    | No hace nada, sirve como marcador.                                  |

---

## Funciones integradas principales

| Función     | Descripción                                   |
|-------------|-----------------------------------------------|
| `print()`   | Imprime en consola.                           |
| `input()`   | Solicita entrada al usuario (cadena).        |
| `int()`     | Convierte a entero.                           |
| `float()`   | Convierte a decimal.                          |
| `str()`     | Convierte a cadena.                           |
| `len()`     | Longitud de secuencia.                        |
| `range()`   | Genera secuencia de números enteros.         |
| `type()`    | Devuelve tipo de dato de variable.           |
| `help()`    | Muestra documentación de objeto.             |
| `sum()`     | Suma todos los elementos de un iterable.     |
| `max()`     | Devuelve el máximo valor de un iterable.     |
| `min()`     | Devuelve el mínimo valor de un iterable.     |

---

## Operadores

### Aritméticos

| Operador | Descripción          |
|----------|---------------------|
| `+`      | Suma                |
| `-`      | Resta               |
| `*`      | Multiplicación      |
| `/`      | División (decimal)  |
| `%`      | Módulo (resto)      |
| `**`     | Potencia            |
| `//`     | División entera     |

**Ejemplo:**

```python
a, b = 5, 3
print(a + b)   # 8
print(a - b)   # 2
print(a * b)   # 15
print(a / b)   # 1.666...
print(a % b)   # 2
print(a ** b)  # 125
print(a // b)  # 1
```

---

### Comparación

| Operador | Descripción           |
|----------|----------------------|
| `==`     | Igual a              |
| `!=`     | Diferente de         |
| `>`      | Mayor que            |
| `<`      | Menor que            |
| `>=`     | Mayor o igual que    |
| `<=`     | Menor o igual que    |

---

### Lógicos

| Operador | Descripción                              |
|----------|-----------------------------------------|
| `and`    | True si ambas condiciones son verdaderas |
| `or`     | True si al menos una condición es verdadera |
| `not`    | Niega el valor booleano                   |

---

### Asignación

| Operador | Ejemplo | Equivale a       |
|----------|---------|------------------|
| `=`      | `x = 5` | asigna 5 a x     |
| `+=`     | `x += 3`| `x = x + 3`      |
| `-=`     | `x -= 3`| `x = x - 3`      |
| `*=`     | `x *= 3`| `x = x * 3`      |
| `/=`     | `x /= 3`| `x = x / 3`      |
| `%=`     | `x %= 3`| `x = x % 3`      |
| `**=`    | `x **= 3`| `x = x ** 3`    |
| `//=`    | `x //= 3`| `x = x // 3`    |

---

### Identidad

| Operador | Descripción                              |
|----------|-----------------------------------------|
| `is`     | True si ambas variables son el mismo objeto |
| `is not` | True si no son el mismo objeto          |

---

### Pertenencia

| Operador | Descripción                           |
|----------|--------------------------------------|
| `in`     | True si elemento está en secuencia   |
| `not in` | True si elemento no está en secuencia|

---

### Bits

| Operador | Descripción                  |
|----------|-----------------------------|
| `&`      | AND                         |
| `|`      | OR                          |
| `^`      | XOR                         |
| `~`      | NOT                         |
| `<<`     | Desplazamiento a la izquierda|
| `>>`     | Desplazamiento a la derecha  |

---

## Métodos comunes con cadenas (strings)

| Método     | Descripción                              |
|------------|-----------------------------------------|
| `isdigit()`| True si todos los caracteres son dígitos |
| `isalpha()`| True si todos son letras                  |
| `isalnum()`| True si letras o dígitos                  |
| `islower()`| True si todas las letras son minúsculas  |
| `isupper()`| True si todas las letras son mayúsculas  |
| `istitle()`| True si está en formato título            |
| `lower()`  | Convierte a minúsculas                    |
| `upper()`  | Convierte a mayúsculas                    |
| `title()`  | Convierte a formato título                |
| `strip()`  | Elimina espacios al inicio y final       |
| `split()`  | Divide cadena en lista por delimitador   |

---

## Estructuras de control

### Secuencial

```python
x = 5
y = 3
z = x + y
print(z)
```

---

### Condicionales

```python
x = 5
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")
```

---

### Condicional anidado

```python
x = 10
if x > 5:
    print("x es mayor que 5")
    if x == 10:
        print("x es igual a 10")
```

---

### Match-case (Python 3.10+)

```python
x = 5
match x:
    case 1:
        print("x es 1")
    case 2:
        print("x es 2")
    case _:
        print("x no es 1 ni 2")
```

---

### Bucles

#### while

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

#### for

```python
for i in range(1, 6):
    print(i)
```

---

### Sentencias especiales en bucles

- `break`: sale inmediatamente del bucle.
- `continue`: pasa a la siguiente iteración.
- `pass`: no hace nada (usado como marcador).

---

## Verificadores y conversores de tipos

| Función            | Descripción                              |
|--------------------|-----------------------------------------|
| `type(var)`        | Devuelve el tipo de dato de `var`.      |
| `isinstance(var, t)` | Devuelve True si `var` es instancia de tipo `t`. |
| `str()`, `int()`, `float()` | Convierte valores a tipo cadena, entero o decimal. |

---

*Este documento proporciona un resumen completo para comenzar con Python.*  


