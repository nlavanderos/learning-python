#siempre posicionar la cmd al root del proyecto, cd learning-python, . path actual, .. path padre
import sys
#permite agregar un path para importar el modulo rangetest
sys.path.append('stuff')
from rangetest import *
#Decoradores limitador en stuff rangetest.py, importar rangetest.Tambien se pueden realizar con assert

#RANGETEST ADMITE COMO ARGUMENTOS DE LA LISTA/TUPLA [LA POSICION DEL ARGUMENTO,VALOR MINIMO,VALOR MAXIMO]
#la funcion definida llamada rangetest por eso @rangetest, no por el nombre del archivo rangetest.py
@rangetest([0, 0.0, 1.0])
def prue(percent):
    pay=10000*(1+percent)
    return pay

#aumento del 20% del sueldo
print(prue(0.2))


# __repr__ SE LLAMA AL HACER USO DE PRINT, finalmente retorna un mensaje personalizado.
# def __repr__(self):
# return '[Person: %s, %s]' % (self.name, self.pay)


#SUPER PERMITE ACCEDER AL PARAMETRO DE LA CLASE SI ES LLAMADO DE UN METODO X DE LA CLASE.
# class Yeah(object):
#     def __init__(self, name):
#         self.name = name
#     # Gets called when an attribute is accessed
#     def __getattribute__(self, item):
#         print '__getattribute__ ', item
#         # Calling the super class to avoid recursion
#         return super(Yeah, self).__getattribute__(item)
#     # Gets called when the item is not found via __getattribute__
#     def __getattr__(self, item):
#         print '__getattr__ ', item
#         return super(Yeah, self).__setattr__(item, 'orphan')


# Nombre de la clase que instancio la variable bob
# bob.__class__.__name__

#LOS PARAMETROS DE UNA CLASE, SE PUEDEN LLAMAR COMO DICCIONARIOS CON __dict__
# >>> list(bob.__dict__.keys()) # Attributes are really dict keys
# ['pay', 'job', 'name'] # Use list to force list in 3.X



#GET Y SETTERS EN PYTHON CON DECORADORES
# class Geeks:
#      def __init__(self):
#           self._age = 0
       
#      # using property decorator
#      # a getter function
#      @property
#      def age(self):
#          print("getter method called")
#          return self._age
       
#      # a setter function
#      @age.setter
#      def age(self, a):
#          if(a < 18):
#             raise ValueError("Sorry you age is below eligibility criteria")
#          print("setter method called")
#          self._age = a
  
# mark = Geeks()
  
# mark.age = 19
  
# print(mark.age)


#A Generic Display Tool ,842 