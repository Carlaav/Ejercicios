from enum import Enum
class zoo:
      cuidadores=[]
      animales=[]
      stock=stock
class vacaciones:
      def __init__(self,inicio,duracion,empleado):
            self.vacacionero=empleado
            self.inicio=inicio
            self.duracion=duracion
class cuidadores:       
    def __init__(self,nombre,apellido,animales,inicio,duracion):
        self.nombre=nombre
        self.apellido=apellido
        self.animales=animales
        self.descanso=vacaciones(inicio,duracion)
class stock:
      suministros={}
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
      carnivoro=carnivoro.tipo()
      herviboro=herbivoro.tipo()
      insectivoro=insectivoro.tipo()   
class animales:
    def __init__(self,especie,tipo_comida,numero,cuidador):
        self.id= numero 
        self.especie= especie
        self.alimentacion=dieta[tipo_comida].name
        self.encargado=cuidador

      
