import random


def busqueda_binaria(lista,comienzo,final,objetivo):
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}')
    if comienzo > final:
        return False

    medio = (comienzo + final)//2 #! //2 división de enteros entre 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


if __name__ == "__main__":
    tamano_lista = int(input('¿De qué tamaño será la lista?: '))
    objetivo = int(input('¿Qué número quieres encontrar?: '))

    lista = sorted([random.randint(0,100) for i in range(tamano_lista)])
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    #!Operador terniario dentro del print 😮
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')