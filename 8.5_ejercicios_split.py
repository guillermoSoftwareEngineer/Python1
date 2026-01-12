# EJERCICIO 1
texto = "Python es potente"
# Usa split() para separar las palabras usando el espacio " " como separador.
# Guarda el resultado en una variable llamada resultado.

resultado = texto.split(" ")
print(resultado)


# EJERCICIO 2
texto = "uno,dos,tres,cuatro"
# Separa el texto usando la coma "," como separador.
# Guarda el resultado en una variable llamada partes.
partes = texto.split(",")
print(partes)


# EJERCICIO 3
texto = "sin-separadores-aqui"
# Usa split() con el separador "|".
# Guarda el resultado en una variable llamada resultado.
resultado = texto.split("|")
print(resultado)

#produce practicamente una lista con un solo elemento ya que el string no contiene "|"

# EJERCICIO 4
texto = "  manzana pera banana  "
# Elimina los espacios sobrantes al inicio y al final del texto.
# Luego separa las palabras usando el espacio " " como separador.
# Guarda el resultado final en una variable llamada frutas.

frutas =texto.strip().split(" ")
print(frutas)



# EJERCICIO 5
texto = "Rojo,Verde,Azul"
# Convierte todo el texto a minúsculas.
# Luego separa los valores usando la coma ",".
# Guarda el resultado en una variable llamada colores.
colores = texto.lower(  ).split(",")
print(colores)


# EJERCICIO 6
texto = "error--warning--info"
# Separa el texto usando "--" como separador.
# Guarda el resultado en una variable llamada niveles.
niveles =texto.split("--")
print(niveles)

# EJERCICIO 7
texto = "uno  dos   tres"
# Reemplaza todos los dobles espacios "  " por un solo espacio " ".
# Luego separa el texto usando el espacio " " como separador.
# Guarda el resultado en una variable llamada resultado.
resultado = texto.replace("  "," ").split(" ")
print(resultado)

# EJERCICIO 8
registro = "Juan Perez | 34 | Bogota"
# Elimina espacios sobrantes al inicio y al final del string completo.
# Luego separa el registro usando el separador " | ".
# Guarda el resultado en una variable llamada datos.
datos = registro.strip().split(" | ")
print(datos)


# EJERCICIO 9
linea = " email: contacto@empresa.com "
# Elimina espacios sobrantes al inicio y al final.
# Reemplaza "email:" por una cadena vacía.
# Luego separa el texto usando "@" como separador.
# Guarda el resultado en una variable llamada resultado.
resultado = linea.strip().replace("email:", " ").split("@")
print(resultado)

# EJERCICIO 10
texto = "Python;Data;Engineering;2026"
# Convierte todo el texto a mayúsculas.
# Luego separa el texto usando ";" como separador.
# Guarda el resultado en una variable llamada partes.
partes = texto.upper().split(";")
print(partes)