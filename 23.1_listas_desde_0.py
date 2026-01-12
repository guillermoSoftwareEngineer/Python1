# Qué es una lista (sin sintaxis)

# Una lista es una estructura que existe para contener 
# varios valores juntos cuando un solo valor no es suficiente.

# “Tengo varias cosas y necesito tratarlas como una sola unidad”.

# las listas tiene  posiciones, que empiezan desde 0

lista = ["uno","dos","tres","cuatro","cinco"]

# la forma de acceder a ellas es a traves de la sintaxis (que no modifica la lista)

# lista[posicion]

print(lista[0])# imprime "uno" para este caso
print(lista[1])# imprime "dos" para este caso
print(lista[2])# imprime "tres" para este caso
print(lista[3])# imprime "cuatro" para este caso
print(lista[4])# imprime "cinco" para este caso

# EJERCICIO A-1
texto = "  Python,Java,Go  "
# Limpia espacios al inicio y al final.
# Luego separa usando la coma ",".
# Guarda el resultado en una variable llamada lenguajes.
lenguajes = (texto.strip().split(","))
print(lenguajes)


# EJERCICIO A-2
texto = "ERROR|WARNING|INFO"
# Convierte todo el texto a minúsculas.
# Luego separa usando "|".
# Guarda el resultado en una variable llamada niveles.
niveles = texto.lower().split("|")
print(niveles)


# EJERCICIO A-3
texto = "uno--dos--tres"
# Separa el texto usando el separador "--".
# Guarda el resultado en una variable llamada resultado.
resultado = texto.split("--")
print(resultado)

# EJERCICIO A-4
texto = "  manzana, pera, banana  "
# Limpia espacios al inicio y al final del string completo.
# Luego reemplaza ", " por ",".
# Luego separa usando la coma.
# Guarda el resultado en una variable llamada frutas.
frutas = texto.strip().replace(", ",",").split(",")
print(frutas) 


# EJERCICIO A-5
registro = "Juan Perez | 34 | Bogota"
# Limpia espacios al inicio y al final. lo hare pero no es necesario no hay espacios al principio o final
# Luego separa usando el separador " | ". lo hare pero no es necesario ya esta asi
# Guarda el resultado en una variable llamada datos.
datos =registro.strip().split(" | ")
print(datos)



# EJERCICIO A-6
texto = "Python  es  potente"
# Reemplaza los dobles espacios por un solo espacio.
# Luego separa usando el espacio " ".
# Guarda el resultado en una variable llamada resultado.
resultado = texto.replace("  "," ").split(" ")
print(resultado)

# EJERCICIO A-7
texto = "Rojo,Verde,Azul"
# Convierte todo el texto a minúsculas.
# Luego separa usando la coma.
# Guarda el resultado en una variable llamada colores.
colores = texto.lower().split(",")
print(colores)



# EJERCICIO A-8
linea = " email: contacto@empresa.com "
# Limpia espacios al inicio y al final.
# Reemplaza "email:" por una cadena vacía.
# Luego separa usando "@".
# Guarda el resultado en una variable llamada resultado.
resultado = linea.strip().replace("email:"," ").split("@")
print(resultado)


# EJERCICIO A-9
texto = "Python;Data;Engineering;2026"
# Convierte todo el texto a mayúsculas.
# Luego separa usando ";".
# Guarda el resultado en una variable llamada partes.
partes =texto.upper().split(";")
print(partes)


# EJERCICIO A-10
texto = "uno  dos   tres"
# Reemplaza los dobles espacios por un solo espacio.
# Luego separa usando el espacio.
# Guarda el resultado en una variable llamada resultado.
resultado = texto.replace("  "," ").split(" ")
print(resultado)