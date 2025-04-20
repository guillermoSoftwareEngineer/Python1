# 1. Muestra los números del 1 al 10 usando while.

print("Conteo de 1 a 10")
conteo = 1
while (conteo <= 10):
    print(conteo)
    conteo += 1

# 2. Muestra los números del 10 al 1 (cuenta regresiva).

print("Conteo de 10 a 1")
conteo = 10
while (conteo >= 1):
    print(conteo)
    conteo -= 1

# 3. Pide números al usuario hasta que escriba 0. Muestra la suma total.

numeroActual = int(input("Por favor, ingresa un número: "))
suma = 0

while numeroActual != 0:
    suma = suma + numeroActual
    print(f"Tu numero ahora es {suma}")
    numeroActual = int(input("Por favor, ingresa un número: "))
    

# 4. Pide al usuario que escriba una contraseña hasta que acierte con "python123".

password = input("Por favor ingresa el password: ")
ValPassword = "python123"

while password != ValPassword:

    print("tu password no es correcto, intenta de nuevo porfavor")
    password = input("Por favor ingresa el password: ")
   

# 5. Pide números hasta que uno sea negativo. Muestra cuántos números positivos escribió.

numIngresado = int(input("Por favor ingresa un numero entero: "))
contador= 0

while numIngresado >= 0:
    print("el numero aun no es negativo")
    contador += 1  
    print(f"cantidad de intentos con positivos = {contador}")
    numIngresado = int(input("Por favor ingresa un numero entero: "))


# 6. Imprime los primeros 10 múltiplos de 3 (empezando en 3).

number3 = 3
contador = 1
primMult= 0

while contador != 4:
    primMult = number3 * contador
    print(primMult)
    contador += 1


# 7. Pide números al usuario y muestra el mayor de todos. Termina cuando escriba 0.

# 8. Crea un contador que pida confirmación con "s" o "n" para continuar.

# 9. Usa while para simular una barra de carga del 0% al 100%, de 10 en 10.

# 10. Imprime los primeros 5 números pares mayores que 10.

