#Definición
class Persona:
    def __init__(self,nombre,edad): #Método constructor
        self.nombre = nombre
        self.edad = edad
        #self es una referencia a esa misma clase, es un apuntador
    
    
    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre} y tengo {self.edad} años.'


#Uso
david = Persona('David',35)
miguel = Persona('Miguel',21)

print(david.saluda(miguel))
print(miguel.saluda(david))