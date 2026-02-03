# BLOQUE DE EJERCICIOS — split() integrado (preparación Data Analysis)
# Objetivo: usar split() junto con métodos de string ya vistos
# Enfoque: extracción de campos, normalización y lectura de datos textuales

# Herramientas permitidas:
# split(), lower(), upper(), strip(), lstrip(), rstrip(), replace(), len(), print()
# indexación individual de listas
# variables

# PROHIBIDO:
# bucles, if, slicing, métodos de listas, listas manuales


# EJERCICIO 1
texto = " Juan , Perez , 34 , Bogota "
# Normaliza el texto (elimina espacios laterales).
# Separa por coma.
# Obtén SOLO el nombre.
# Guarda el resultado en una variable llamada nombre.
# Imprime nombre.
nombre = texto.strip().split(",")[0]
print(nombre)


# EJERCICIO 2
texto = "ERROR|WARNING|INFO"
# Convierte todo a minúsculas.
# Separa usando "|".
# Obtén SOLO el último nivel.
# Guarda el resultado en una variable llamada nivel.
# Imprime nivel.
nivel = texto.lower().split("|")[-1]
print(nivel)



# EJERCICIO 3
texto = "Python, Java, Go, Rust"
# Elimina espacios innecesarios.
# Separa usando ",".
# Obtén SOLO "Go".
# Guarda el resultado en una variable llamada lenguaje.
# Imprime lenguaje.
lenguaje = texto.replace(" ","").split(",")[2]
print(lenguaje)

# EJERCICIO 4
registro = "id:1024|user:admin|status:ACTIVE"
# Convierte todo a minúsculas.
# Separa usando "|".
# Obtén SOLO el campo "status:active".
# Guarda el resultado en una variable llamada estado.
# Imprime estado.
estado = registro.lower().split("|")[2]
print(estado)


# EJERCICIO 5
fecha = "2026/01/11"
# Separa usando "/".
# Obtén SOLO el mes.
# Guarda el resultado en una variable llamada mes.
# Imprime mes.
mes =fecha.split("/")[1]
print(mes)

# EJERCICIO 6
ruta = "/var/log/system/error"
# Elimina el primer "/" si es necesario.
# Separa usando "/".
# Obtén SOLO "system".
# Guarda el resultado en una variable llamada carpeta.
# Imprime carpeta.
carpeta = ruta.lstrip("/").split("/")[2] 
print(carpeta)

# EJERCICIO 7
csv = "id,name,email"
# Convierte todo a mayúsculas.
# Separa usando ",".
# Obtén SOLO el segundo campo.
# Guarda el resultado en una variable llamada campo.
# Imprime campo.
campo = csv.upper().split(",")[1]
print(campo)


# EJERCICIO 8
log = " INFO | 2026-01-11 | System Started "
# Elimina espacios laterales.
# Separa usando "|".
# Obtén SOLO la fecha.
# Guarda el resultado en una variable llamada fecha_log.
# Imprime fecha_log.
fecha_log = log.strip().split("|")[1]
print(fecha_log.lstrip()) # para normalizar mejor la respuesta uso lstrip


# EJERCICIO 9
texto = "producto=Laptop;precio=1200;stock=25"
# Convierte todo a minúsculas.
# Separa usando ";".
# Obtén SOLO "precio=1200".
# Guarda el resultado en una variable llamada precio.
# Imprime precio.
precio = texto.lower().split(";")[1]
print(precio)


# EJERCICIO 10 (conceptual, sin código)
# Explica con palabras:
# por qué split() es una herramienta clave para convertir texto del mundo real
# # en datos que luego pueden analizarse.
# por que generalmente los datos vienen separados por elementos o caracteres como ; , entre otros
# debido a eso para organizar y separar split() permite convertir a datos analizables
# de un texto plano a datos organizados