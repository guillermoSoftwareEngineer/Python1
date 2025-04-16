# 1. Crea una variable edad. Si es mayor o igual a 18, muestra “Puedes votar”, si no, “No puedes votar”.
entrada_edad = input("ingresa tu edad: ")
edad = int(entrada_edad) # para convertir el string en numero

if edad >= 18:
    print("Puedes Votar")
else:
    print("no puedes Votar")

# 2. Pide un número cualquiera. Si es mayor a 0, muestra “Positivo”, si es menor a 0, “Negativo”, si es 0, “Cero”.

entrada_numero = input("ingresa un numero: ")
numero = int(entrada_numero) # para convertir el string como numero

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Cero")


# 3. Crea una variable nota. Si es mayor o igual a 3, muestra “Aprobado”, si no, “Reprobado”.

nota = 3

if nota >= 3 :
    print("aprobado")
else:
    print("reprobado")

# 4. Crea dos variables a y b. Muestra cuál es mayor, o si son iguales.

var1 = 77 # equivale a la variable a
var2 = 77 # equivale a la variable b

if var1 > var2:
    print("la variable a es mayor que la b")
elif var2 > var1:
    print("la variable b es mayor que la a")
else:
    print("Las dos variables son iguales")


# 5. Crea una variable nombre. Si es igual a tu nombre, muestra “¡Hola, [nombre]!”, si no, “No te conozco”.

name = "Guillermo"

if name == "Guillermo":
    print("Hola " + name)
else:
    print("No te conozco")


# 6. Pide la edad de una persona. Si tiene 0 a 12 años, es “niño”; si 13 a 17, “adolescente”; si 18 a 59, “adulto”; si 60 o más, “adulto mayor”.

String_ed_Persona =input ("Ingresa tu edad por favor: ")
ed_persona = int(String_ed_Persona)

if ed_persona <= 12:
    print("niño")
elif ed_persona > 12 and ed_persona <= 17 :
    print("adolescente")
elif ed_persona >= 18 and ed_persona <= 59 :
    print ("adulto")
elif ed_persona > 60:
    print("adulto mayor")
else:
    print("revisa por que tu edad no es valida") # en caso de ingreso de numeros negativos u ingreso de otros

# 7. Pide un número del 1 al 7 y muestra el día de la semana correspondiente.

String_number_Day = input("por favor, ingresa el dia de la semana como numero: ")
number_day =int(String_number_Day) 

if number_day == 1:
    print( "Lunes")
elif number_day == 2:
    print("Martes")
elif number_day == 3:
    print("Miercoles")
elif number_day == 4:
    print("Jueves")
elif number_day == 5:
    print("Viernes")
elif number_day == 6:
    print("Sabado")
elif number_day == 7:
    print("Domingo")
else:
    print("revisa que tu numero este entre 1 y 7") # Para manejar el error

# 8.  Pide una calificación del 0 al 5. Si es 5, “Excelente”, si 4, “Muy bien”, si 3, “Bien”, si menos, “Mejorable”.

string_calificacion =input("Ingresa la calificacion de 0 a 5: ")
calificacion = int(string_calificacion)

if calificacion == 5:
    print ("excelente")
elif calificacion == 4:
    print("muy Bien")
elif calificacion == 3:
    print("Bien")
elif calificacion < 3:
    print("mejorable")
else:
    print("revisa la calificacion ingresada")


# 9. Pide dos números. Si ambos son pares, muestra “Ambos son pares”; si uno lo es, “Uno es par”; si ninguno, “Ninguno es par”.

string_number1= input("Por favor ingresa el primer numero: ")
string_number2= input("Por favor ingresa el segundo numero: ")

number1 = int(string_number1)
number2 = int(string_number2)

if number1 % 2 == 0 and number2 % 2 == 0:
    print("Ambos son pares")
elif number1 % 2 != 0 and number2 % 2 != 0:
    print("Ninguno es par")
else:
    print("Uno es par")

# 10. Crea un programa que reciba un número y diga si es par o impar.

string_N = input ("ingresa un numero por favor: ")
n = int(string_N)

if n % 2 == 0:
    print( "el numero es par")
else:
    print("El numero es impar")