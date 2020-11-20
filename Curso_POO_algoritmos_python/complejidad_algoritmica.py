import time
import sys

def factorial(n):
    respuesta = 1

    while n>1:
        respuesta *= n
        n -= 1
    
    return respuesta


def factorial_r(n):
    if n==1:
        return 1
    
    return n*factorial_r(n-1)


if __name__ == "__main__":
    n = 999
    sys.setrecursionlimit(n+10)

    comienzo = time.time()
    #print(f'Factorial de {n} es {factorial(n)}')
    factorial(n)
    final = time.time()
    print(f'Final - comienzo (normal) = {final - comienzo}')

    comienzo = time.time()
    #print(f'Factorial recursivo de {n} es {factorial_r(n)}')
    factorial_r(n)
    final = time.time()
    print(f'Final - comienzo (recursivo) = {final - comienzo}')