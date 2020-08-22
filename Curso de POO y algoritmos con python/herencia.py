class Rectangulo:
    
    def __init__(self, base,altura):
        self.base = base
        self.altura = altura

    
    def area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo): #Aquí le decimos que hereda de la clase rectángulo
    
    def __init__(self, lado):
        super().__init__(lado, lado)
    

if __name__ == "__main__":
    rectangulo = Rectangulo(3,4)
    print(f'El área del rectangulo con base {rectangulo.base} y altura {rectangulo.altura} es {rectangulo.area()}')

    cuadrado = Cuadrado(5)
    print(f'El área del cuadrado con sus lados de tamaño {cuadrado.base} es {cuadrado.area()}')
                                                        #Da igual si uso base o altura, debido a que es un cuadrado