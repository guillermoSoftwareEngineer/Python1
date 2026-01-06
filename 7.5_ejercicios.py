# DÍA 4 — COMBINACIÓN DE MÉTODOS DE STRING
# Regla: usa SOLO métodos ya estudiados

# Ejercicio 1
texto = "Python es Poderoso"
# Convierte todo a minúsculas y cuenta cuántas veces aparece la letra "o"
print(texto.lower().count("o"))


# Ejercicio 2
texto = "APRENDER python ES CLAVE"
# Convierte todo a minúsculas
# Luego cuenta cuántas veces aparece la palabra "python"
print(texto.lower().count("python"))


# Ejercicio 3
texto = "banana BANANA banana"
# Convierte todo a minúsculas
# Cuenta cuántas veces aparece "banana"
print(texto.lower().count("banana"))


# Ejercicio 4
texto = "Programar en Python es programar"
# Convierte todo a minúsculas
# Cuenta cuántas veces aparece "programar"
print(texto.lower().count("programar"))


# Ejercicio 5
texto = "PythonPythonPYTHON"
# Convierte todo a minúsculas
# Cuenta cuántas veces aparece "python"
print(texto.lower().count("python"))


# Ejercicio 6
texto = "Aprender Python es aprender a pensar"
# Convierte todo a minúsculas
# Usa find() para encontrar el índice de "python"
print(texto.lower().find("python"))

# Ejercicio 7
texto = "ERROR error Error"
# Convierte todo a minúsculas
# Cuenta cuántas veces aparece "error"
print(texto.lower().count("error"))

# Ejercicio 8
texto = "HolaHolaHOLA"
# Convierte todo a minúsculas
# Cuenta cuántas veces aparece "hola"
print(texto.lower().count("hola"))


# Ejercicio 9
texto = "Mi lenguaje favorito es PYTHON"
# Convierte todo a minúsculas
# Usa len() para imprimir la longitud del texto resultante
print(len(texto.lower()))


# Ejercicio 10
texto = "Python es poderoso"
# Convierte todo a MAYÚSCULAS
# Cuenta cuántas veces aparece la letra "O"
print(texto.upper().count("O"))
