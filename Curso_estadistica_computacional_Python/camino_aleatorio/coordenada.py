class Coordenada:
    def __init__(self,x,y): #!self es la referencia a la propia instancia
        self.x = x
        self.y = y


    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x , self.y + delta_y) #!Coordenada origial más el movimiento


    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x #!La diferencia entre ambas coordenadas X
        delta_y = self.y - otra_coordenada.y #!La diferencia entre ambas coordenadas Y

        return(delta_x**2 + delta_y**2)**0.5 #!Pitágoras, lo elevamos a la (1/2) [raíz cuadrada]