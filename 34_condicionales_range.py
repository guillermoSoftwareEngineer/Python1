for i in range(20): #va hasta 19 es propio de range
    print(i)

for i in range(10,20): #va de 11 hasta 19 es propio de range
    print(i)

    # se pueden usar if dentro de range
    numbers =[1,2,3,4,5,6,7,8,9,10]
    print('numeros pares')
    for number in numbers:
        if number % 2 == 0:
            print(number)