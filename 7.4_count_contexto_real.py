
# COUNT() EN CONTEXTO REAL


# Ejercicio 1
texto = "Python python PYTHON"
# Cuenta cuántas veces aparece "python"
# Ajusta el texto para que el resultado sea 3

print(texto.lower().count("python"))

# Ejercicio 2
texto = "   hola hola   HOLA"
# Cuenta cuántas veces aparece "hola"
# Ignora espacios y mayúsculas
print(texto.lower.count("hola"))

# Ejercicio 3
frase = "Aprender Python es aprender a pensar"
# Cuenta cuántas veces aparece la palabra "aprender"
# Debe contar todas aunque estén en mayúsculas/minúsculas
print(frase.lower().count("aprender"))

# Ejercicio 4
texto = "banana BANANA BaNaNa"
# Cuenta cuántas veces aparece "banana"
print(texto.count("banana"))

# Ejercicio 5
texto = "   ERROR error Error ERROR   "
# Cuenta cuántas veces aparece "error"
print(texto.count("error"))

# Ejercicio 6
texto = "uno,dos,uno,dos,UNO"
# Cuenta cuántas veces aparece "uno"
print(texto.count("uno"))

# Ejercicio 7
texto = "   python   "
# Cuenta cuántas veces aparece "python"
# Asegúrate de que los espacios no afecten el resultado
print(texto.count("python"))

# Ejercicio 8
texto = "Hola hola-hola hola"
# Cuenta cuántas veces aparece "hola"
# OJO: piensa si el guion afecta o no
print(texto.count("hola")) #no afecta si uso count

# Ejercicio 9
texto = "Mi lenguaje favorito es PYTHON. python es poderoso"
# Cuenta cuántas veces aparece "python"
print(texto.count("python"))

# Ejercicio 10
texto = "   aaaAAAaaa   "
# Cuenta cuántas veces aparece "a"
print(texto.count("a"))
