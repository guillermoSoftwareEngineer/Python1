# Ejemplo 1

# se crea la cadena
cadena = 'Este es un texto'

# se crea el iterador 

iterador_texto = iter(cadena)

# se itera en la cadena con for

for char in cadena:
    print(char)

# Ejemplo 2
# iterar numeros impares

limite = 20

limite_par = iter(range(1,limite +1,2))

for num in limite_par:
    print(num)