# BLOQUE: split() + slicing

# Un string contiene información compuesta
# split() lo transforma en lista
# slicing permite seleccionar un segmento
# El resultado sigue siendo una lista

# split() crea la estructura
# slicing lee una parte de esa estructura

# QUÉ PROBLEMA REAL RESUELVE

# Ejemplos reales (sin código):
# quedarte solo con el nombre y apellido de un registro
# ignorar encabezados o totales
# tomar solo las primeras columnas
# descartar campos irrelevantes

# BLOQUE DE EJERCICIOS — split() + slicing
# Reglas:
# - Usa solo: strip(), lower()/upper(), replace(), split(), slicing
# - NO usar: bucles, condicionales, indexación individual, join, métodos de listas, len()
# - Todos los resultados deben ser LISTAS
# - No optimices de más
# - Código completo en cada ejercicio


# EJERCICIO D-1
texto = "Python,Java,Go,Rust"
# Separa el texto por comas.
# Luego obtén solo los dos primeros elementos.
# Guarda el resultado en una variable llamada resultado.
resultado = texto.split(",")[0:2]
print(resultado)




# EJERCICIO D-2
texto = "uno-dos-tres-cuatro-cinco"
# Separa el texto usando "-".
# Luego obtén los elementos desde "dos" hasta "cuatro".
# Guarda el resultado en una variable llamada resultado.
resultado = texto.split("-")[1:4]
print(resultado) 


# EJERCICIO D-3
texto = "ERROR|WARNING|INFO|DEBUG"
# Convierte el texto a minúsculas.
# Luego separa usando "|".
# Luego obtén todos los elementos excepto el último.
# Guarda el resultado en una variable llamada niveles.
niveles = texto.lower().split("|")[:-1]
print(niveles)

# EJERCICIO D-4
texto = "  manzana pera banana uva  "
# Limpia espacios al inicio y al final.
# Separa usando el espacio " ".
# Luego obtén solo los elementos del medio
# (excluye el primero y el último).
# Guarda el resultado en una variable llamada frutas.
frutas =texto.strip().split(" ")[1:-1]
print(frutas)

# EJERCICIO D-5
texto = "Juan,Perez,34,Bogota,Colombia"
# Separa el texto usando ",".
# Luego obtén solo los tres primeros elementos.
# Guarda el resultado en una variable llamada datos_personales.
datos_personales = texto.split(",")[:3]
print(datos_personales)


# EJERCICIO D-6
texto = "2026/01/11/logs/system/error"
# Separa el texto usando "/".
# Luego obtén solo los dos últimos elementos.
# Guarda el resultado en una variable llamada resultado.
resultado = texto.split("/")[-2:]
print(resultado)


# EJERCICIO D-7
texto = "Python;Data;Engineering;Cloud;SQL"
# Convierte todo el texto a mayúsculas.
# Separa usando ";".
# Luego obtén todos los elementos excepto los dos últimos.
# Guarda el resultado en una variable llamada tecnologias.
tecnologias =texto.upper().split(";")[:-2]
print(tecnologias)


# EJERCICIO D-8
texto = "uno,dos,tres"
# Separa usando ",".
# Luego obtén una lista vacía usando slicing.
# Guarda el resultado en una variable llamada resultado.
resultado = texto.split(",")[0:0]
print(resultado)


# EJERCICIO D-9
texto = "rojo|verde|azul|amarillo"
# Convierte el texto a minúsculas.
# Separa usando "|".
# Luego obtén solo el primer elemento usando slicing.
# Guarda el resultado en una variable llamada resultado.
resultado = texto.lower().split("|")[:1]
print(resultado)


# EJERCICIO D-10
# Explica con palabras (sin código):
# # ¿cuál es la diferencia de responsabilidad entre split() y slicing?
# split divide y retorna una nueva lista, es decir la crea de acuerdo a la division
# slicing lo que hace es tomar elementos de una lista ya creada de acuerdo a sus argumentos sin incluir 
# el ultimo
