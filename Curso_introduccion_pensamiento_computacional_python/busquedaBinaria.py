objetivo = int(input('Escoge un número: '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo) #!Si el objetivo > 1.0 vamos a empezar en 1.0
respuesta = (alto+bajo)/2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'Bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2<objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    
    respuesta = (alto+bajo)/2

print(f'La raíz cuadrada de {objetivo} es {respuesta}')