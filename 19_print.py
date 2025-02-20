# print puede separar argumentos con , a la hora de imprimir 
pr_argument = 'Hola'
seg_argument = 'adios'
ter_argument = 'Hola de nuevo'
cuart_argument = 'Adios de Nuevo'

print(pr_argument, seg_argument)

# ARGUMENTO SEP 

# existe el argumento sep, que define el caracter de separacion de argumentos sep ='-'

print( pr_argument, seg_argument, ter_argument , cuart_argument, sep='- ')

# el ultimo parametro sep tambien debe estar separado por una coma de los demas argumentos

# ARGUMENTO AND

# hace que no se ejecute el salto de linea

print ('Esto es una oracion', end=' ') #Hace que se  imprima en una sola linea
print('completa')

# FORMAT STRINGS LITTERALS (f)

var1 = 33
var2 = True

print(f'Puedo traer la variable {var1}, y tambien la variable {var2} al literal')

#OTRA FORMA DE USAR FORMAT

frase = 'Hola Soy Guillermo'
frase2 = 'Estoy aprendiendo python'

print("frase {}, frase2 {}" .format(frase,frase2))

# salto de linea se hace co \n (el slash es inverido)

palabras = "saltos de \n linea"
print(palabras)

# CARACTERES DE ESCAPE

# usar el slash invertido, para los caracteres de escape

frase = ' Me estoy quedando sin ideas de strings \"jejej\"'
print(frase)
