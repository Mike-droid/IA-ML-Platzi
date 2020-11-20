class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    
    @property #!decoradores
    def region(self):
        return self._region

    
    @region.setter
    def set_region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no es válida en {self.pais}')


casilla = CasillaDeVotacion(123,['Ciudad de México','Morelos'])
print(casilla.region)
casilla.region = 'Morelos'
print(casilla.region)