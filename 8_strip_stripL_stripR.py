# Los métodos strip(), lstrip() y rstrip() se usan para eliminar caracteres
# (por defecto espacios en blanco) de los extremos de una cadena.

# strip(): Elimina los caracteres del inicio y del final.
# lstrip(): Elimina los caracteres solo al inicio (izquierda).
# rstrip(): Elimina los caracteres solo al final (derecha).

# Ejercicios
# Ejercicio 1:
# Define una variable con la cadena " Python " y utiliza strip() para eliminar los espacios en ambos extremos.

cadena = " Python"
print(cadena)
print(len(cadena))

nuevaCadena = cadena.strip()
print(nuevaCadena)
print(len(nuevaCadena)) # se elimino el espacio

# Ejercicio 2:
# Usa la misma cadena " Python " y aplica lstrip() para eliminar únicamente los espacios del inicio.

cadena2 = " python "
print(cadena2)
print(len(cadena2))

nuevaCadena2 = cadena2.lstrip() #elimina los espacios en la parte izquierda
print(nuevaCadena2)
print(len(nuevaCadena2))

# Ejercicio 3:
# Utiliza la cadena " Python " y aplica rstrip() para eliminar únicamente los espacios del final.

cadena3  = " Java "
print(cadena3)
print(len(cadena3))

nuevaCadena3 = cadena3.rstrip()
print(len(nuevaCadena3))

# Ejercicio 4:
# Crea una variable con el valor "***Hola***" y utiliza strip() especificando el carácter * para eliminarlo de ambos extremos.
saludo = "***hola***"
print(saludo)
print(len(saludo))

nuevoSaludo = saludo.strip("*") # se puede aclarar exactamente que caracter eliminar
print(nuevoSaludo)
print(len(nuevoSaludo))

# Ejercicio 5:
# Define una variable con el texto "!!!Bienvenido!!!" y utiliza strip("!") para quitar los signos de exclamación del inicio y del final.

exclamacion = "!!!Bienvenido!!!"
print(exclamacion)
print(len(exclamacion))

nuevaExclamacion = exclamacion.strip("!")
print(nuevaExclamacion)
print(len(nuevaExclamacion))


# Ejercicio 6:
# Asigna a una variable la cadena " Aprendiendo Python " y muestra la longitud de la cadena antes y después de aplicar strip().
frase = " Aprendiendo Python "
print(len(frase))
nuevaFrase = frase.strip()
print(nuevaFrase)
print(len(nuevaFrase))


# Ejercicio 7:
# Crea una variable con la cadena que contenga tabulaciones y espacios, por ejemplo "\t Python\t", y utiliza strip() para limpiarla.

tabulaciones = "\t Python\t"
print(tabulaciones)
print(len(tabulaciones))

nuevaTabulaciones = tabulaciones.strip()
print(nuevaTabulaciones)
print(len(nuevaTabulaciones))

# Ejercicio 8:
# Define la cadena " Hola " y utiliza strip() para obtener el texto sin espacios al inicio y final.
sal_corto = " hola "
print(sal_corto)
nuevo_sal_corto = sal_corto.strip()
print(nuevo_sal_corto)

# Ejercicio 9:
# Con la cadena " Python ", primero aplica lstrip() y luego rstrip() en dos pasos separados para eliminar los espacios de ambos extremos.

snake = " python "
print(snake)
print(len(snake))
left = snake.lstrip()
print(left)
print(len(left))
right = snake.rstrip()
print(right)
print(len(right))

# Ejercicio 10:
# Define una variable con el texto "xxPythonxx" y utiliza strip("x") para eliminar las letras "x" de ambos extremos.
conX = "xxPythonxx"
print(conX)
print(len(conX))

nuevo_conX = conX.strip("x")
print(nuevo_conX)
print(len(nuevo_conX))

