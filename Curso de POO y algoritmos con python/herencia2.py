class Camara:

    def __init__(self, mp, marca):
        self.mp = mp
        self.marca = marca

    def toma_foto(self):
        return (f'Has tomado una foto con tu cámara de {self.marca} y tiene una resolución de {self.mp} megapixeles')


class VideoCamara(Camara):

    def __init__(self, mp,marca,fps):
        super().__init__(mp,marca)
        self.fps = fps

    
    def gragar_video(self):
        return (f'Estás grabando un vídeo a {self.fps} FPS con tu cámara {self.marca}')


if __name__ == "__main__":
    camara_sony = Camara(23,'Sony')
    print(camara_sony.toma_foto())

    camara_red = VideoCamara(45,'Red',24)
    print(camara_red.gragar_video())