# Metodo count()

# Una sola idea, clara y suficiente:

# count() cuenta cuántas veces aparece un carácter o subcadena dentro de un string.

# Devuelve un número
# No devuelve índices
# No modifica el texto
# Si no aparece Devuelve devuelve 0

# ¿count() diferencia mayúsculas de minúsculas?
#Sí. count() es sensible a mayúsculas y minúsculas (case-sensitive).

"banana".count("a") #Devuelve 3
print("banana".count("a"))
"banana".count("na") #Devuelve 2
print("banana".count("na"))
"banana".count("z") #Devuelve 0
print("banana".count("z"))

# EJERCICIOS DE count() 

# Ejercicio 1
texto = "banana"
# Cuenta cuántas veces aparece exactamente la letra "a"
print(texto.count("a")) 

# Ejercicio 2
texto = "banana"
# Cuenta cuántas veces aparece exactamente la letra "n"
print(texto.count("n"))  

# Ejercicio 3
texto = "banana"
# Cuenta cuántas veces aparece exactamente la subcadena "na"
# Nota: count NO cuenta coincidencias solapadas
print(texto.count("na")) 

# Ejercicio 4
frase = "Python es poderoso"
# Cuenta cuántas veces aparece exactamente la letra "o" (minúscula)
# No contar "O" mayúscula porque no existe en el texto
print(frase.count("o"))  

# Ejercicio 5
frase = "Python es poderoso"
# Cuenta cuántas veces aparece exactamente la palabra "Python"
# Debe coincidir en mayúsculas y minúsculas
print(frase.count("Python")) 

# Ejercicio 6
palabra = "elefante"
# Cuenta cuántas veces aparece exactamente la letra "e"
print(palabra.count("e"))  

# Ejercicio 7
palabra = "elefante"
# Cuenta cuántas veces aparece exactamente la letra "z"
# La letra no existe en el texto
print(palabra.count("z"))  

# Ejercicio 8
texto = "Slicing y count"
# Cuenta cuántos espacios (" ") hay en el texto
print(texto.count(" "))  

# Ejercicio 9
texto = "programación"
# Cuenta cuántas veces aparece exactamente la letra "o"
# La "ó" NO es igual a "o"
print(texto.count("o")) 

# Ejercicio 10
texto = "aaaaa"
# Cuenta cuántas veces aparece exactamente la letra "a"
print(texto.count("a"))  

