from enum import Enum
class zoo:
      cuidadores=[]
      animales=[]
      stock={}

      @staticmethod
      def asignar_cuidador(cuidador,animal):
            cuidador = cuidadores.__init__(cuidador)
            animal = animales.__init__(animal)
            animal.encargado= cuidador

      @staticmethod
      def dar_vacaciones(solicitud):
            if solicitud:
                  cuidadores.descanso=solicitud
            else:
                  pass

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
            self.descanso=vacaciones(inicio,duracion,vacaciones.vacacionero)

      @staticmethod
      def solicitar_vacaciones(inicio,duracion,empleado):
            solicitud = (inicio,duracion,empleado)
            return solicitud

class stock:
      suministros={}

      def esta_vacio(self, suministros):
            if suministros:
                  pass
            else:
                  raise Exception("No hay stock")
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
      carnivoro=carnivoro.__init__(Enum)
      herviboro=herbivoro.__init__(Enum)
      insectivoro=insectivoro.__init__(Enum)
class animales:
      def __init__(self,especie,tipo_comida,numero,cuidador):
            self.id= numero
            self.especie= especie
            self.alimentacion=dieta[tipo_comida].name
            self.encargado=cuidador


