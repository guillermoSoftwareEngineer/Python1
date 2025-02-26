# EL generador
# Produce  un conjunto de numeros de los cuales podemos iterar

def generador(): #se define la funcion
    yield 1  # se definen los valores dentro de esa funcion
    yield 2
    yield 3
    yield 4
    yield 5

    # se llaman los valores

for valor in generador():
    print(valor)

