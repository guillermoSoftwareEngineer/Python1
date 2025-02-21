# Sintaxis 

tareas = ["despertar","Tender la cama","Bañarme","vestirme","Hacer Cafe","Hacer huevos"]
# se pueden guardar diferentes tipos de datos ddentro de las listas
# tareas = ["despertar",True, 3, 3.1416, "J" ,"Hacer huevos"]

print (tareas)

# El tipo de dato es list
print ("las tareas son de tipo " + str(type(tareas)))

# consultar la longitud (numero de datos que tiene la lista tareas)
print(len(tareas))

# indexacion[]
# Saber u obtener el dato de alguna de las posiciones dentro de la lista( desde 0)

print(tareas[2])
print(tareas[0])
print(tareas[-1])

# sliceing

frase = "Esta es mi frase"

print(frase[0:7])
print(frase[0:3])# no incluye la ultima posicion, funciona como un intervalo abierto
print(frase[7:])# dejar vacio significa que va hasta el fin