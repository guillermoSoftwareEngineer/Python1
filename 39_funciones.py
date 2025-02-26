# definicion de la function

def saludo(nombre,apellido): # uso de parametros
    print("Hola",nombre, apellido) #lo que se hace con los datos


# el codigo es reutilizable usando nuevos parametros

saludo('Guillermo','Vasquez') #Llamado a la funcion con nuevos parametros
saludo('Homero','Simpson') #Llamado a la funcion con nuevos parametros
saludo('Rick','Sanchez') #Llamado a la funcion con nuevos parametros


#  Se puede poner un valor por defecto para que la funcion si no lo recibe renderize un valor diferente

def suma (num1,num2 = 0): #Si num2 no existe por defecto sera 0
    result = num1 + num2
    print(result)

suma(3,5) # debe renderizar 8
suma(7) # debe renderizar 7, ya que el segundo parametro es por defecto 0

# se puede invertir el orden de llamados de parametros ajustandolos en el llamado a la funcion

suma(num2= 33, num1 = 22)
saludo(apellido='Jordan',nombre= 'Michael')