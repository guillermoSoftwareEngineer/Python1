# se debe separar la matriz por filas

# 123
# 456
# 789                columna
        #  fila       0  1  2

#            0       [[1,2,3],
#            1       [4,5,6],
#            2       [7,8,9]]

#cada elemento de la matriz tiene una posicion en fila y una en columna
# el numero nueve representa la posicion (2,2)

matrix =[[1,2,3],[4,5,6],[7,8,9]]

print(matrix)
print(matrix[0]) # muestra la primera lista

print(matrix[1][0]) # muestra el cuatro por que se enlazan

matrix =[[[1,2,3],[4,5,6],[7,8,9]],[[10,12,13],[24,25,26],[37,38,39]]]

print(matrix[1][1][2]) # muestra el 25 por que se enlazan