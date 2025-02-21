# Las tuplas son inmutables

tupla_number = (1,2,3,4,5,6,7,8)
print(tupla_number)
print(type(tupla_number))

print(tupla_number[0])

# tupla_number[0] = "numero" presentara error, por que una tupla no puede ser modificada (inmutabilidad)
print(tupla_number) 

# las tuplas see pueden definir sin parentesis
new_tupla = 7,8,9,10
print(type(new_tupla)) # mostrara que es clase tupla