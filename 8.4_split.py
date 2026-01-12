# split()

# split() cambia el paradigma:

# Pasamos de texto continuo → a unidades semánticas (palabras / tokens)
# Esto no es “otro método más”.
# Es el puente entre strings y estructuras de datos reales.

# Los problemas que NO se pueden resolver bien con replace():
# Múltiples espacios inconsistentes
# Conteo fiable de palabras
# Limpieza robusta
# Normalización real de texto humano

#si en un string hay division de espacios varias es decir entre palabras puede haber uno, dos y tres espacios
# en el mismo string, replace no lo normalizaria adecuadamente, encambio split si lo hace()

# split() NO modifica el texto, crea una lista
# Por defecto:
# separa por cualquier cantidad de espacios
# El resultado siempre es una lista
# Primero se limpia, luego se analiza

texto = " hola   hola    hola"
print(len(texto.replace("  ", " ")))
print(len(texto.split(" ")))
print(texto.split())

# DÍA 7 — split()
# Objetivo: convertir texto real en estructuras analizables
# Regla: SOLO usar métodos ya vistos + split()

# Ejercicio 1
texto = "hola mundo"
# Separa el texto en palabras
print(texto.split())


# Ejercicio 2
texto = "hola   mundo   python"
# Separa el texto correctamente a pesar de los espacios múltiples
print(texto.split())


# Ejercicio 3
texto = "Hola   Hola    HOLA"
# Convierte a minúsculas
# Separa en palabras
# Cuenta cuántas veces aparece "hola"
print(texto.lower().split().count("hola"))


# Ejercicio 4
texto = "   aprender python es clave   "
# Limpia los bordes
# Separa en palabras
# Imprime la lista resultante
print(texto.strip().split())


# Ejercicio 5
texto = "python es poderoso"
# Separa el texto
# Imprime cuántas palabras hay
print(len(texto.split()))


# Ejercicio 6
texto = "error   error    error"
# Separa el texto
# Cuenta cuántas veces aparece "error"
print(texto.split().count("error"))


# Ejercicio 7
texto = "   hola   hola   hola   "
# Limpia los bordes
# Normaliza a minúsculas
# Separa en palabras
print(texto.strip().lower().split())


# Ejercicio 8
texto = "python,java,python,c++"
# Separa usando la coma como separador
print(texto.split(","))


# Ejercicio 9
texto = "uno dos tres cuatro"
# Separa el texto
# Imprime el primer elemento de la lista
print(texto.split()[0])


# Ejercicio 10 (clave)
texto = "   hola   hola   hola   "
# Limpia
# Normaliza
# Separa
# Reconstruye el texto EXACTAMENTE como:
# "hola hola hola"
print(" ".join(texto.strip().lower().split()))

