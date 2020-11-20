class Lavadora:
    
    def __init__(self):
        pass


    def lavar(self, temperatura='caliente',jabon='ariel',ropa='playeras'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon(jabon)
        self._lavar(ropa)
        self._centrifugar(ropa) #!Métodos privados ¿?

    
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua a temperatura {temperatura}')
    

    def _anadir_jabon(self,jabon):
        print(f'Añadiendo jabón marca {jabon}')

    
    def _lavar(self,ropa):
        print(f'Lavando {ropa}')

    
    def _centrifugar(self,ropa):
        print(f'Centrifugando {ropa}')


if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()