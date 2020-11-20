import random
import collections

PALOS = ['espada','corazon','rombo','trebol'] #!Convención para constantes
VALORES = ['as','2','3','4','5','6','7','8','9','10','J','Q','K']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo,valor))
    return barajas


def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano) #!random.sample tomará valores al azar SIN repetirlos
    return mano


def main(tamano_mano, intentos):
    barajas = crear_baraja()
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas , tamano_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1]) #!Obtenemos el índice 0 o 1 porque barajas.append((palo,valor)) <-- [0,1]
        counter = dict(collections.Counter(valores))
        #print(f'Valores: {valores}')
        for valor in counter.values():
            if valor == 2:
                pares += 1
                break

    probabilidad_par = pares / intentos
    #print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es de {probabilidad_par} o bien de {probabilidad_par * 100}%')
##########################################################################################################
    corrida = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[0]) #!Obtenemos el índice 0 o 1 porque barajas.append((palo,valor)) <-- [0,1]
        counter2 = dict(collections.Counter(valores))
        #print(f'Valores: {valores}')
        for valor in counter2.keys():
            if valor in valores[0] == 'espada' and valor in valores[1] == 'espada' and valor in valores[2] == 'espada' and valor in valores[3] == 'espada' and valor in valores[4] == 'espada':
                corrida += 1
                break
            if valor in valores[0] == 'trebol' and valor in valores[1] == 'trebol' and valor in valores[2] == 'trebol' and valor in valores[3] == 'trebol' and valor in valores[4] == 'trebol':
                corrida += 1
                break
            if valor in valores[0] == 'corazon' and valor in valores[1] == 'corazon' and valor in valores[2] == 'corazon' and valor in valores[3] == 'corazon' and valor in valores[4] == 'corazon':
                corrida += 1
                break
            if valor in valores[0] == 'rombo' and valor in valores[1] == 'rombo' and valor in valores[2] == 'rombo' and valor in valores[3] == 'rombo' and valor in valores[4] == 'rombo':
                corrida += 1
                break

    probabilidad_corrida = corrida / intentos
    print(f'La probabilidad de obtener una corrida en una mano de {tamano_mano} barajas es de {probabilidad_corrida} o bien de {probabilidad_corrida * 100}%')

if __name__ == "__main__":
    tamano_mano = int(input('¿De cuántas barajas será la mano?: '))
    intentos = int(input('¿Cuántos intentos para calcular la probabilidad?: '))

    main(tamano_mano,intentos)