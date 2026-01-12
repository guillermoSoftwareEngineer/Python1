# EJERCICIO MC-1
texto = "  Python,Java,Go  "
# Elimina espacios sobrantes al inicio y al final.
# Luego separa el texto usando la coma ",".
# Guarda el resultado en una variable llamada lenguajes.
lenguajes = texto.strip().split(",")
print(lenguajes)

# EJERCICIO MC-2
texto = "ERROR|WARNING|INFO"
# Convierte todo el texto a minúsculas.
# Luego separa usando el separador "|".
# Guarda el resultado en una variable llamada niveles.
niveles =texto.lower().split("|")
print(niveles)

# EJERCICIO MC-3
texto = "uno--dos--tres--cuatro"
# Separa el texto usando "--".
# Guarda el resultado en una variable llamada resultado.
resultado = texto.split("--")
print(resultado)

# EJERCICIO MC-4
texto = "  manzana, pera, banana  "
# Elimina espacios sobrantes al inicio y al final del texto completo.
# Luego reemplaza ", " por ",".
# Luego separa el texto usando la coma ",".
# Guarda el resultado en una variable llamada frutas.
frutas = texto.strip().replace(", ",",").split(",")
print(frutas)


# EJERCICIO MC-5
texto = "nombre:Juan|edad:34|ciudad:Bogota"
# Convierte todo el texto a minúsculas.
# Luego separa el texto usando el separador "|".
# Guarda el resultado en una variable llamada datos.
datos = texto.lower().split("|")
print(datos)


# EJERCICIO MC-6
texto = "Python  es  potente"
# Reemplaza todos los dobles espacios "  " por un solo espacio " ".
# Luego separa el texto usando el espacio " " como separador.
# Guarda el resultado en una variable llamada resultado.
resultado = texto.replace("  "," ").split(" ")
print(resultado)
