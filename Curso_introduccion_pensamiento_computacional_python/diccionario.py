estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}


print("Iterar a lo largo de las llaves: ")
for pais in estudiantes:
    print(pais)


print("Iterar a lo largo de las llaves: ")
for pais in estudiantes.keys():
    print(pais)


print("Iterar a lo largo de los valores")
for numero_de_estudiantes in estudiantes.values():
    print(numero_de_estudiantes)


print("Iterar en una tupla las llaves y los valores")
for pais, numero_de_estudiantes in estudiantes.items():
    print(pais, numero_de_estudiantes)