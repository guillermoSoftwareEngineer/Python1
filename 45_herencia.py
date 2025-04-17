# Una clase puede heredar el comportamiento de una clase padre

# Definicion de la clase padre

class Auto:
    def __init__(self, marca, color, modelo): # siempre init y siempre self( en caso de marca, color etc)
        self.marca = marca
        self.color = color
        self.modelo =  modelo

# definicion del metodo
    def consultar(self): # Argumento siempre self
        print(f"el auto es marca {self.marca} de color {self.color} y de modelo {self.modelo} ")

# creacion objetos en base a clase padre

auto1= Auto("ferrari","rojo",2025)
auto2= Auto("Mclaren","azul",2023)

#Ejecucion de el metodo de la clase padre

auto1.consultar()
auto2.consultar()

#ejecucion de nueva clase heredando de clase padre

class Moto(Auto): # hereda de clase auto
    # sobreescribe la definicion del metodo
    def consultar(self): # Argumento siempre self
        print(f"la moto es marca {self.marca} de color {self.color} y de modelo {self.modelo} ")

# creacion objetos en base a clase hija que  heredo de clase padre

moto1= Moto("Ducati Lenovo Team","rojo",2025) #se debe cambiar a Moto (en verde) la clase hija que hereda
moto2= Moto("Monster Energy Yamaha MotoGP","azul negro y verde",2023) #se debe cambiar a Moto (en verde) la clase hija que hereda

#Ejecucion de el metodo de la clase padre heredado por la clase hija

moto1.consultar()
moto2.consultar()