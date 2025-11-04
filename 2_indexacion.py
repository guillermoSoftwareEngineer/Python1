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

# Ejercicios

# Ejercicio 1
# Imprime la primera letra usando indexación.

palabra = "Python"

print(palabra[0])

# Ejercicio 2
# Imprime la letra que está en la posición 3 (contando desde 0).

palabra = "index"

print(palabra[3])
# imprime 3 ya que palabra ahora es "index"


# Ejercicio 3
# Usando índice negativo, imprime el carácter !.
saludo = "Hola!"

print(saludo[4])
print(saludo[-1]) #tambien sirve

# Ejercicio 4
# Imprime la letra t que corresponde al tercer carácter del string (especifica el índice correcto).
frase = "Este es un texto"

print('El indice correcto es el 2, y la letra es:')
print(frase[2])

# Ejercicio 5
# Dado:
# Imprime la última letra usando un índice negativo (sin usar len).

s = "programa"
 print(s[-1])

# Ejercicio 6
# Imprime "uva" usando indexación de listas.
#  Dado un listado (lista):

lista = ["manzana", "pera", "uva", "kiwi"]

print[lista[2]]

# Ejercicio 7

# Dado:
# Imprime la letra "c" accediendo con índices encadenados.
mi_lista = ["a", ["b", "c", "d"], "e"]

print(mi_lista[1][1])

# El indice encadenaado se refiere a usar mas corchetes [] para acceder a un indicee anidado

# Ejercicio 8

# Usando indexación simple (no slicing aún), imprime la letra k. ¿Qué índice usas?
# Dado:


texto2 = "abcdefghijkl"
print(texto2[10])

# Ejercicio 9
# Dado:
# Imprime la penúltima letra usando índice negativo.

pal = "secreto"

print(pal[-1])

# Ejercicio 10
# Dado:
# Imprime el carácter 5 de la cadena. (Pista: piensa en su posición contando desde 0.)

cad = "123456789"

print(cad[4])









