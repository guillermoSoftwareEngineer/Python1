# 1. Métodos upper() y lower()

# upper retorna los caracteres en mayuscula
# upper retorna los caracteres en minuscula

# Ejercicio 1:
# Dado el string "python", usa el método upper() para convertirlo a mayúsculas.

cadena = 'python'
print(cadena.upper())


# Ejercicio 2:
# Dado el string "PYTHON", usa el método lower() para convertirlo a minúsculas.

string2 = 'PYTHON'
print(string2.lower())

# Ejercicio 3:
# Asigna a una variable el valor "PyThOn" y muestra el resultado de aplicar upper() y lower() 
# en dos líneas separadas.

string3 = 'PyThOn'
print(string3.upper)
print(string3.lower) 

# Por que  retorna ?
# <built-in method upper of str object at 0x000002878D02BA20>
# <built-in method lower of str object at 0x000002878D02BA20>

# Ejercicio 4:
# Guarda en una variable el texto "Hola Mundo" y muestra el texto en mayúsculas.

saludo = 'Hola Mundo'
print(saludo.upper())

# Ejercicio 5:
# Guarda en una variable el texto "Hola Mundo" y muestra el texto en minúsculas.


saludo2 = 'Hola Mundo'
print(saludo2.lower())

# Ejercicio 6:
# Usa una variable para almacenar tu nombre en minúsculas y muestra tu nombre en mayúsculas.

nombre = 'guillermo'
print(nombre.upper())

# Ejercicio 7:
# Crea una variable con el texto "Aprender Python" y muestra primero el texto en mayúsculas y 
# luego en minúsculas.

aprender ='Aprender Python'
print(aprender.upper())
print(aprender.lower())

# Ejercicio 8:
# Asigna a una variable el valor "Bienvenido" y muestra el resultado de upper() 
# seguido de un espacio y luego el resultado de lower().

valor = 'Bienvenido'
valor_may = valor.upper()
valor_min = valor.lower()

print(valor_may + ' ' + valor_min)

# Ejercicio 9:
# Define una variable con el valor "PrAcTiCa" y muestra la comparación de si
#  el texto es igual a su versión en mayúsculas.

var1 = 'PrAcTiCa'
var2 = var1.upper()

print( var1 == var2 )

# Ejercicio 10:
# Define una variable con el valor "Ejercicio" y verifica si al aplicar lower() el resultado
# es igual al texto original (recuerda que debe coincidir carácter por carácter).

varejer = 'Ejercicio'
varejer_low = varejer.lower()

print(varejer == varejer_low)