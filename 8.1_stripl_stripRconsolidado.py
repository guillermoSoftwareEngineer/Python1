# lstrip() y rstrip()
# Regla: no modificar el texto original, solo aplicar métodos

# Ejercicio 1
texto = "   Python"
# Elimina SOLO los espacios del inicio e imprime el resultado
print(len(texto))
print(texto.lstrip())
print(len(texto.lstrip()))

# Ejercicio 2
texto = "Python   "
# Elimina SOLO los espacios del final e imprime el resultado
print(len(texto))
print(texto.rstrip())
print(len(texto.rstrip()))

# Ejercicio 3
texto = "   Python   "
# Elimina SOLO los espacios del inicio
# Imprime el resultado y luego su longitud

print(texto.lstrip())
print(len(texto.lstrip()))


# Ejercicio 4
texto = "   Python   "
# Elimina SOLO los espacios del final
# Imprime el resultado y luego su longitud
print(texto.rstrip()) 
print(len(texto.rstrip()))

# Ejercicio 5
texto = "   PYTHON   "
# Elimina espacios del inicio, convierte a minúsculas
# Cuenta cuántas veces aparece "python"
print(texto.lstrip().lower().count("python"))


# Ejercicio 6
texto = "ERROR error   "
# Elimina SOLO los espacios del final
# Convierte a minúsculas y cuenta "error"
print(texto.rstrip().lower().count("error"))


# Ejercicio 7
texto = "   aprender python es clave"
# Elimina SOLO los espacios del inicio
# Usa find() para buscar "python"
print(texto.lstrip().find("python"))


# Ejercicio 8
texto = "python es poderoso   "
# Elimina SOLO los espacios del final
# Usa len() para mostrar la longitud final
print(len(texto.rstrip()))


# Ejercicio 9
texto = "   hola hola hola   "
# Elimina SOLO los espacios del inicio
# Cuenta cuántas veces aparece "hola"
print(texto.lstrip().count("hola"))


# Ejercicio 10 (clave)
texto = "   hola   mundo   "
# Aplica lstrip() y luego rstrip()
# Imprime el resultado
# (piensa: ¿equivale a strip()?)
print(texto.lstrip().rstrip())
# equivalle a strip totalmente ya que este ultimo elimina los espacios adicionales tanto al inicio como al 
# final 