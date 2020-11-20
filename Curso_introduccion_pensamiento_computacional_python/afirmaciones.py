#assert <expresión booleana> , <mensaje de error>

def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        if type(palabra) == bool:
            print(f'El valor booleano {palabra} no es un String')
        else:
            try:
                assert type(palabra) == str , f'{palabra} no es string'
                assert len(palabra) > 0 , 'No se permiten strings vacíos'
                primeras_letras.append(palabra[0])
            except AssertionError as e:
                print(e)

    return (primeras_letras)

mi_lista = ['hola',5.1,'',4,True,'Miguel','$10','=(1)']
print('Los caracteres válidos son: ' , primera_letra(mi_lista))