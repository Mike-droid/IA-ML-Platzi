# x,y path for drunk walking
path_x = [0]
path_y = [0]

class Campo:
    def __init__(self):
        self.coordenadas_de_borrachos = {} #!Empezamos con un diccionario vacío


    def anadir_borracho(self,borracho,coordenada): #!Qué borracho lo queremos añadir dónde
        self.coordenadas_de_borrachos[borracho] = coordenada #! Key: borracho, Value: valor de coordenada


    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        path_x.append(path_x[-1] + delta_x)
        path_y.append(path_y[-1] + delta_y)
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x,delta_y)
        self.coordenadas_de_borrachos[borracho] = nueva_coordenada


    def obtener_coordenada(self,borracho):
        return self.coordenadas_de_borrachos[borracho]