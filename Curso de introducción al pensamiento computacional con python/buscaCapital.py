print('BUSCADOR DE CAPITALES')

pais  = input('\nEscribe el país al que desees conocer su capital: ')

def busca_pais(paises, pais):
    try:
        return paises[pais]
    except KeyError:
        return print('\n \nEl país que buscas, no se encuentra en la base de datos.')

paises = {
        'Colombia': 'Bogotá',
        'Uruguay': 'Montevideo',
        'España': 'Madrid',
        'Canada': 'Ottawa',
        'Argentina': 'Buenos Aires',
        'Australia': 'Canberra',
        'Bolivia': 'Sucre',
        'Brasil': 'Brasilia',
        'Chile': 'Santiago',
        'Venezuela': 'Caracas',
        'Costa Rica': 'San Jose',
        'Cuba': 'La Habana',
        'Ecuador': 'Quito',
        'Egipto': 'El Cairo',
        'Francia': 'Paris',
        'Filipinas': 'Manilla',
        'India': 'Nueva Delhi',
        'Indonesia': 'Yakarta',
        'Italia': 'Roma',
        'Libano': 'Beirut',
        'México': 'Ciudad de México'
        }

print(busca_pais(paises, pais))