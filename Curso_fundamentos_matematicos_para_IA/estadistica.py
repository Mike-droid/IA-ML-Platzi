import numpy as np
from statistics import mode,median
from collections import Counter
temperaturas = np.array([3,35,30,37,27,31,41,20,16,26,45,37,9,41,28,
                        21,31,35,10,26,11,34,36,12,22,17,33,43,19,
                        48,38,25,36,32,38,28,30,36,39,40])
valores = np.unique(temperaturas)
print(Counter(temperaturas))
print(f'Valores : {valores}')
print(f'Media: {round(temperaturas.mean(),2)}')
print(f'Moda: {mode(temperaturas)}')
print(f'Mediana: {median(temperaturas)}')
print(f'Varianza: {round(temperaturas.var(),2)}')
print(f'Ubicación del valor superior: posicion {temperaturas.argmax()} , el numero es {temperaturas[temperaturas.argmax()]}')
print(f'Ubicación del valor inferior: posicion {temperaturas.argmin()} , el numero es {temperaturas[temperaturas.argmin()]}')