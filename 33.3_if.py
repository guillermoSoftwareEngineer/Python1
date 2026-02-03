# Qué es if

# if es una estructura de control condicional.
# Sirve para:

# Ejecutar un bloque de código SOLO si se cumple una condición.

# Sintaxis mínima explicada
# if condicion:
#     accion

# Explicacion:

# if → palabra reservada
# condicion → una expresión que se evalúa como:
# True (verdadero)
# False (falso)
# : → inicia el bloque
# indentación → lo que se ejecuta solo si la condición es verdadera

# Ejemplo 

edad = 20

if edad >= 18:
    print("Es mayor de edad")

# El orden correcto es:

# for → recorrer
# if → decidir
# for + if → procesar datos reales

# BLOQUE DE EJERCICIOS — for + if (FILTRADO)

# BLOQUE DE EJERCICIOS — H
# Tema: for + if (primer contacto CONTROLADO)
#
# REGLAS OBLIGATORIAS:
# - Usa SOLO: split(), strip(), lower(), upper(), replace(), for, if, print
# - NO usar: len(), range(), slicing, indexación, métodos de listas, join
# - NO crear listas nuevas
# - NO modificar la lista original
# - El if SOLO decide si se imprime o no
# - Trabaja SIEMPRE sobre el texto ORIGINAL salvo que el enunciado diga lo contrario


# EJERCICIO H-1
texto = "Python,Java,Go,Rust"
# Recorre los lenguajes separados por coma.
# Imprime ÚNICAMENTE los lenguajes que,
# en el texto original, NO estén completamente en minúsculas.

for lenguages in texto.split(","):
    if lenguages != lenguages.lower():
        print(lenguages)


print("------------------------------------") # lo uso para ver en la ejecucion donde empieza el resultado del siguiente ejercicio


# EJERCICIO H-2
texto = "python,Java,go,Rust"
# Recorre los lenguajes separados por coma.
# Imprime ÚNICAMENTE los lenguajes que
# estén completamente en minúsculas en el texto original.
for lenguaje in texto.split(","):
    if lenguaje == lenguaje.lower():
        print(lenguaje)

print("------------------------------------") # lo uso para ver en la ejecucion donde empieza el resultado del siguiente ejercicio

# EJERCICIO H-3
texto = "ERROR|WARNING|INFO"
# Convierte el texto a minúsculas.
# Recorre los niveles.
# Imprime SOLO el nivel cuyo valor sea exactamente "warning".
for nivel in texto.lower().split("|"):
    if nivel == "warning":
        print(nivel)

print("------------------------------------") # lo uso para ver en la ejecucion donde empieza el resultado del siguiente ejercicio


# EJERCICIO H-4
texto = "uno dos tres cuatro"
# Separa por espacio.
# Recorre las palabras.
# Imprime SOLO las palabras que NO estén en mayúsculas
# (evalúa la palabra tal como sale del split).
for  numero in texto.split(" "):
    if numero != numero.upper():
        print(numero)

print("------------------------------------") # lo uso para ver en la ejecucion donde empieza el resultado del siguiente ejercicio



# EJERCICIO H-5
texto = "Rojo|verde|Azul|AMARILLO"
# Separa usando "|".
# Recorre los colores.
# Imprime SOLO los colores que estén completamente en mayúsculas.

for color in texto.split("|"):
    if color == color.upper():
        print(color)

print("------------------------------------") # lo uso para ver en la ejecucion donde empieza el resultado del siguiente ejercicio



# EJERCICIO H-6
texto = "Python  es  Potente"
# Reemplaza los dobles espacios por uno.
# Separa por espacio.
# Recorre las palabras.
# Imprime SOLO las palabras que comiencen con mayúscula
# (evalúa la palabra original, no la transformes para decidir).
for palabra in texto.replace("  "," ").split(" "):
    if palabra[0] == palabra[0].upper():
        print(palabra)

print("------------------------------------") # lo uso para ver en la ejecucion donde empieza el resultado del siguiente ejercicio



# EJERCICIO H-7
texto = "juan,PEDRO,Ana,maria"
# Separa usando ",".
# Recorre los nombres.
# Imprime SOLO los nombres que NO estén completamente en mayúsculas
# ni completamente en minúsculas.
for name in texto.split(","):
    if name != name.upper() and name != name.lower():
        print(name)

print("------------------------------------") # lo uso para ver en la ejecucion donde empieza el resultado del siguiente ejercicio


# EJERCICIO H-8
texto = "INFO|debug|Warning|ERROR"
# Separa usando "|".
# Recorre los niveles.
# Imprime SOLO los niveles que NO estén completamente en mayúsculas.
for level in texto.split("|"):
    if level != level.upper():
        print(level)


print("------------------------------------") # lo uso para ver en la ejecucion donde empieza el resultado del siguiente ejercicio

# EJERCICIO H-9
texto = "uno DOS tres CUATRO"
# Separa usando espacio.
# Recorre las palabras.
# Imprime SOLO las palabras que estén completamente en mayúsculas.
for word in texto.split(" "):
    if word == word.upper():
        print(word)


print("------------------------------------") # lo uso para ver en la ejecucion donde empieza el resultado del siguiente ejercicio


# EJERCICIO H-10
# Explica con palabras (sin código):
# por qué en este bloque el for recorre TODOS los elementos,
# pero el if decide cuáles se imprimen y cuáles no.

# el for asigna un alias a cada elemento y va revisandolos recorriendolos 1 x 1, no decide ni ejecuta solo recorre, 
# en cambio el if con base en una condicion
# la evalua y si es cierta ejecuta una accion, la conbinacion de los dos es bastante util

print("------------------------------------") # lo uso para ver en la ejecucion donde empieza el resultado del siguiente ejercicio