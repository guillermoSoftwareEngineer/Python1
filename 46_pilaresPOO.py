
"""
LOS 4 PILARES DE LA POO:
1. Abstraccion     - Simplificar un concepto del mundo real.
2. Encapsulamiento - Proteger los datos internos.
3. Herencia        - Reutilizar y extender funcionalidad.
4. Polimorfismo    - Mismo metodo, diferentes comportamientos.
"""

#    1. ABSTRACCION   
# La clase Animal representa un concepto general, 
# con solo los atributos/metodos esenciales.
class Animal:
     
    def __init__(self, nombre): #    2. ENCAPSULAMIENTO  
        self.__nombre = nombre  # Usamos __ para encapsular el nombre.

                              #    4. POLIMORFISMO (metodo base)  
    def hacer_sonido(self):   # metodo que las subclases pueden redefinir.
        return "Sonido genérico"

    # metodo comun que usa el atributo encapsulado.
    def decir_nombre(self):
        return f"Mi nombre es {self.__nombre}"

#    3. HERENCIA   
# Perro ES UN Animal (hereda atributos y metodos).
class Perro(Animal): #usar la superclase o clase padre como parametro en la clase hija para que herede
   
    def hacer_sonido(self):  # Redefinimos el metodo para cambiar el comportamiento (POLIMORFISMO).
        return " Guau "      # es el mismo metodo pero cambia el return (comportamiento cambia)

class Gato(Animal):
    def hacer_sonido(self):
        return " Miau "

#     USO    
if __name__ == "__main__": # definimos nuevos objetos, no clases objetos
    # Creamos un Perro (que ES UN Animal).
    mi_perro = Perro("Dinno")
    mi_gato = Gato("Queen")

    # Llamamos a los metodos
    print(mi_perro.hacer_sonido())  
    print(mi_gato.hacer_sonido())   

    # Accedemos al metodo comun heredado.
    print(mi_perro.decir_nombre())  