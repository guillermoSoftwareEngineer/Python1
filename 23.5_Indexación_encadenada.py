# Indexación encadenada (listas + strings)

# EJERCICIO IE-1
texto = "Juan,Perez,34,Bogota"
# Separa usando ",".
# Obtén SOLO "Juan".
# Guarda el resultado en una variable llamada nombre.
nombre = texto.split(",")[0] 
print(nombre)


# EJERCICIO IE-2
texto = "ERROR|WARNING|INFO"
# Convierte a minúsculas.
# Separa usando "|".
# Obtén SOLO "warning".
# Guarda el resultado en una variable llamada nivel.
nivel = texto.lower().split("|")[1]
print(nivel)



# EJERCICIO IE-3
texto = "Python,Java,Go,Rust"
# Separa usando ",".
# Obtén SOLO "Go".
# Guarda el resultado en una variable llamada lenguaje.
lenguaje = texto.split(",")[2]
print(lenguaje)


# EJERCICIO IE-4
texto = "uno-dos-tres-cuatro"
# Separa usando "-".
# Obtén SOLO "cuatro".
# Guarda el resultado en una variable llamada resultado.
resultado =texto.split("-")[-1]
print(resultado)



# EJERCICIO IE-5
texto = "2026/01/11/logs/system/error"
# Separa usando "/".
# Obtén SOLO "logs".
# Guarda el resultado en una variable llamada carpeta.
carpeta = texto.split("/")[3]
print(carpeta)


# EJERCICIO IE-6
texto = "rojo|verde|azul|amarillo"
# Convierte a minúsculas.
# Separa usando "|".
# Obtén SOLO "rojo".
# Guarda el resultado en una variable llamada color.
color = texto.lower().split("|")[0]
print(color)

# EJERCICIO IE-7
texto = "A,B,C,D,E"
# Separa usando ",".
# Obtén SOLO "C".
# Guarda el resultado en una variable llamada letra.
letra = texto.split(",")[2]
print(letra)

# EJERCICIO IE-8
texto = "manzana pera banana uva"
# Separa usando el espacio.
# Obtén SOLO "uva".
# Guarda el resultado en una variable llamada fruta.
fruta = texto.split(" ")[-1]
print(fruta)

# EJERCICIO IE-9
texto = "nombre:Juan|edad:34|ciudad:Bogota"
# Separa usando "|".
# Obtén SOLO "edad:34".
# Guarda el resultado en una variable llamada dato.
dato = texto.split("|") [1]
print(dato)

# EJERCICIO IE-10
# Explica con palabras (sin código):
# qué significa exactamente “indexación encadenada”
# y por qué sigue siendo una sola expresión.
# por que es posible lograr con python hacer chaining (encadenamiento) de un metodo y una indexacion
# es usar operaciones seguidas, que usan el resultado inmediatamente anterior
