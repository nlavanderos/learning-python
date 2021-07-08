#CHAPTER 38 :Managed Attributes, 1219

#properties without decorators

class Person: # Add (object) in 2.X
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        "Name property doc"
        print('fetch...')
        return self._name
    @name.setter
    def name(self, value):
        print('change...')
        self._name = value

    @name.deleter 
    def name(self):
        print('remove...')
        del self._name

    #Las properties, son siempre 4 debido a que estan establecidas en el built-in de python.
    # fget
    # function to be used for getting an attribute value
    # fset
    # function to be used for setting an attribute value
    # fdel
    # function to be used for del'ing an attribute
    # doc
    # docstring

    #De otra forma se puede definir cada funcion con x nombre y pasarla a una variable con el nombre inicializado, en este caso name.
    #name = property(getName, setName, delName, "Creacion de nombre",)

pj=Person('Kaiba')
print(pj.name)
pj.name='Seto Kaiba'
print(pj.name)
del pj.name
print(Person.name.__doc__)



#Computed Attributes

class PropSquare:
    def __init__(self, start):
        self.value = start
    def getX(self): # On attr fetch
        return self.value ** 2
    def setX(self, value): # On attr assign
        self.value = value
    X = property(getX, setX) # No delete or docs
P = PropSquare(3) # Two instances of class with property
Q = PropSquare(32) # Each has different state information
print(P.X) # 3 ** 2
P.X=4
print(P.X) # 4 ** 2
print(Q.X)

#Descriptores


class Descriptivo:
    def __init__(self):
        self.atb=0
    #self,instance,owner
    def __get__(self,*args):
        return [self,args,self.atb]
    
    def __set__(self,instance,value):
        print('sss',instance.__class__.__name__)
        self.atb=value
        return self.atb


#Self>>es la clase.nombreAtributo(Sujeto.atr)
#instancia >> es el nombre de la variable(instanciaB), que contiene la instancia
#owner >> es la clase que inicializa(Sujeto)

class Sujeto:
    m=Descriptivo()

instanciaB=Sujeto()
instanciaB.m=25
print(instanciaB.m)



#PROPERTIES Y Descriptores

# class Property:
#   def __init__(self, fget=None, fset=None, fdel=None, doc=None):
#       self.fget = fget
#       self.fset = fset
#       self.fdel = fdel # Save unbound methods
#       self.__doc__ = doc # or other callables
#   def __get__(self, instance, instancetype=None):
#       if instance is None:
#           return self
#       if self.fget is None:
#           raise AttributeError("can't get attribute")
#       return self.fget(instance) # Pass instance to self
#   # in property accessors
#   def __set__(self, instance, value):
#       if self.fset is None:
#           raise AttributeError("can't set attribute")
#       self.fset(instance, value)
#   def __delete__(self, instance):
#       if self.fdel is None:
#           raise AttributeError("can't delete attribute")
#       self.fdel(instance)
# class Person:
#   def getName(self): print('getName...')
#   def setName(self, value): print('setName...')
#   name = Property(getName, setName) # Use like property()