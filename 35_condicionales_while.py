# whilw mientras

condicion = True

while condicion == True:
    if condicion == False: # si esta condicion se cumple
        break #break finaliza el while
    print('Es verdadero')
    condicion = False


# si se desea saltar el codigo para continuar en otro lado se usa continue

numeros = [1,2,3,4,5,6,7,8,9,0]

for i in range (10):
    if i == 5: #omite el 5
        continue
    print(i)
   