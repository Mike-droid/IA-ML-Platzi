class Terrestre:

    def desplazar(self):
        print('El animal anda')


class Acuatico:

    def desplazar(self):
        print('El animal nada')


class Cocodrilo(Terrestre, Acuatico):
    """Abstracción de cocodrilo. Herencia multiple.
    
    Como Terrestre se encuentra más a la izquierda,
    sería la definición de desplazar de esta clase la
    que prevalecería.
    """
    pass