# EJERCICIOS COMBATIENDO PROGRAMACION DEFENSIVA


lista = ["uno", "dos", "tres", "cuatro", "cinco", "seis"]

# EJERCICIO C-1
# Obtén los primeros 3 elementos.
print(lista[0:3])


# EJERCICIO C-2
# Obtén los últimos 2 elementos.
print(lista[-2:])


# EJERCICIO C-3
# Obtén todos los elementos excepto el primero.
print(lista[1:]) 


# EJERCICIO C-4
# Obtén todos los elementos excepto el último.
print(lista[:-1]) 

# EJERCICIO C-5
# Obtén los elementos desde "dos" hasta "cuatro"
# usando posiciones.
print(lista[1:4]) 

# EJERCICIO C-6
# Obtén una lista vacía usando slicing.
print(lista[0:0])


# EJERCICIO C-7
# Explica con palabras:
# qué significa exactamente lista[:3]
# significa que se toman los elementos desde el index cero hasta la posicion index dos
# ya que el ultimo termino no se incluye para este caso 3, de la lista

# EJERCICIO C-8
# Explica con palabras:
# qué significa exactamente lista[2:]
# significa que se toman los elementos desde el index dos hasta el final de la lista

# EJERCICIO C-9
# Explica con palabras:
# qué significa exactamente lista[:-1]
# significa que se toman los elementos desde el inicio de la lista, sin tomar el ultimo index -1


# EJERCICIO C-10
# Explica con palabras:
# por qué slicing devuelve una lista incluso
# cuando el resultado tiene un solo elemento.
# por que slicing esta hecho para trabajar con conjuntos de datos, listas en este caso,
# y existen conjuntos de un solo elemento 

# Slicing tambien funciona en strings archivo 7.1
var = "este es un texto"
print(var[0:4])