# en la indexacion, podemos acceder a determinada letra de un string mediante el uso de []
# mas su ubicacion dentro del string contando desde 0 

texto = "Este es un texto"

# 0 = 'E' 
print(texto[0]) #imprime la 'E'
# 1 = 's'
print(texto[1]) #imprime la 's'
# 2 = 't'
print(texto[2]) #imprime la 't'

# Tambien funciona usando como parametros numeros negativos y empieza desde el final
# imprime los numeros desde la ultima letra para atras

# -1 = 'o' 
print(texto[-1]) #imprime la 'o'
# -2 = 't'
print(texto[-2]) #imprime la 't'
# -3 = 'x'
print(texto[-3]) #imprime la 'x'