class Autor:

    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.edad=edad


class Libro:

    def __init__(self, titulo,paginas,autor_nombre):
        self.titulo=titulo
        self.paginas=paginas
        self.autor_nombre=autor_nombre


if __name__ == "__main__":
    james_clear = Autor('James Clear',33)
    atomic_habits = Libro('Atomic Habits',300,james_clear.nombre)
    print(f'Autor: {james_clear.nombre}')
    print(f'Libro: {atomic_habits.titulo}, autor: {atomic_habits.autor_nombre}')