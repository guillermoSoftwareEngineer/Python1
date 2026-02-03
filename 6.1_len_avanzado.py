# Qué es len()
# len() devuelve la cantidad de elementos de una colección (por ahora: listas y strings).
# No modifica nada
# No recorre explícitamente
# No devuelve los elementos, solo el tamaño

# Ejemplos conceptuales (sin código):

# Una lista con 5 elementos → len devuelve 5
# Un string con 10 caracteres → len devuelve 10

# Idea clave:
# len() responde a la pregunta “¿cuántos hay?”, no “¿cuáles son?”

# NUNCA ASUMAS EL TAMAÑO DE UN DATO QUE NO CONTROLAS. 



# BLOQUE ÚNICO DE EJERCICIOS — Nivel I
# Tema: len() + for (sin if todavía)

# REGLAS OBLIGATORIAS
# Usa SOLO: split(), strip(), len(), for, print
#  NO usar: if, range, slicing, indexación, métodos de listas
#  NO crear listas nuevas
#  NO modificar la lista
# SOLO observar y reportar

# EJERCICIO I-1
texto = "Python,Java,Go"
# Separa por coma.
# Imprime cuántos lenguajes hay.
print(len(texto.split(",")))


# EJERCICIO I-2
texto = "uno dos tres cuatro"
# Separa por espacio.
# Imprime cuántas palabras hay.
print(len(texto.split(" ")))


# EJERCICIO I-3
texto = "ERROR|WARNING|INFO|DEBUG"
# Separa usando "|".
# Imprime la cantidad de niveles.
print(len(texto.split("|")))


# EJERCICIO I-4
texto = "  manzana pera banana uva  "
# Limpia espacios.
# Separa por espacio.
# Imprime cuántas frutas hay.
print(len(texto.strip().split(" ")))


# EJERCICIO I-5
texto = "2026/01/11/logs/system/error"
# Separa usando "/".
# Imprime cuántas partes tiene la ruta.
print(len(texto.split("/")))


# EJERCICIO I-6
texto = "A,B,C,D,E,F"
# Separa por coma.
# Imprime cuántas letras hay.
print(len(texto.split(",")))


# EJERCICIO I-7
texto = "rojo|verde|azul"
# Separa por "|".
# Imprime el total de colores.
print(len(texto.split("|")))

# EJERCICIO I-8
texto = "Python es potente"
# Separa por espacio.
# Imprime cuántas palabras hay.
print(len(texto.split(" ")))

# EJERCICIO I-9
texto = "uno"
# Separa por espacio.
# Imprime cuántos elementos hay.
print(len(texto.split(" ")))

# EJERCICIO I-10 (conceptual, sin código)
# Explica con palabras:
# por qué len() NO reemplaza al for
# y por qué el for NO reemplaza a len().

# len solo cuenta no dice que hay dentro exactamente, solo dice cuantos de ellos hay, en cambio 
# for sabe que hay dentro de cada uno sabe que hay dentro