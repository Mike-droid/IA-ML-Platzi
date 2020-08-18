def run(nombre):
    print(f'Tu nombre tiene {len(nombre)} caracteres (contando espacios)')


if __name__ == "__main__":
    nombre = input('Escribe tu nombre: ')
    run(nombre)