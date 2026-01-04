# Metodo Find()

# find() busca una subcadena dentro de otra y devuelve
# el índice donde empieza, o -1 si no existe
# No modifica el texto.
# No lanza error.
# find() siempre devuelve el índice de la primera coincidencia,
# aunque el carácter o subcadena aparezca varias veces.

"Python".find("th")  # Produce 2
print("Python".find("th"))
"Python".find("x")   # Produce -1
print("Python".find("x"))


# EJERCICIOS DE find() 

# Ejercicio 1
texto = "Python es poderoso"
# Busca "Python" y muestra el índice donde empieza
print(texto.find("Python"))

# Ejercicio 2
texto = "Python es poderoso"
# Busca "poder" y muestra el índice
print(texto.find("poder") )

# Ejercicio 3
texto = "Python es poderoso"
# Busca "Java" y muestra el resultado
print(texto.find("Java"))

# Ejercicio 4
palabra = "elefante"
# Busca la letra "e" y muestra el índice
print(palabra.find("e") )

# Ejercicio 5
palabra = "banana"
# Busca la subcadena "na" y muestra el índice
print(palabra.find("na") )

# Ejercicio 6
frase = "aprender python es clave"
# Busca la palabra "python" y muestra el índice
print(frase.find("python"))

# Ejercicio 7
frase = "aprender python es clave"
# Busca la letra "z" y muestra el resultado
print(frase.find("z"))

# Ejercicio 8
texto = "Slicing y find"
# Busca el espacio " " y muestra el índice
print(texto.find(" "))

# Ejercicio 9
texto = "computadora"
# Busca la subcadena "put" y muestra el índice
print(texto.find("put"))

# Ejercicio 10
texto = "programación"
# Busca la letra "ó" y muestra el índice
print(texto.find("ó"))
