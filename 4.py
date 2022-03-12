from enum import Enum


class cuidadores:       
    def __init__(self,nombre,apellido,animales):
        self.nombre=nombre
        self.apellido=apellido
        self.animales=animales

class comida:
      pass
class carnivoro(comida):
      def __init__(self,tipo):
        self.carnivoro=tipo
class herbivoro(comida):
       def __init__(self,tipo):
            self.herbivoro=tipo
class insectivoro(comida):
       def __init__(self,tipo):
            self.insectivoro=tipo      
class animales:
    def __init__(self,raza,tipo_comida,numero):
        self.id= numero 
        self.comida=comida(tipo_comida)
        self.raza= raza
class stock:
      pass
class dieta(Enum):
      carnivoro=carnivoro()
      herviboro=herbivoro()
      insectivoro=insectivoro()
