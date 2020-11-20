def run(nombre1,edad1,nombre2,edad2):
    if edad1>edad2:
        print(f'{nombre1} es mayor que {nombre2}')
    elif edad1<edad2:
        print(f'{nombre2} es mayor que {nombre1}')
    else:
        print(f'{nombre1} y {nombre2} tienen la misma edad')


if __name__ == "__main__":
    nombre1 = input("¿Cuál es el nombre de la primera persona?: ")
    edad1 = int(input("¿Cuál es la edad de la primera persona?: "))
    nombre2 = input("¿Cuál es el nombre de la segunda persona?: ")
    edad2 = int(input("¿Cuál es la edad de la segunda persona?: "))
    run(nombre1,edad1,nombre2,edad2)