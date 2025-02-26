
#FUNCION LAMBDA
# Es una forma mas sencilla y con menos codigo de ejecutar una funcion
# sirve para funciones pequeñas y rapidas

# Normalmente, la funcion seria asi:

def sumar(a, b):
    return a + b

# con lambda se puede expresar en una sola linea, es algo como las arrow function de javaScript

sumar = lambda a, b: a + b

# su uso seria:
resultado = sumar(3, 5)
print(resultado)  


# otro ejemplo 
multiplicar_por_dos = lambda x: x * 2
print(multiplicar_por_dos(5)) 


