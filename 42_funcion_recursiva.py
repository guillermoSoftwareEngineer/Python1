# para hallar el factorial de 5

#   !5 = 5*4*3*2*1

# para hallar el factorial de 4

#   !4 =   4*3*2*1

# Pero el factorial de 5 tambien se puede hallar con

#           5 * !4 

#   y asi consecutivamente

#           5 * !4 
#           4 * !3 
#           3 * !2 
#           2 * !1

# esto tiene un fin o regla y es que es valido para todos los numeros mayores a 0 (caso base)

True > 0

# Es decir que en ese momento se debe detener

def factorial(n):
    if n == 0:  # Esto es el caso base
        return 1 #por que por convencion matematica !0 (factorial de 0)  es = 1
    else:
        return n * factorial(n - 1)  # Aquí la función se llama a sí misma

factorial_5 = factorial(5)
print(factorial_5)

factorial_0 = factorial(0)
print(factorial_0)

def fibonachi(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)
    

    
print(fibonachi(0))
print(fibonachi(1))
print(fibonachi(2))
print(fibonachi(3))
 
  
