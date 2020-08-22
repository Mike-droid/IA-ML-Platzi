class Automovil:
    
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo' #variable privada
        self._motor = Motor(cilindros=4) #variable privada

    
    def acelerar(self, tipo='despacio'):
        if tipo=='rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        

        self._estado = 'en_movimiento'
        self._estadoLlanta = 'girando'
        self._temperatura = 10


class Motor:

    def __init__(self, cilindros, tipo='gasolina'): #default value
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    
    def inyecta_gasolina(self, cantidad):
        cantidad+=cantidad


class Llantas:

    def __init__(self, rines):
        self.rines = 'metálicos'
        self._estadoLlanta = 'reposo'


class Radio:

    def __init__(self, estacion ,isON=False):
        self.estacion = estacion

    
    def enciendeRadio(self):
        if isON==False:
            isOn = True
            self.estacion = float.input('Escribe la estación que quieres escuchar: ')