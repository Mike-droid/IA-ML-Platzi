import random
import math

def media(X):
    return sum(X) / len(X)


def varianza(X):
    mu = media(X)
    acumulador = 0
    for x in X:
        acumulador += (x-mu)**2
    return acumulador / len(X)


def desviacion_estandar(X):
    return math.sqrt(varianza(X))


if __name__ == "__main__":
    X = [random.randint(1,50) for i in range(30)] #*Genera números aleatorios entre X & Y, N cantidad de veces
    µ = media(X)
    sigma_cuadrado = varianza(X)
    sigma = desviacion_estandar(X)
    print(f'Valores: {X}')
    print(f'Media: {µ}')
    print(f'Varianza: {sigma_cuadrado}')
    print(f'Desviación estándar: {sigma}')