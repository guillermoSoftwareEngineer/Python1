# BLOQUE DE EJERCICIOS — Lectura de registros estructurados (Nivel Junior)
# Objetivo real: leer datos textuales estructurados como lo haría un analista junior
# Enfoque: registros, campos, limpieza y decisión consciente de impresión

# HERRAMIENTAS PERMITIDAS:
# split(), strip(), lower(), upper(), replace(), len()
# for, if
# indexación individual de listas
# print()

# PROHIBIDO:
# range, slicing
# métodos de listas
# listas nuevas
# diccionarios
# modificar la lista original


# EJERCICIO 1
logs = "INFO|System started\nERROR|Disk failure\nWARNING|Low memory"
# Separa el texto en líneas usando "\n".
# Recorre cada línea.
# Imprime SOLO la línea completa que contenga "ERROR".
lineas = logs.split("\n")
for line in lineas:
    if "ERROR" in line:
        print(line)

print("*"*25) # por que estoy confundiendo cada ejercicio al ejecutar en la terminal para revisar


# EJERCICIO 2
data = "Juan,34,Bogota\nMaria,29,Medellin\nPedro,41,Cali"
# Cada línea representa una persona: nombre,edad,ciudad
# Recorre cada línea.
# Separa cada línea por ",".
# Imprime SOLO el nombre de las personas que viven en "Bogota".

for linea in data.split("\n"):
    if linea.split(",")[2] == "Bogota": # al usar split se obtienen tres objetos cada uno con una linea, y su contenido tiene indexacion
        print(linea.split(",")[0]) #index 0 equivale al nombre

print("*"*25) # por que estoy confundiendo cada ejercicio al ejecutar en la terminal para revisar


# EJERCICIO 3
registros = "ok|200\nfail|500\nok|201\nfail|404"
# Cada línea tiene estado|codigo
# Recorre cada línea.
# Imprime SOLO los códigos de las líneas cuyo estado sea "fail".

for registro in registros.split("\n"):
    if registro.split("|")[0] == "fail":
        print(registro.split("|")[1])

print("*"*25) # por que estoy confundiendo cada ejercicio al ejecutar en la terminal para revisar

# EJERCICIO 4
usuarios = "admin:true\nguest:false\nroot:true\nuser:false"
# Cada línea tiene usuario:activo
# Recorre cada línea.
# Imprime SOLO el nombre de los usuarios activos (true).

for usuario in usuarios.split("\n"):
    if usuario.split(":")[1] == "true":
        print(usuario.split(":")[0])

print("*"*25) # por que estoy confundiendo cada ejercicio al ejecutar en la terminal para revisar

# EJERCICIO 5
csv = "id,name,email\n1,Ana,ana@mail.com\n2,,noemail\n3,Carlos,c@mail.com"
# Ignora la primera línea (encabezado).
# Recorre las demás.
# Imprime SOLO las líneas donde el nombre NO esté vacío.


for lineas in csv.split("\n")[1:]:
    if lineas.split(",")[1] != "":
        print(lineas)
   
    
print("*"*25) # por que estoy confundiendo cada ejercicio al ejecutar en la terminal para revisar




# EJERCICIO 6
logs = "INFO | 2026-01-11 | System Started\nERROR | 2026-01-12 | Disk Failure"
# Recorre cada línea.
# Limpia espacios laterales.
# Separa por "|".
# Imprime SOLO la fecha de las líneas cuyo nivel sea "ERROR".


for linea in logs.split("\n"):
    campos = linea.split("|")
    print("campos es " + str(campos))# para entender mejor el ejercicio

    nivel = campos[0].strip()
    fecha = campos[1].strip()

    if nivel == "ERROR":
        print(fecha)


print("*"*25) # por que estoy confundiendo cada ejercicio al ejecutar en la terminal para revisar
    
 # EJERCICIO 7
ventas = "Laptop;1200\nMouse;25\nKeyboard;0\nMonitor;300"

# REGLAS ESPECÍFICAS:
# - Cada línea tiene exactamente: producto;precio
# - El precio se evalúa como TEXTO, no como número
# - No convertir tipos
# - No eliminar líneas
# OBJETIVO:
# Recorre cada línea.
# Imprime SOLO el nombre del producto
# cuyo precio NO sea exactamente "0".

for linea in ventas.split("\n"):
    # print(linea)
    campos = linea.split(";")

    producto = campos[0]
    valor = campos[1]

    if valor != "0":
        print(producto)


   
   
print("*"*25) # por que estoy confundiendo cada ejercicio al ejecutar en la terminal para revisar



# EJERCICIO 8
registros = "OK|user1\nOK|user2\nFAIL|user3\nOK|user4"

# REGLAS ESPECÍFICAS:
# - Cada línea tiene exactamente: estado|usuario
# - No transformar el estado para evaluarlo
# OBJETIVO:
# Recorre cada línea.
# Imprime SOLO el nombre del usuario
# cuyo estado sea exactamente "OK".

for index in registros.split("\n"):
    estado = index.split("|")[0]
    usuario = index.split("|")[1]
    if estado == "OK":
        print(usuario)

print("*"*25) # por que estoy confundiendo cada ejercicio al ejecutar en la terminal para revisar

# EJERCICIO 9
paths = "/home/user/docs\n/var/log/system\n/etc/nginx/conf"

# REGLAS ESPECÍFICAS:
# - Cada línea es una ruta
# - Puede comenzar con "/"
# - No usar slicing
# - No asumir cantidad fija de niveles
# OBJETIVO:
# Recorre cada ruta.
# Elimina el "/" inicial SOLO si existe.
# Separa por "/".
# Imprime SOLO el último elemento de cada ruta.

for ruta in paths.split("\n"):
    ruta = ruta.split("/")[-1]
    print(ruta)
   


   
  print("*"*25) # por que estoy confundiendo cada ejercicio al ejecutar en la terminal para revisar  



# EJERCICIO 10 (CONCEPTUAL — sin código)
# Explica con tus palabras:
# por qué en este bloque:
# - se trabaja con registros completos
# - se accede a campos específicos
# - se decide qué imprimir
# y por qué esto representa mejor el trabajo real
# de un analista de datos junior que usar split() de forma aislada.

# por que es evidente que esto se acerca mas a la manipulacion de datos, por ejemplo, ya seria facil acceder a filas y columnas
# o a objetos que tienen los datos ordenados, listos para manipulacion, tambien como se pueden manejar celdas vacias o nulas
# seleccionar elementos debe acercarse mas a lo fundamental en cuanto a datos