class Coordenada:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def distancia(self, otra_coordenada): #otra coordenada es otra instancia de la coordenada
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return(x_diff + y_diff)**0.5 #Elevar algo a la 1/2 ó 0.5 es lo mismo que sacar raíz cuadrada


if __name__ == "__main__": # <----Si este archivo lo ejecutamos desde la terminal 
    coord_1 = Coordenada(3,30)
    coord_2 = Coordenada(4,8)

    print(f'La distancia entre coordenada 1 y coordenada 2 es de {coord_1.distancia(coord_2)} metros')
    #print(isinstance(coord_2,Coordenada))