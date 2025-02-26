# otro ejemplo de programacion funcional usando lambda
numeros = [1, 2, 3, 4, 5]
resultado = list(map(lambda x: x * 2, numeros)) #Se puede pasar lambda como argumento de una funcion superior (map)
# para que se aplique en todos los elementos
print(resultado)  