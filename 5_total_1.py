# Ejercicios del día (repaso inteligente)

# 1. Indexación básica – positiva

# Dada la cadena "Colombia", imprime la letra que está en la posición 3.

cadena ='Colombia'

print(cadena[3])

# 2. Indexación básica – negativa

# Con la cadena "Python", imprime la última letra.

cadena = 'python'

print(cadena[-1])

# 3. Replicación simple

# Crea la variable m = "hey " y repítela 7 veces.

m = 'hey '

print(m * 7)

# 4. Concatenación con espacio

# Concatena "Hola" y "Guillermo" con un espacio en medio.

print('hola' + ' ' + 'Guillermo')

# 5. Concatenación + indexación

# De la palabra "Mariposa", imprime la primera letra y luego la última concatenadas, quedando así:
# Ma

ins ='Mariposa'

print(ins[0] + ins[-1])

# 6. Replicación numérica convertida a texto

# Convierte el número 5 en texto y repítelo 4 veces.

num = 5

rep =str(num)

print(rep *4)

# 7. Indexación intermedia

# De "ABCDEFGHIJK", imprime la letra en la posición 5.

abecedario = 'ABCDEFGHIJK'

print(abecedario[5])

# 8. Replicación con salto de línea

# Crea "Hola\n" y repítelo 3 veces.

greet = 'hola\n'

print(greet * 3)

# 9. Concatenar emojis

# Concatena "🔥" dos veces y luego "⚡" tres veces en un solo print.

emoj1 = "🔥"
emoj2 = "⚡"

print(emoj1 * 2 + emoj2 * 3)

# 10. Replicación y concatenación juntas

# Crea una variable g = "Go" y produce:
# GoGoGoPython

g = 'Go'
lenguage = 'Python'


print(g *3 + lenguage)
