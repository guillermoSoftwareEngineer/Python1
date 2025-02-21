yo ={"nombre":"Guillermo", "apellido":"Vasquez","nacionalidad":"Colombiano"}
print(type(yo))

# saber que llaves tiene un diccionario (KEYS)

llaves=yo.keys()#deben llevar los parentesis de parametros como funciones
print(llaves)
print(type(llaves))

# saber que valores tiene un diccionario (VALUES)
valores=yo.values()#deben llevar los parentesis de parametros como funciones
print(valores)
print(type(valores))

# saber que claves y valores tiene un diccionario (ITEMS)
clave_valor=yo.items()#deben llevar los parentesis de parametros como funciones
print(clave_valor)
print(type(clave_valor))

#igual que los otros pueden haber diccionarios de diccionarios
# por ejemplo en el uso de productos, nombre, precio, color, disponibilidad,etc