'''los metodos dunder viene por defecto, a veces tambien se llaman metodos magicos,
 y se crean autamaticamente al crear, cualquier clase, siempre inician y terminan con 2 guiones
 bajos como __init__'''



 # 1. __init__ - Metodo constructor que inicializa el objeto
print('Uso de __init__, creacion de self para mostrar metodos')

class Persona:
    def __init__(self, nombre, edad):
        # self es la instancia de la clase
        # Asigna valores a los atributos del objeto
        self.nombre = nombre
        self.edad = edad

p = Persona('Juan', 30)  # Llama automaticamente a __init__




# 2. __str__ - Define como se muestra el objeto como string
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        # Esto crea la version "texto" del objeto
        # que se usará cuando se imprima o convierta a string
        return f'Nombre: {self.nombre}, Edad: {self.edad}'

# Creación del objeto
p = Persona("Laura", 32)

# Cuando imprimes el objeto, Python usa __str__
print(p)  # Muestra: Nombre: Laura, Edad: 32

# Si conviertes el objeto a string también usa __str__
texto_del_objeto = str(p)
print(texto_del_objeto)  # Muestra: Nombre: Laura, Edad: 32





# 3. __repr__ - Representacion tecnica para debugging
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __repr__(self):
        # String que permitiria recrear el objeto
        return f'Persona(nombre="{self.nombre}", edad={self.edad})'

p = Persona('Luis', 35)
print(repr(p))  # Output: Persona(nombre="Luis", edad=35)

# __repr__ retorna las instancias que pertenecen a ese objeto, en este caso:
# solo hay dos instancias, nombre y edad




# 4. __len__ - Comportamiento para la funcion len()
class Coleccion:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        # Devuelve entero representando el tamano
        return len(self.items)

col = Coleccion([1, 2, 3, 4])
print(len(col))  # Output: 4




# 5. __getitem__ - Permite acceso a elementos con []
# es practicamente como si lo convirtiera en un array del 
# que se puede obtener cada elemento (metodo interno)
class Coleccion:
    def __init__(self, items):
        self.items = items
    
    def __getitem__(self, indice):
        # Devuelve el elemento en la posicion indicada
        return self.items[indice]

col = Coleccion(['a', 'b', 'c'])
print(col[1])  # Output: b