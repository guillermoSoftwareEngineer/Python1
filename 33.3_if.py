# Qué es if

# if es una estructura de control condicional.
# Sirve para:

# Ejecutar un bloque de código SOLO si se cumple una condición.

# Sintaxis mínima explicada
# if condicion:
#     accion

# Explicacion:

# if → palabra reservada
# condicion → una expresión que se evalúa como:
# True (verdadero)
# False (falso)
# : → inicia el bloque
# indentación → lo que se ejecuta solo si la condición es verdadera

# Ejemplo 

edad = 20

if edad >= 18:
    print("Es mayor de edad")

# El orden correcto es:

# for → recorrer
# if → decidir
# for + if → procesar datos reales

# BLOQUE DE EJERCICIOS — for + if (FILTRADO)


# EJERCICIO H-1
texto = "Python,Java,Go,Rust"
# Imprime SOLO los lenguajes que NO estén en minúsculas


# EJERCICIO H-2
texto = "Python,Java,Go,Rust"
# Imprime SOLO los lenguajes con más de 3 letras
# Pista: no necesitas len


# EJERCICIO H-3
texto = "ERROR|WARNING|INFO"
# Convierte a minúsculas
# Imprime SOLO el nivel "warning"


# EJERCICIO H-4
texto = "rojo|verde|azul|amarillo"
# Convierte a minúsculas
# Imprime SOLO los colores que contienen la letra "a"


# EJERCICIO H-5
texto = "Juan,Perez,34,Bogota"
# Imprime SOLO los elementos que NO sean números


# EJERCICIO H-6
texto = "Python  es  potente"
# Reemplaza dobles espacios por uno
# Imprime SOLO las palabras que sean distintas de "es"


# EJERCICIO H-7
texto = "A,B,C,D,E"
# Imprime SOLO las letras que NO sean "C"


# EJERCICIO H-8
texto = "2026/01/11/logs/system"
# Imprime SOLO las partes que estén en minúsculas


# EJERCICIO H-9
texto = "ERROR|warning|Info"
# Imprime SOLO los elementos que NO estén completamente en minúsculas


# EJERCICIO H-10
# Explica con palabras (sin código):
# por qué for + if NO modifica la lista original
