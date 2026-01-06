# Método strip()
# Contexto 

# En texto real, los espacios sobrantes rompen comparaciones, conteos y búsquedas.
# strip() NO cambia el contenido, solo elimina espacios al inicio y al final del texto.

# Regla clave:
# strip() no toca espacios internos.

# EJERCICIOS

# Ejercicio 1
texto = "   Python   "
# Elimina los espacios exteriores e imprime el resultado
print(texto.strip())


# Ejercicio 2
texto = "   Python   "
# Elimina los espacios exteriores y muestra la longitud final
print(len(texto.strip()))


# Ejercicio 3
texto = "   PYTHON   "
# Elimina espacios, convierte a minúsculas y cuenta cuántas veces aparece "python"
print(texto.strip().lower().count("python"))

# Ejercicio 4
texto = "   aprender python   "
# Elimina espacios y usa find() para buscar "python"
print(texto.strip().find("python"))


# Ejercicio 5
texto = "   hola hola   "
# Elimina espacios y cuenta cuántas veces aparece "hola"
print(texto.strip().count("hola"))

# Ejercicio 6
texto = "   ERROR error Error   "
# Elimina espacios, convierte a minúsculas y cuenta "error"
print(texto.strip().lower().count("error"))


# Ejercicio 7
texto = "   Python es poderoso   "
# Elimina espacios y muestra la longitud del texto
print(len(texto.strip()))


# Ejercicio 8
texto = "   PYTHON   PYTHON   "
# Elimina espacios exteriores y cuenta cuántas veces aparece "PYTHON"
# (piensa si necesitas convertir mayúsculas o no)

print(texto.strip().count("PYTHON")) #.strip() solo elimina caracteres 
# al inicio y al final de la cadena. No mira lo que sucede en la mitad del texto.


# Ejercicio 9
texto = "   slicing y strip   "
# Elimina espacios y cuenta cuántos espacios internos hay
print(texto.strip().count(" "))


# Ejercicio 10
texto = "   Python   "
# Elimina espacios y convierte todo a MAYÚSCULAS
print(texto.strip().upper())


# EJERCICIOS CONSOLIDACION 
print("***************************************")

# MICRO-BLOQUE — ERRORES COMUNES CON strip()

# Ejercicio 1
texto = "hola   mundo"
# Usa strip() y cuenta cuántos espacios hay
# ¿El resultado cambia respecto a no usar strip()?
print(texto.count(" "))
print(texto.strip().count(" "))
# el resultado es el mismo por que strip solo elimina los espacios al principio y al final de la cadena
# y ya que no hay espacios al principio y al final en el texto original el resultado es el mismo 



# Ejercicio 2
texto = "   hola   mundo   "
# Usa strip() y cuenta cuántos espacios hay
# Explica (en comentario) qué espacios se eliminaron
print(texto.strip().count(" "))
#el resultado es 3 por que se eliminaron al principio y al final al usar strip()
# ya que el ceentro contiene 3 espacios strip() no actua sobre ellos


# Ejercicio 3
texto = "   python   python   "
# Usa strip() y count() para contar "python"
# ¿El resultado es 1 o 2? ¿por qué?
print(texto.strip().count("python"))
#El resultado es 2, por que strip no elimina caracteres solo espacios al principio o final
# del string 

# Ejercicio 4
texto = "error   error"
# Usa strip() y count() para contar "error"
# ¿strip() ayuda en este caso?
print(texto.strip().count("error"))
# strip() borra espacios al princicio y final ya que el string tiene 2 veces la palabra "error"
# count() cuenta las 2 palabras strip() solo serviria para normalizar


# Ejercicio 5
texto = "   ERROR   error   "
# Usa strip() y count("error")
# ¿Por qué el resultado NO es el esperado?
print(texto.strip().count("error"))
#posiblemente el resultado no sea el esperado por que la IA que pone los ejercicios espera un resultado de 2
# aun sin explicarlo en el enunciado, lo mas probable es que creyera que para normalizar, tambien debia usar
# lower()


# Ejercicio 6
texto = "   Python es poderoso   "
# Usa strip() y find("poderoso")
# ¿Cambia el índice respecto a no usar strip()?
print(texto.strip().find("poderoso"))
# Si claro que cambia el indice ya que al usar strip cambiamos la cantidad de caracteres en el string
#  y el espacio tambien es un caracter segun el codigo ASCII

# Ejercicio 7
texto = "hola-mundo"
# Usa strip() y count("hola")
# ¿Tiene algún efecto strip() aquí?
print(texto.strip().count("hola"))
#no tiene ningun efecto ya que el string original no tiene espacios ni al principio ni al final
# entonces al aplicar el metodo strip() no estamos haciendo nada


# Ejercicio 8
texto = "   hola hola hola   "
# Usa strip() y count("hola")
# ¿Por qué aquí strip() sí es útil?
print(texto.strip().count("hola"))

#strip()si esta eliminando los espacios al principio y al final que son inecesarios


# Ejercicio 9
texto = "   PYTHON python Python   "
# Usa strip(), lower() y count("python")
# ¿Por qué el ORDEN de los métodos importa?
print(texto.strip().lower().count("python"))

# importa por que si uso count antes de lower, count solo encontrara una coincidencia
# pero si uso primero lower abra dos coincidencias mas, ya que lower() pone todo en minuscula


# Ejercicio 10 (clave)
texto = "   hola   mundo   "
# Usa strip() y len()
# Luego comenta:
# ¿strip() limpia el texto o solo los bordes?
print(len(texto.strip()))

# strip() limpia solo los bordes. Si en el centro hay 3 espacios estos seguiran siendo tres
