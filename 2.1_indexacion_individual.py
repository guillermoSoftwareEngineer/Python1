# Tema: indexación individual 

# Indexar es obtener un solo elemento de una lista usando su posición.
# Devuelve un valor, no una lista
# No modifica la lista
# Es lectura directa

# BLOQUE DE EJERCICIOS — indexación individual (listas)

# EJERCICIO E-1
texto = "Juan,Perez,34,Bogota"
# Separa el texto usando ",".
# Luego obtén SOLO el nombre (primer elemento).
# Guarda el resultado en una variable llamada nombre.

nombre = texto.split(",")[0]
print(nombre)

# EJERCICIO E-2
texto = "ERROR|WARNING|INFO"
# Convierte el texto a minúsculas.
# Separa usando "|".
# Luego obtén SOLO el último elemento.
# Guarda el resultado en una variable llamada nivel.
nivel = texto.lower().split("|")[-1]
print(nivel)

# EJERCICIO E-3
texto = "Python,Java,Go,Rust"
# Separa usando ",".
# Luego obtén SOLO el segundo elemento.
# Guarda el resultado en una variable llamada lenguaje.
lenguaje = texto.split(",")[1]
print(lenguaje)


# EJERCICIO E-4
texto = "uno-dos-tres-cuatro"
# Separa usando "-".
# Luego obtén SOLO "tres" usando posición.
# Guarda el resultado en una variable llamada resultado.
resultado = texto.split("-")[2]
print(resultado)

# EJERCICIO E-5
texto = "2026/01/11/logs/system/error"
# Separa usando "/".
# Luego obtén SOLO "system".
# Guarda el resultado en una variable llamada carpeta.
carpeta = texto.split("/")[-2] 
print(carpeta)

# EJERCICIO E-6
texto = "rojo|verde|azul|amarillo"
# Convierte a minúsculas.
# Separa usando "|".
# Luego obtén SOLO el primer elemento.
# Guarda el resultado en una variable llamada color.
color = texto.lower().split("|")[0]
print(color)

# EJERCICIO E-7
texto = "A,B,C,D,E"
# Separa usando ",".
# Luego obtén SOLO el elemento central ("C").
# Guarda el resultado en una variable llamada letra.
letra =texto.split(",")[2]
print(letra)

# EJERCICIO E-8
texto = "manzana pera banana uva"
# Separa usando el espacio.
# Luego obtén SOLO el último elemento.
# Guarda el resultado en una variable llamada fruta.
fruta = texto.split(" ")[-1]
print(fruta)

# EJERCICIO E-9
texto = "nombre:Juan|edad:34|ciudad:Bogota"
# Separa usando "|".
# Luego obtén SOLO el segundo elemento completo.
# Guarda el resultado en una variable llamada dato.
dato = texto.split("|")[1]
print(dato)

# EJERCICIO E-10
# Explica con palabras (sin código):
# por qué indexación devuelve un valor
# y slicing devuelve una lista.
# por que index se refiere a una posicion dentro de la lista, en cambio slicingtrae una seccion de esa lista que 
# puede contener un solo indice o un conjunto de indices continuo

