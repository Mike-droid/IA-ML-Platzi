import random


def busqueda_lineal(lista,objetivo):
    match=False

    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break
    
    return match


if __name__ == "__main__":
    tamano_lista = int(input('¿De qué tamaño será la lista?: '))
    objetivo = int(input('¿Qué número quieres encontrar?; '))

    lista = [random.randint(0,100) for i in range(tamano_lista)]
    encontrado = busqueda_lineal(lista,objetivo)
    print(lista)
    #!Operador terniario dentro del print 😮
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')