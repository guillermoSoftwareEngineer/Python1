# Slicing básico en strings

# Slicing es pedir un rango de caracteres

# Sintaxis

# texto[inicio:fin]

# REGLAS

# inicio sí se incluye
# fin NO se incluye

texto = "Python"
texto[0:2]  
print(texto[0:2])

# Si inicio es 0, puedes omitirlo
texto = "Python"
texto[0:3] # escribe Pyt cuenta desde 0,1,2,3 pero  fin NO se incluye
print(texto[0:3])
texto[:3] #es lo mismo


# Si fin es len(texto), puedes omitirlo
texto2 = "Pythoniso"
texto2[2:6] #inicio sí se incluye P=0 y=1 t=2 h=3 o=4 n=5  salida desde la t t=2
print(texto2[2:6])   #   P=0 y=1 t=2 h=3 o=4 n=5 i =6  pero como fin NO se incluye salida hasta la n n=5 una menos que :6]
# resultado de salida "thon" 
texto2[2:]

# EJERCICIOS DE SLICING 

# Ejercicio 1
# Dada la cadena "Python"
# Imprime las dos primeras letras usando slicing

cad = "Python"
print(cad[:2])


# Ejercicio 2
# Dada la cadena "Programar"
# Imprime desde la letra "g" hasta la "m" (inclusive en el resultado)

pro = "Programar"
print(pro[3:7])


# Ejercicio 3
# Dada la cadena "Aprender Python"
# Imprime solo la palabra "Aprender"

apr = "Aprender Python"
print(apr[:8])


# Ejercicio 4
# Dada la cadena "Aprender Python"
# Imprime solo la palabra "Python"
apr2 = "Aprender Python"
print(apr[9:])

# Ejercicio 5
# Dada la cadena "abcdefgh"
# Imprime los caracteres desde el índice 2 hasta el 5
abc = "abcdefgh"
print(abc[2:6])

# Ejercicio 6
# Dada la cadena "Hola Mundo"
# Imprime desde el inicio hasta el carácter antes del espacio

hol = "Hola Mundo"
print(hol[:4])


# Ejercicio 7
# Dada la cadena "Hola Mundo"
# Imprime desde el espacio hasta el final (incluyendo el espacio)
hol2 = "Hola Mundo"
print(hol2[4:])

# Ejercicio 8
# Dada la cadena "Python"
# Imprime todo menos la última letra usando slicing

cadp ="Python"
print(cadp[:5])

# Ejercicio 9
# Dada la cadena "Programación"
# Usa len() para imprimir los últimos 3 caracteres con slicing
prog = "Programación"
total=len(prog)
print(prog[9:total])

# Ejercicio 10
# Dada la cadena "SlicingEsPoder"
# Imprime una subcadena que empiece en el índice 3 y termine en el 9
power = "SlicingEsPoder"
print(power[3:10])


# CONSOLIDACION 
# Ejercicio 1
# Dada la cadena:
# texto = "Elefante"
# Imprime "Ele" usando slicing.

texto = "Elefante"
print(texto[:3])

# Ejercicio 2
# Dada la cadena:
# palabra = "Computadora"
# Imprime "put" usando slicing.

palabra = "Computadora"
print(palabra[3:6])

# Ejercicio 3
# Dada la cadena:
# frase = "Python es poder"
# Imprime solo "Python".

frase = "Python es poder"
print(frase[:6])


# Ejercicio 4
# Dada la cadena:
# frase = "Python es poder"
# Imprime solo "poder"
# usa len()

frase = "Python es poder"
print(frase[len(frase)-5:])


# Ejercicio 5
# Dada la cadena:
# codigo = "ABCDEF"
# Imprime los últimos 2 caracteres usando len() y slicing.

codigo = "ABCDEF"
print(codigo[len(codigo)-2:])


# Ejercicio 6 (explicación en código)
# Completa este print() sin cambiar el texto, solo el slicing:
# texto = "Slicing"
# print("La palabra 'Sli' sale porque uso:", texto[ ??? ])

texto = "Slicing"
print("La palabra 'Sli' sale porque uso:", texto[ :3 ])

# Bloque 3 — Regla final (una sola línea)
# Escribe una sola línea, sin código, que complete esta frase:
# “En slicing, el índice de inicio __________ y el índice de fin __________.”
# “En slicing, el índice de inicio se cuenta desde el indice 0 y se incluye y el índice de fin no se incluye
# asi que si quiero llegar hata el indice 6 debo terminar el slicing co el siguiente [:7].”