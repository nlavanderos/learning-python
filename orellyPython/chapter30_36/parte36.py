#CHAPTER 32 : Advanced Class Topics,1000


# Room for improvement: MRO, slots, GUIs.<__mro__,__slots__>
#MRO>>method resolution order 3.x prioriza la herencia de izquierda para buscar atributos,DFLR>>search depth first then left to right
#DFLR busca el atributo en todas las herencias quedandose con el ultimo valor encontrado mas ala derecha

#MRO, con force selection de un atributo/metodo
#class A: attr = 1 # Classic (Python 2.X)
#class B(A): pass # B and C both lead to A
#class C(A): attr = 2
#class D(B, C): attr = B.attr # <== Choose A.attr, above
#x = D()
#x.attr # Searches x, D, B, A
#1

#DFLR, con force selection de un atributo
#  class A(object): attr = 1 # New-style ("object" not required in 3.X)
#  class B(A): pass
#  class C(A): attr = 2
#  class D(B, C): attr = C.attr  # <== Choose C, to the right
#  x = D()
#  x.attr # Searches x, D, B, C
# 2

#MRO, con force selection de un metodo
# class A:
#     def meth(s): print('A.meth')
# class C(A):
#     def meth(s): print('C.meth')
# class B(A):
#     pass
# class D(B, C): 
#     pass
# x = D()
# x.meth()
# print(D.__mro__)


#the new style, __mro__ method can list all paths classes to the final object.Depth first then left to Right 
#in the previous example print(D.__mro__)


#Slots se usa para optimizacion, ya que reduce el tiempo de ejecucion.
#__slots__ , permite hacer uso exclusivo de las variables que aparecen en la lista.
#Si uno quiere anadir mas tiene que agregar el metodo sobrecarga __dict__ a slots...
#sera valido para instancias creadas afuera de la clase y dentro de la clase(self).

# class Slotful:
#     __slots__ = ['a', 'b', '__dict__']
#     def __init__(self, data):
#         self.c = data
# I = Slotful(3)
# I.a, I.b = 1, 2
# I.d=4

# print(I.a, I.b, I.c,I.d,I.__dict__.keys())


#Existen tres formas para establecer get y SETTERS

#1.DEFINIENDO funcion property, como argumento las funciones creadas al nombre del atributo.
# class properties(object): # Need object in 2.X for setters
# def getage(self):
# return 40
# def setage(self, value):
# print('set age: %s' % value)
# self._age = value
# age = property(getage, setage, None, None)


#2.USANDO metodos de sobrecarga __getattr__ y __setattr__
# class operators:
# def __getattr__(self, name): # On undefined reference
# if name == 'age':
# return 40
# else:
# raise AttributeError(name)
# def __setattr__(self, name, value): # On all assignments
# print('set: %s %s' % (name, value))
# if name == 'age':
# self.__dict__['_age'] = value # Or object.__setattr__()
# else:
# self.__dict__[name] = value

# 3. usando decoradores @ , tales como @property,@nombreAtributo.setter siendo la mas sencilla de implementar
class properties:
    def __init__(self):
        self._age = 0
       
    @property # Coding properties with decorators: ahead
    def age(self):
        print("getter method called")
        print(self._age)
        return self._age

    @age.setter
    def age(self, value):
        print("setter method called")
        self._age=value

objetx=properties()
# basicamente es un metodo con asignacion
objetx.age=20
objetx.age
# lo que si tambien podria sobreescribir el valor usando el nombre del atributo.
# objetx._age=10
# objetx._age