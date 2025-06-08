#  'super()' permite a una clase hija usar metodos
# y propiedades
# de su clase padre (la clase de la que hereda) y luego añadir los suyos propios.

class Animal:
    """
    Esta es la clase padre. Define las caracteristicas básicas de cualquier animal.
    """
    def __init__(self, nombre, edad): # el constructor se debe inicializar con __init__ (propiedades comunes a todos los animales)
        # El constructor de la clase Animal.
        # Aqui inicializamos las propiedades comunes a todos los animales.
        self.nombre = nombre
        self.edad = edad
        print(f"DEBUG: Inicializando un Animal: {self.nombre}, {self.edad} años.")

    def hacer_sonido(self): #Metodo basico para que el animal haga un sonido.
       
        print("El animal hace un sonido genérico.")

    def describir(self): # Metodo para describir al animal.

        return f"Soy un animal llamado {self.nombre} y tengo {self.edad} años."

class Perro(Animal):
    """
    Esta es la clase hija 'Perro', que hereda de 'Animal'.
    Un perro es un tipo de animal, pero tiene caracteristicas y comportamientos especificos.
    """
    # siempre que se usa self en un atributo es por que ese atributo es propio de esa clase
    # es decir es unico de su clase, ya se padre o clase hija y se debe pasar como argumento
    # a la def 

    def __init__(self, nombre, edad, raza):
        #   USO DE super()    
        # super().__init__(nombre, edad) llama al constructor de la clase 'Animal' (la clase padre).
        # Esto asegura que las propiedades 'nombre' y 'edad' se inicialicen correctamente
        # por la logica de la clase padre ANTES de que 'Perro' añada sus propias cosas.
        super().__init__(nombre, edad)
        
        # Después de que el padre ha hecho su parte, la clase 'Perro' añade su propiedad especifica: 'raza'.
        # Que tambien que se tuvo que pasar como argumento en def __init__(self, nombre, edad, raza) antes
        self.raza = raza
        print(f"DEBUG: Inicializando un Perro: {self.nombre}, {self.edad} años, raza {self.raza}.")

    def hacer_sonido(self):
        """
        Este Metodo 'hacer_sonido' sobreescribe el Metodo de la clase 'Animal'.
        Los perros ladran, no hacen un sonido genérico.
        """
        print("¡Guau! ¡Guau!")

    def describir(self):
        """
        Este Metodo tambien sobreescribe 'describir' para añadir información especifica del perro.
        Podemos usar super() si queremos incluir la descripción del padre.
        """
        #   USO DE super()   PARA EXTENDER UN Metodo  
        # super().describir() llama al Metodo 'describir' de la clase 'Animal'.
        # Luego, le añadimos la información especifica de la raza del perro.
        descripcion_animal = super().describir() 
        return f"{descripcion_animal} Soy un perro de raza {self.raza}."

#   Creación de objetos y demostración  

print("Demostrando la clase Animal  ")
mi_animal = Animal("Leo", 5)
print(mi_animal.describir())
mi_animal.hacer_sonido()
print("-" * 30) # lineas de separado

print("\nDemostrando la clase Perro  ")
mi_perro = Perro("Max", 3, "Golden Retriever") # Al crear el Perro, se llama al constructor de Animal y luego al de Perro
print(mi_perro.describir()) # Llama al Metodo 'describir' del Perro, que a su vez usa el de Animal
mi_perro.hacer_sonido() # Llama al Metodo 'hacer_sonido' especifico del Perro
print("-" * 30) # lineas de separado

print("\nOtro ejemplo de Perro  ")
otro_perro = Perro("Luna", 2, "Labrador")
print(otro_perro.describir())
otro_perro.hacer_sonido()
print("-" * 30) # lineas de separado





# OTRO EJEMPLO 

# Notas para una mejor comprension

# Atributos: Son variables que pertenecen a una clase o a sus objetos. Definen las propiedades de un objeto. 
# Por ejemplo, pensemos en una persona: ¿Qué caracteriza a una persona en general? Las personas tienen 
# nombre, edad, dirección, etc. En términos de POO, estos serían los atributos de la clase Person.

# Métodos: Son funciones definidas dentro de una clase que operan sobre sus objetos. Definen los comportamientos 
# de un objeto. Siguiendo con el ejemplo de una persona, ¿Qué acciones puede realizar una persona? Puede hablar, 
# caminar, comer, etc. En POO, estas acciones serían métodos de la clase Person.

# EJEMPLO CLASICO DE DEFINICION DE UNA CLASE

class Person:
    def __init__(self, name, age):
        self.name = name  # Atributo
        self.age = age    # Atributo

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años.")  # Método

# Crear una instancia de la clase Person
persona1 = Person("Ana", 30)
persona1.greet()  #   Hola, mi nombre es Ana y tengo 30 años.


# EJEMPLO DE USO DE UN CONSTRUCTOR (Con base en la clase anterior Person)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Crear una instancia de Person
person1 = Person("Ana", 30)
print(person1.name)  #   Ana
print(person1.age)   #   30


# Ejemplo de Uso de super()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello! I am a person.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hi, I'm {self.name}, and I'm a student with ID: {self.student_id}")

# Crear instancia de Student y llamar a greet

    student = Student("Ana", 20, "S12345")
    student.greet()  #   Hello! I am a person.
                 #         Hi, I'm Ana, and I'm a student with ID: S12345   