# DÍA 6 — MICRO-CONSOLIDACIÓN
# Objetivo: limpieza y análisis de texto real

# Ejercicio 1
texto = "   PYTHON es Poderoso   "
# Limpia los bordes
# Convierte todo a minúsculas
# Cuenta cuántas veces aparece la letra "o"
print(texto.strip().lower().count("o"))


# Ejercicio 2
texto = "ERROR error Error   "
# Limpia los bordes
# Convierte a minúsculas
# Reemplaza "error" por "fallo"
# Cuenta cuántas veces aparece "fallo"
print(texto.strip().lower().replace("error","fallo").count("fallo"))


# Ejercicio 3
texto = "   hola   mundo   "
# Limpia los bordes
# Reemplaza los espacios internos por un guion "-"
# Imprime el resultado
print(texto.strip().replace(" ","-"))


# Ejercicio 4
texto = "Aprender Python es aprender a pensar"
# Convierte todo a minúsculas
# Usa find() para encontrar el índice de "python"
print(texto.lower().find("python"))


# Ejercicio 5
texto = "banana BANANA banana"
# Convierte todo a minúsculas
# Cuenta cuántas veces aparece "banana"
print(texto.lower().count("banana"))


# Ejercicio 6
texto = "   python,java,python,c++   "
# Limpia los bordes
# Reemplaza las comas por espacios
# Cuenta cuántas veces aparece "python"
print(texto.strip().replace(","," ").count("python"))


# Ejercicio 7
texto = "Hola   Hola   HOLA"
# Convierte todo a minúsculas
# Reemplaza los espacios dobles por un solo espacio
# Cuenta cuántas veces aparece "hola"
print(texto.lower().replace("  "," ").count("hola"))


# Ejercicio 8
texto = "   Programar en Python es programar   "
# Limpia los bordes
# Convierte a minúsculas
# Cuenta cuántas veces aparece "programar"
print(texto.strip().lower().count("programar")) 


# Ejercicio 9
texto = "2024-05-10"
# Reemplaza "-" por "/"
# Usa len() para mostrar la longitud final
print(len(texto.replace("-","/")))

# Ejercicio 10 (clave)
texto = "   hola   hola   hola   "
# Limpia los bordes
# Normaliza a minúsculas
# Haz que quede exactamente:
# "hola hola hola"
# Imprime el resultado
print(texto.strip().lower().replace("  "," "))
