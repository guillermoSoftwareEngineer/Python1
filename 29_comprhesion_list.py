#crear listas de form abreve, rapida y potente 

# Elevar al cuvo los numeros del 1 al 10

El_cubo = [x ** 3 for x in range(1,11)] # si es hasta 10 se debe poner el valor siguiente intervalo abierto
print(El_cubo)

# convertir temperaturas en celcius a farenheit

celcius =[20,25,30,40]
farenheit=[(temperatura * 9/5) + 32 for temperatura in celcius]
print(farenheit)

#numeros pares de uno a 10


pares = [ x for x in range(1,11) if x % 2 == 0]  # si es hasta 10 se debe poner el valor siguiente range(1,11) 
# intervalo abierto

# [expresión for variable in range(1,11) if condición]

print(pares)


# transposicion de matriz

matrix =[[1,2,3],
         [4,5,6],
         [7,8,9]]

# selecciona todos los valores de la primera columna es decir toma todas las filas y las 
# convierte en columnas e inversamente
transpuesta = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transpuesta)