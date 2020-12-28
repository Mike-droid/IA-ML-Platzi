#álgebra lineal
import numpy as np

#definimos la mátriz y la mátriz resultado
matriz = np.array([[1,-3,2],[5,6,-1],[4,-1,3]])

matriz_resultado= np.array([[-3],[13],[8]])

#calculamos la inversa de la matriz
matriz_inv = np.linalg.inv(matriz)

#Realizamos el produto entre la matriz inversa y la matriz resultado
matriz_solucion= matriz_inv.dot(matriz_resultado)

print(f"La solución del producto entre {matriz} y que tiene como resultado {matriz_resultado} es: {matriz_solucion}")