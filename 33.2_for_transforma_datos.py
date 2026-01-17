# BLOQUE DE EJERCICIOS — for + transformación
# Reglas:
# - Usa solo: split(), strip(), lower()/upper(), replace(), for, print
# - NO usar: if, range, len, slicing, indexación, métodos de listas
# - NO crear listas nuevas
# - No modificar la lista original
# - Transformar solo el elemento dentro del for


# EJERCICIO G-1
texto = "Python,Java,Go"
# Separa usando ",".
# Recorre la lista e imprime cada lenguaje en MAYÚSCULAS.
for lenguaje in texto.split(","):
    print(lenguaje.upper())


# EJERCICIO G-2
texto = "ERROR|WARNING|INFO"
# Convierte el texto a minúsculas.
# Separa usando "|".
# Recorre la lista e imprime cada nivel en mayúsculas.
for levels in texto.lower().split("|"):
    print(levels.upper())


# EJERCICIO G-3
texto = "  manzana pera banana  "
# Limpia espacios.
# Separa usando el espacio.
# Recorre la lista e imprime cada fruta en MAYÚSCULAS.
for fruits in texto.strip().split(" "):
    print(fruits.upper())


# EJERCICIO G-4
texto = "uno-dos-tres-cuatro"
# Separa usando "-".
# Recorre la lista e imprime cada elemento en minúsculas.
for number in texto.split("-"):
    print(number.lower())


# EJERCICIO G-5
texto = "Juan,Perez,34,Bogota"
# Separa usando ",".
# Recorre la lista e imprime cada dato sin espacios sobrantes.
for data in texto.split(","):
    print(data.strip())


# EJERCICIO G-6
texto = "rojo|verde|azul"
# Convierte a minúsculas.
# Separa usando "|".
# Recorre la lista e imprime cada color en MAYÚSCULAS.
for color in texto.lower().split("|"):
    print(color.upper())


# EJERCICIO G-7
texto = "Python  es  potente"
# Reemplaza dobles espacios por uno.
# Separa usando el espacio.
# Recorre la lista e imprime cada palabra en minúsculas.
for word in texto.replace("  "," ").split(" "):
    print(word.lower())


# EJERCICIO G-8
texto = "A,B,C,D"
# Separa usando ",".
# Recorre la lista e imprime cada letra en minúsculas.
for letter in texto.split(","):
    print(letter.lower())

# EJERCICIO G-9
texto = "2026/01/11/logs/system"
# Separa usando "/".
# Recorre la lista e imprime cada parte en MAYÚSCULAS.
for datos in texto.split("/"):
    print(datos.upper())

# EJERCICIO G-10
# Explica con palabras (sin código):
# por qué transformar el elemento dentro del for
# NO cambia la lista original.
# ya que el for usa una variable temporal que contiene el valor de la lista original en cada iteracion
# sin modificar la lista original
