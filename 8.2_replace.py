# DÍA 6 — replace()

# Primer método que MODIFICA el contenido del texto

#  replace(): TRANSFORMA.

# replace() sustituye texto por otro texto, exactamente como se le indica.
# No entiende contexto, no interpreta intención, solo reemplaza coincidencias exactas.

# texto.replace("lo_que_busco", "lo_que_pongo")


# REGLAS
# Distingue mayúsculas y minúsculas

# Reemplaza todas las coincidencias (por defecto)

# No modifica el string original (crea uno nuevo)

# No elimina espacios “porque sí” → los reemplaza

# EJERCICIOS REEPLACE

# Ejercicio 1
texto = "Hola Mundo"
# Reemplaza "Mundo" por "Python"
# Imprime el resultado
nuevo_texto = texto.replace("Mundo","Python")
print(texto)
print(nuevo_texto)# crea una nueva cadena


# Ejercicio 2
texto = "Python es poderoso"
# Reemplaza "poderoso" por "increíble"
# Imprime el resultado
print(texto)
print(texto.replace("poderoso","increíble" )) # crea una nueva cadena



# Ejercicio 3
texto = "banana banana banana"
# Reemplaza "banana" por "manzana"
# Imprime el resultado
print(texto)
print(texto.replace("banana","manzana")) # crea una nueva cadena


# Ejercicio 4
texto = "Hola   Mundo"
# Reemplaza los espacios dobles por un solo espacio
# Imprime el resultado
print(texto)
print(texto.replace("  "," "))


# Ejercicio 5
texto = "ERROR error Error"
# Convierte todo a minúsculas
# Reemplaza "error" por "fallo"
# Imprime el resultado
textomin = texto.lower()
print(textomin.replace("error","fallo"))


# Ejercicio 6
texto = "python,java,python,c++"
# Reemplaza las comas por espacios
# Imprime el resultado
print(texto)
print(texto.replace(",", " "))


# Ejercicio 7
texto = "Aprender Python es aprender a pensar"
# Reemplaza "aprender" por "practicar"
# (piensa si necesitas normalizar antes)
# Imprime el resultado
print(texto)
 # como Aprender tiene mayuscula al principio se cambia solo la segunda coincidencia exacta
#  no es necesario normalizar ya que solo se reemplaza la palabra exacta "aprender"
print(texto.replace("aprender","practicar"))


# Ejercicio 8
texto = "   hola   mundo   "
# Elimina espacios de los bordes
# Reemplaza los espacios internos por un guion "-"
# Imprime el resultado
print(texto)
print(texto.strip().replace("   ","-"))


# Ejercicio 9
texto = "2024-05-10"
# Reemplaza "-" por "/"
# Imprime el resultado
print(texto)
print(texto.replace("-","/"))


# Ejercicio 10 (clave)
texto = "hola   hola   hola"
# Usa replace() para que quede:
# "hola hola hola"
# Imprime el resultado
print(texto)
print(texto.replace("  "," "))
