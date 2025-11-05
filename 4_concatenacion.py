# Solo se pueden concatenar valores del mismo tipo (por ejemplo, string con string, lista con lista).

# Si intentas concatenar tipos diferentes (por ejemplo, número con texto), da error.

# Si necesitas mezclar tipos, debes convertirlos


first_name = 'Guillermo'
second_name ='Vasquez'

print(first_name + ' ' + second_name)

# EJERCICIOS 

# Ejercicio 1
# Une dos palabras en una sola cadena.

a = "Hola"
b = "Python"
print(a + b)

# Ejercicio 2

# Une dos palabras separadas por un espacio.

p1 = "Hola"
p2 = "Mundo"

print(p1 + ' ' + p2)

# Ejercicio 3
# Concatena tres cadenas:

x = "Aprender"
y = "Python"
z = "es divertido"

print(x + ' ' + y + ' ' + z)


# Ejercicio 4

# Concatena texto y número (usa str() para evitar error):

nombre = "Guillermo"
edad = 40

print(nombre + ' ' + str(edad))

# Ejercicio 5

# Concatena una cadena con un salto de línea \n entre ellas.

linea1 = "Primera línea"
linea2 = "Segunda línea"

print(linea1 + '\n' + linea2)

# Ejercicio 6

# Concatena varios strings dentro de un print() sin usar variables nuevas.

print(p1 + ' ' + 'a' + ' ' + 'todos')

# Ejercicio 7

# Concatena listas con el operador +.

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]



print(str(lista1) +  str(lista2)) # por que deben ser el mismo tipo de datos

#  unir las listas verdaderamente

print(lista1 + lista2)

# Ejercicio 8 

# Concatena texto con un carácter especial, por ejemplo "!".

frase = "Buen trabajo"

print( frase+ '!')

# Ejercicio 9

# Concatena una palabra repetida dos veces.

palabra = "Hola"

print(palabra*2)
# tambien funciona pero piden concatenar
print(palabra + palabra)

# Ejercicio 10

# Concatena cadenas usando el operador * para repetir texto.
# (usa concatenación por multiplicación)


palabra = "Py"
print(palabra*3)

































































