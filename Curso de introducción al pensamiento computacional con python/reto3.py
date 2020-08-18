epsilon = 0.01
paso = epsilon**2
respuestaAprox = 0.0


def aproximacion(objetivo,epsilon,paso,respuestaAprox):
    while abs(respuestaAprox**2 - objetivo) >= epsilon and respuestaAprox <= objetivo:
        respuestaAprox += paso

    if abs(respuestaAprox**2 - objetivo) >= epsilon:
        print(f'No se encontró la raíz cuadrada de {objetivo}')
    else:
        print(f'La raíz cuadrada de {objetivo} es {respuestaAprox}')


def busqueda_binaria(objetivo,respuestaBinaria,epsilon,bajo,alto):
    while abs(respuestaBinaria**2 - objetivo) >= epsilon:
        if respuestaBinaria**2<objetivo:
            bajo = respuestaBinaria
        else:
            alto = respuestaBinaria
    
        respuestaBinaria = (alto+bajo)/2

    print(f'La raíz cuadrada de {objetivo} es {respuestaBinaria}')


def run(opcion):
    if opcion==1:
        objetivo = int(input('Escoge un número: '))
        aproximacion(objetivo,epsilon,paso,respuestaAprox)
    elif opcion==2:
        objetivo = int(input('Escoge un número: '))
        alto = max(1.0, objetivo)
        bajo = 0.0
        respuestaBinaria = (alto+bajo)/2
        busqueda_binaria(objetivo,respuestaBinaria,epsilon,bajo,alto)
    else:
        print("Opción incorrecta")


if __name__ == "__main__":
    opcion = int(input("""
    Selecciona una opcion
    1. Aproximación
    2. Búsqueda binaria
    """))
    run(opcion)