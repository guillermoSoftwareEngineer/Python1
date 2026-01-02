word_1 = 'cualquier Palabra'
word_2 = 'otra'

print(len(word_1)) # muestra que tantos caracrteres tiene la variable word_1
print(len(word_2))# muestra que tantos caracrteres tiene la variable word_2

# EJERCICIOS DE len() (SIN RESOLVER)

#  Ejercicio 1
# Crea una variable con tu nombre y muestra cuántos caracteres tiene usando len().

nombre ="Guillermo"
print(len(nombre))

# Ejercicio 2
# Guarda la palabra "Python" en una variable y muestra su longitud.

lenguaje = "python"
print(len(lenguaje))

# Ejercicio 3
# Crea una lista con 5 frutas y muestra cuántos elementos tiene la lista usando len().

lista_frutas = ["manzana", "pera", "naranja", "patilla", "guanabana"]
print(len(lista_frutas))


# Ejercicio 4
# Dada la cadena "Aprender Python", muestra cuántos caracteres tiene incluyendo el espacio.

cadena = "aprender Python"
print(len(cadena))

# Ejercicio 5
# Concatena "Hola" y "Mundo" con un espacio y muestra la longitud del resultado usando len().

mensaje_1 = "hola"
mensaje_2 = "Mundo" 

t_mensaje = mensaje_1 + " " + mensaje_2
print(t_mensaje)
print(len(t_mensaje))

# Ejercicio 6
# Repite la cadena "Hi" 4 veces y muestra la longitud final del texto resultante.

s_mensaje = "hi"
s_cadena = s_mensaje * 4
print(len(s_cadena ))

# Ejercicio 7
# Crea una variable con "ABCDE" y muestra el último índice válido usando len()
# (pista: el último índice NO es igual a la longitud)

variable = "ABCDE"
print(len(variable)-1)

# Ejercicio 8
# Crea una lista con números del 1 al 10 y muestra cuántos elementos tiene usando len().

n_lista =[1,2,3,4,5,6,7,8,9,10]
print(len(n_lista))

# Ejercicio 9
# Dada la cadena "12345", imprime su longitud y luego imprime su último carácter usando len() para calcular el índice.

o_cadena = "12345"
print(len(o_cadena))
print(o_cadena[len(o_cadena)-1])

# Ejercicio 10
# Crea una cadena "Error" y usa len() para demostrar por qué intentar acceder a cadena[len(cadena)] sería incorrecto
# (no ejecutes el error, solo muéstralo en un print como texto explicativo)

e_cadena = "Error"

print(len(e_cadena)) # cuenta en realidad que hay 5 caracteres

# print(e_cadena[len(e_cadena)]) len cuenta desde uno, pero como al usar [] se busca 
# desde la posicion 0 no encuentra el 5 caracter

# NOTA IMPORTANTE

# con [] se indexa desde 0, SE CUENTA DESDE 0 CERO
# con la funcion len()  SI cuenta cuántos elementos existen, No cuenta posiciones, No conoce índices

