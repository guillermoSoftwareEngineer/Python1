# Tema: slicing 
# Slicing es una forma de leer una parte de una lista sin modificarla.
# No crea lógica.
# No decide nada.
# No procesa datos.
# ¿Qué segmento continuo de esta lista quiero ver?
# slicing → devuelve una lista

# Un slicing se define por tres ideas:
# Desde dónde empiezo
# Hasta dónde termino
# Sin incluir el final (El límite derecho nunca se incluye)

elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Quiero los elementos desde la posición 1
# hasta antes de la posición 4
print(elementos[1:4]) # los indices se cuentan desde 0

# Ejercicios


lista = ["uno", "dos", "tres", "cuatro", "cinco", "seis"]

# EJERCICIO B-1
# Obtén una nueva lista con los primeros 3 elementos.
new_lista = lista[0:3]
print(new_lista)

# EJERCICIO B-2
# Obtén una nueva lista con los elementos desde la posición 2
# hasta la posición 5 (sin incluir la 5).
print(lista[2:5])


# EJERCICIO B-3
# Obtén una nueva lista con los últimos 2 elementos.
print(lista[len(lista)-2:])


# EJERCICIO B-4
# Obtén una nueva lista con todos los elementos excepto el primero.
print(lista[1:])


# EJERCICIO B-5
# Obtén una nueva lista con todos los elementos excepto el último.
print(lista[0:len(lista)-1])


# EJERCICIO B-6
# Obtén una nueva lista con los elementos desde "dos" hasta "cuatro"
# usando posiciones, no texto.
print(lista[1:3])


# EJERCICIO B-7
# Obtén una nueva lista con los primeros 4 elementos.
print(lista[0:4])


# EJERCICIO B-8
# Obtén una nueva lista con los elementos del medio:
# excluye el primero y el último.
print(lista[1:len(lista)-1  ])


# EJERCICIO B-9
# Obtén una nueva lista vacía usando slicing
# (no elimines la lista original).
lista_vacia = lista[(len(lista)+1):(len(lista)+2)]
print(lista_vacia)

# EJERCICIO B-10
# Explica con palabras (sin código):
# qué significa exactamente lista[1:4]

# significa tomar los datos desde la posicion index 1, es decir el segundo valor de la lista,
# hasta la posicion 3 ya que el ultimo indice del argumento es 4 y este no se incluye





