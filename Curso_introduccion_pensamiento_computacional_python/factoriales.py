#import sys
#sys.setrecursionlimit(1010)
#!Las 2 líneas de arriba son para establecer el límite de recursividad que hará python, por defecto es 1000

def factorial(n):
    """
    Calcula el factorial de n

    n int > 0

    returns n!
    """
    if n==1:
        return 1
    
    return n * factorial(n-1)

n = int(input('Escribe un entero: '))

print(factorial(n))