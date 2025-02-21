# recolectar datos de usuario o ingresadoos por el ususario
#retornar informacion al usuario

deporte = input ("Que deporte te gusta practicar:") # La funcion input solo recibe strings
print("te gusta practicar " + deporte)

# para uar un numero se debe hacer casting

year = input("Que año es actualmente: ")
print(year)

print("La variable 'year' es de tipo " + str(type(year))) # print solo permite datos tipo string
# se debe hacer casting del string tambien 

# Para transformarla en número se debe hacer casting
numberType = int(year)
tipoNumero = type(numberType)

print("Después de hacer casting, el tipo de 'numberType' es " + str(tipoNumero))
