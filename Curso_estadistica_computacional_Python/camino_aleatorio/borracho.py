import random

class Borracho:
    def __init__(self,nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho): #!Hereda de la clase Borracho
    def __init__(self,nombre):
        super().__init__(nombre)


    def camina(self):
        return random.choice([(0,-1),
                            (-1,0),
                            (1,0),
                            (0,1)])
                            #!coordenadas x,y = abajo, izquierda, derecha, arriba