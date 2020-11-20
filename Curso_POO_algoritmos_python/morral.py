def morral(tamano_morral, pesos, valores, n):
    print('Afuera de todo')
    print(f'[Tamaño morral: {tamano_morral}]', f'[Pesos: {pesos[n-1]}]', f'[Valores: {valores[n-1]}]', f'[n: {n}]')
    if n == 0 or tamano_morral == 0:
        print('Primer if')
        print(f'[Tamaño morral: {tamano_morral}]', f'[Pesos: {pesos[n-1]}]', f'[Valores: {valores[n-1]}]', f'[n: {n}]')
        return 0
    
    if pesos[n-1]>tamano_morral:
        print('Segundo if')
        print(f'[Tamaño morral: {tamano_morral}]', f'[Pesos: {pesos[n-1]}]', f'[Valores: {valores[n-1]}]', f'[n: {n}]')
        return morral(tamano_morral,pesos,valores, n-1)

    return max(valores[n-1] + morral(tamano_morral-pesos[n-1], pesos,valores,n-1),
            morral(tamano_morral,pesos,valores,n-1))


if __name__ == "__main__":
    valores = [60,100,120] #money
    pesos = [10,20,30] #kilos
    tamano_morral = 45 #avaible space
    n = len(valores)
    
    resultado = morral(tamano_morral,pesos,valores,n)
    print(f'Valores recogidos y sumados: {resultado}')