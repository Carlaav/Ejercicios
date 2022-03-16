from enum import Enum
import time
class zoo:
      def __init__(self, cuidadores, animales):
            self.cuidadores = cuidadores
            self.animales = animales
            self.stock = stock()
          
      #Asigna a un cuidador un animal que cuidar
      def cuidar(self, cuidador, animal):
            cuidador.animales.append(animal)
      
      def cogerVacaciones(self, cuidador, inicio, duracion):
            cuidador.solicitarVacaciones(inicio, duracion)
      
class vacaciones:
      def __init__(self,inicio,duracion,empleado):
            self.vacacionero=empleado
            self.inicio=inicio
            self.duracion=duracion
            
      def verVacaciones(self):
            print("Vacaciones de", self.vacacionero, "va de", self.inicio, "hasta dentro de", self.duracion, "dias")
class cuidadores:       
      def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
        self.animales=[]
        
      def solicitarVacaciones(self, dia, duracion):
            vacaciones(dia, duracion, self)
              
      def getAnimalesCuidados(self):
            return self.animales
        
class stock:
      
      suministros={}
      
      def sacar(self, comida, cantidad):
            if comida in self.suministros.keys():
                  if self.suministros[comida] - cantidad > 0:
                        self.suministros[comida] = self.suministros[comida] - cantidad
                  else:
                        print("No es posible sacar esa cantidad de comida")
            else:
                  print("No queda de esa comida posible")


class comida:
      food=[]
class carnivoro:
      def __init__(self):
        self.tipo="carnivoro"
class herbivoro:
       def __init__(self):
            self.tipo="herbivoro"
class insectivoro:
       def __init__(self):
            self.tipo="insectivoro" 
class dieta(Enum):
      carn=carnivoro().tipo
      herv=herbivoro().tipo
      insec=insectivoro().tipo   
class animales:
    def __init__(self,especie,tipo_comida,numero,cuidador):
        self.id= numero 
        self.especie= especie
        self.alimentacion=dieta[tipo_comida].name
        self.encargado=cuidador
        

lista_Cuidadores = [cuidadores("Pepe", "Rodriguez"), cuidadores("Carla", "Tzi")]
lista_animales = [animales("Gato", dieta["carn"].name, 1, lista_Cuidadores[0])]

miZoo = zoo(lista_Cuidadores, lista_animales)