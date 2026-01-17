# for
# Qué es for

# for es una estructura de control que sirve para recorrer una colección (por ahora, una lista) 
# elemento por elemento.

# sintaxis mínima explicada

# for variable in lista:
    # accion

# for palabra reservada indica el inicio del ciclo o que se va a hacer una iteracion
# in se lee literalmente como dentro de en este caso es de una lista llamada "lista"

# el simbolo ":" Marca el inicio del bloque del for.
# Todo lo que esté indentado debajo se repite.

# accion con espacio a la izquierda NO es decorativo.
# Python usa la indentación para saber:
# “esto pertenece al for”

texto = "uno,dos,tres"
lista = texto.split(",")

for palabra in lista:
    print(palabra)

# BLOQUE DE EJERCICIOS 

# Reglas:
# - Usa solo: split(), strip(), lower()/upper(), replace(), for, print
# - NO usar: if, range, len, slicing, indexación, métodos de listas
# - NO crear listas nuevas
# - Solo recorrer e imprimir
# - Código completo en cada ejercicio


# EJERCICIO F-1
texto = "Python,Java,Go"
# Separa el texto usando ",".
# Recorre la lista e imprime cada lenguaje.

for lenguaje in texto.split(","):
    print(lenguaje + " ejercicio 1") # agrego la concatenacion para leer bien el ejercicio al ejecutar y probar
    # de aqui en adelante segun cada ejercicio 


# EJERCICIO F-2
texto = "ERROR|WARNING|INFO"
# Convierte el texto a minúsculas.
# Separa usando "|".
# Recorre la lista e imprime cada nivel.
for info in texto.lower().split("|"): 
    print(info + " ejercicio 2")

# EJERCICIO F-3
texto = "  manzana pera banana  "
# Limpia espacios.
# Separa usando el espacio.
# Recorre la lista e imprime cada fruta.
for fruta in texto.strip().split(" "):
    print(fruta + " ejercicio 3")


# EJERCICIO F-4
texto = "uno-dos-tres-cuatro"
# Separa usando "-".
# Recorre la lista e imprime cada elemento.
for elemento in texto.split("-"):
    print(elemento + " ejercicio 4")

# EJERCICIO F-5
texto = "Juan,Perez,34,Bogota"
# Separa usando ",".
# Recorre la lista e imprime cada dato.
for dato in texto.split(","):
    print(dato + " ejercicio 5")

# EJERCICIO F-6
texto = "rojo|verde|azul"
# Convierte a minúsculas.
# Separa usando "|".
# Recorre la lista e imprime cada color.
for color in texto.lower().split("|"):
    print(color + " ejercicio 6")

# EJERCICIO F-7
texto = "Python  es  potente"
# Reemplaza dobles espacios por uno.
# Separa usando el espacio.
# Recorre la lista e imprime cada palabra.
for palabra in texto.replace("  "," ").split(" "):
    print(palabra + " ejercicio 7")


# EJERCICIO F-8
texto = "A,B,C,D"
# Separa usando ",".
# Recorre la lista e imprime cada letra.
for letra in texto.split(","):
    print(letra + " ejercicio 8")


# EJERCICIO F-9
texto = "2026/01/11/logs/system"
# Separa usando "/".
# Recorre la lista e imprime cada parte.
for level in texto.split("/"):
    print(level + " ejercicio 9")


# EJERCICIO F-10
# Explica con palabras (sin código):
# qué contiene la variable del for en cada vuelta.
# en cada vuelta se contiene solo uno de los elementos de la lista 
