import datetime
from Comunidad.base import Session, engine, Base
from sqlalchemy import Column, Integer, String

class Persona:

   def __init__(self, nombre, edad):
       self.__nombre = nombre
       self.__edad = edad


   def asignar_edad(self, edad):
       self.__edad = edad
       self.edad2 = edad

   def asignar_nombre(self, nombre):
       self.__nombre = nombre

   def dar_edad(self):
       return(self.__edad)

   def dar_nombre(self):
       return(self.__nombre)

   def calcular_anio_nacimiento(self, ya_cumplio_anios):
       anio_actual = datetime.datetime.now().year
       anio_2 = 0
       anio_3 = 0
       anio_4 = 0
       anio_5 = 0
       anio_6 = 0
       anio_7 = 0
       anio_8 = 0
       anio_9 = 0
       anio_10 = 0
       anio_11 = 0
       if ya_cumplio_anios:
           return (anio_actual - self.__edad)
       else:
           return (anio_actual - self.__edad + 1)