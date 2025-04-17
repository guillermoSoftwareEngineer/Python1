# ls definicon de clases se hace con la palabra reservada "class"
# Es una buena practica poner los nombres de la clase iniciar la primera letra con mayuscula

#self es similar al this en JavaScript

class Persona:                   # Constructor (metodo especial __init__)
    def __init__(self,name,age): # el constructor se define mediante una funcion init, ademas de pasar self 
        self.name = name         # como argumento, se pasan los a definir name, y age
        self.age = age             # es decir metodo especial __init__ se usa en caso de crear atributos especializados (name, age)

    # Definicion de el Metodo
    def saludar (self):          # El metodo se define mediante una funcion y su argumento siempre debe ser self
        print(f"Hola mi nombre es {self.name} y tengo {self.age}")


# creacion de objeto basado en la clase persona

persona1 = Persona("Daniel",33) # los argumentos son el nuevo nombre y edad
persona2 = Persona("Tatiana",35) # los argumentos son el nuevo nombre y edad

#Se usa la definicion del objeto creado en base al constructor con el metodo creado

persona1.saludar()
persona2.saludar()
