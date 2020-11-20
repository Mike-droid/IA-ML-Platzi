from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show #!El entorno virtual debe estar encendido para que funcionar y usar numpy -v 1.19.3

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for i in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def graficar_pasos(x_valores, y_valores):
    fig = figure(title='Caminos aleatorios')
    fig.line(x_valores, y_valores)
    show(fig)


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='Miguel')
    origen = Coordenada(0,0)
    distancias = []

    for _ in range(numero_de_intentos): #!Ese guión bajo significa que no vamos a utilziar la variable
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1)) #!No tendrá decimal con round 1

    return distancias


def graficar(x,y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos',y_axis_label='distancia')
    grafica.line(x,y, legend_label='distancia media')
    print('Graficando...')
    show(grafica)


def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []

    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias)/len(distancias),4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media) #!Esto nos dará nuestras coordenadas en Y
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Máxima= {distancia_maxima}')
        print(f'Mínima = {distancia_minima}')
    graficar(distancias_de_caminata, distancias_media_por_caminata)


if __name__ == "__main__":
    distancias_de_caminata = [10,100,1000,10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)