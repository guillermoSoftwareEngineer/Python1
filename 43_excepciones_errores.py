# Try except 
# La idea de esto es mandar mensajes de informacion para que se comprenda cual es la causa del error 

# estructura
try:
    pass #codigo a ejecutarse
except:
    pass # mensaje o accion en caso de ejecutarse el error

# Ejercicio de division 
# segun las reglas de la matematica no se puede dividir por 0 

try:
    divisor = input("Ingresa un numero para dividir por el: ")
    dividendo = 30
    division = dividendo/divisor
except ZeroDivisionError: # se puede manejar cada tipo de error (ZeroDivisionError este caso)
    print("Oye, no se puede dividir por 0")
except ValueError: # se puede manejar cada tipo de error (ValueError)
    print("Ese no es un caracter valido, debe ser un numero")
except Exception as e:
    print("Ocurrió un error inesperado:", e) # se puede guardar la excepcion en una variable e

#las divisiones tienen jerarquia y estan definidas en un arbol, por ejemplo con una
# sola se pueden manejar todas las excepciones de geometria el arbol es asi:

# Exception
# ├── ArithmeticError
# │   ├── FloatingPointError
# │   ├── OverflowError
# │   └── ZeroDivisionError
# ├── AssertionError
# ├── AttributeError
# ├── BufferError
# ├── EOFError
# ├── ImportError
# │   ├── ModuleNotFoundError
# │   └── ZipImportError
# ├── LookupError
# │   ├── IndexError
# │   ├── KeyError
# │   └── CodecRegistryError
# ├── MemoryError
# ├── NameError
# │   └── UnboundLocalError
# ├── OSError
# │   ├── BlockingIOError
# │   ├── ChildProcessError
# │   ├── ConnectionError
# │   │   ├── BrokenPipeError
# │   │   ├── ConnectionAbortedError
# │   │   ├── ConnectionRefusedError
# │   │   └── ConnectionResetError
# │   ├── FileExistsError
# │   ├── FileNotFoundError
# │   ├── InterruptedError
# │   ├── IsADirectoryError
# │   ├── NotADirectoryError
# │   ├── PermissionError
# │   └── TimeoutError
# ├── ReferenceError
# ├── RuntimeError
# │   ├── NotImplementedError
# │   └── RecursionError
# ├── StopIteration
# ├── StopAsyncIteration
# ├── SyntaxError
# │   └── IndentationError
# │       └── TabError
# ├── SystemError
# ├── TypeError
# ├── ValueError
# │   └── UnicodeError
# │       ├── UnicodeDecodeError
# │       ├── UnicodeEncodeError
# │       └── UnicodeTranslateError
# └── Warning
#     ├── DeprecationWarning
#     ├── PendingDeprecationWarning
#     ├── RuntimeWarning
#     ├── SyntaxWarning
#     ├── UserWarning
#     ├── FutureWarning
#     ├── ImportWarning
#     ├── UnicodeWarning
#     └── ResourceWarning

