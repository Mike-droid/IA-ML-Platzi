objetivo = int(input('Escoge un número: '))
epsilon = 0.01 #!Qué tan cerca queremos llegar de la respueta
paso = epsilon**2 #!Qué tanto nos vamos a ir acercando por iteración a la respuesta
respuesta = 0.0
iterador = 0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    #print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso #!En cada iteración le sumamos el paso a la respuesta
    iterador += 1


if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raíz cuadrada de {objetivo}')
else:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
print(f"Valor de iterador: {iterador}")