# los diccionarios almacenan clave: valor

auto = {"marca": "ferrari", "motor": "v8", "cantidad": 1, "color": "rojo"}
print(auto)
print(auto["color"])#se puede acceder al valor de cad propiedad mediante su clave

# se puede usar del para eliminar una clave de el diccionario
print(auto)

del(auto["motor"])

print(auto) # ya no aparece la clave motor al imprimir