# Explicación basica del juego
print("Juego Piedra, Papel o Tijera para dos jugadores")

# Saber el nombre de los jugadores lo hace mas personal
jugador1 = input("Escribe tu nombre jugador 1: ")
print("El nombre del jugador 1 es: " + jugador1)

jugador2 = input("Escribe tu nombre jugador 2: ")
print("El nombre del jugador 2 es: " + jugador2)

# Diccionario para traducir numeros a texto
opciones_texto = {1: "piedra", 2: "papel", 3: "tijera"}

# Selección del jugador 2
opcion_jug2 = int(input(jugador2 + " selecciona el numero de la opcion que deseas escoger 1.Piedra 2.Papel 3.Tijeras: "))

if opcion_jug2 in opciones_texto:
    print(jugador2 + " seleccionaste la opcion " + opciones_texto[opcion_jug2]())
else:
    print("opcion inválida. Debes escoger 1, 2 o 3.")
    print("vuelve a comenzar")

# Selección del jugador 1
opcion_jug1 = int(input(jugador1 + " selecciona el numero de la opcion que deseas escoger 1.Piedra 2.Papel 3.Tijeras: "))

if opcion_jug1 in opciones_texto:
    print(jugador1 + " seleccionaste la opcion " + opciones_texto[opcion_jug1]())
else:
    print("opcion inválida. Debes escoger 1, 2 o 3.")
    print("vuelve a comenzar")

# Almacenar nombres de las selecciones
eleccion_jug1 = opciones_texto[opcion_jug1]
eleccion_jug2 = opciones_texto[opcion_jug2]

#  jug1      jug2
# piedra    piedra
# 	        papel
# 	        tijera

# papel     papel
# 	        piedra
# 	        tijera

# tijera    tijera
# 	        piedra
# 	        papel	

# Clasificación de estados 
if opcion_jug2 == 1:  # Jugador 2 elige Piedra
    if opcion_jug1 == 1:
        print("El jugador " + jugador1 + " seleccionó " + eleccion_jug1 + " y el jugador " + jugador2 + " seleccionó " + eleccion_jug2)
        print(eleccion_jug1 + " y " + eleccion_jug2 + " son iguales, entonces empate")
    elif opcion_jug1 == 2:
        print("El jugador " + jugador1 + " seleccionó " + eleccion_jug1 + " y el jugador " + jugador2 + " seleccionó " + eleccion_jug2)
        print(eleccion_jug1 + " cubre " + eleccion_jug2 + ", gana " + jugador1)
    elif opcion_jug1 == 3:
        print("El jugador " + jugador1 + " seleccionó " + eleccion_jug1 + " y el jugador " + jugador2 + " seleccionó " + eleccion_jug2)
        print(eleccion_jug2 + " rompe " + eleccion_jug1 + ", gana " + jugador2)

elif opcion_jug2 == 2:  # Jugador 2 elige Papel
    if opcion_jug1 == 1:
        print("El jugador " + jugador1 + " seleccionó " + eleccion_jug1 + " y el jugador " + jugador2 + " seleccionó " + eleccion_jug2)
        print(eleccion_jug2 + " cubre " + eleccion_jug1 + ", gana " + jugador2)
    elif opcion_jug1 == 2:
        print("El jugador " + jugador1 + " seleccionó " + eleccion_jug1 + " y el jugador " + jugador2 + " seleccionó " + eleccion_jug2)
        print(eleccion_jug1 + " y " + eleccion_jug2 + " son iguales, entonces empate")
    elif opcion_jug1 == 3:
        print("El jugador " + jugador1 + " seleccionó " + eleccion_jug1 + " y el jugador " + jugador2 + " seleccionó " + eleccion_jug2)
        print(eleccion_jug1 + " corta " + eleccion_jug2 + ", gana " + jugador1)

elif opcion_jug2 == 3:  # Jugador 2 elige Tijera
    if opcion_jug1 == 1:
        print("El jugador " + jugador1 + " seleccionó " + eleccion_jug1 + " y el jugador " + jugador2 + " seleccionó " + eleccion_jug2)
        print(eleccion_jug1 + " rompe " + eleccion_jug2 + ", gana " + jugador1)
    elif opcion_jug1 == 2:
        print("El jugador " + jugador1 + " seleccionó " + eleccion_jug1 + " y el jugador " + jugador2 + " seleccionó " + eleccion_jug2)
        print(eleccion_jug2 + " corta " + eleccion_jug1 + ", gana " + jugador2)
    elif opcion_jug1 == 3:
        print("El jugador " + jugador1 + " seleccionó " + eleccion_jug1 + " y el jugador " + jugador2 + " seleccionó " + eleccion_jug2)
        print(eleccion_jug1 + " y " + eleccion_jug2 + " son iguales, entonces empate")
