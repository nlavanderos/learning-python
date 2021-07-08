# __getattr__ is run for undefined attributes
# __getattribute__ is run for every attribute



#Cargar un modulo en una variable y retornarla.Con un metodo inclusive.

# def loadclass():
# import sys, importlib
# modulename = sys.argv[1] # Module name in command line
# module = importlib.import_module(modulename) # Import module by name string
# print('[Using: %s]' % module.CardHolder) # No need for getattr() here
# return module.CardHolder



#Decorators


# def decorator(cls): # On @ decoration
#     class Wrapper:
#         def __init__(self, *args): # On instance creation
#             #tranfiere a wrapped todo el contenido instanciado en forma de diccionario
#             self.wrapped = cls(*args)
#             #traza
#             print(self.wrapped.__dict__)
#         def __getattr__(self, name): # On attribute fetch
#             return getattr(self.wrapped, name)

#     return Wrapper

# @decorator
# class C: 
#     def __init__(self, x, y):
#         self.attr = 'spam'
#         self.x=x
#         self.y=y

# instanciaP = C(6, 7)
# print(instanciaP.y)




#Nesting Decorators

# def d1(F): return lambda: 'X' + F()
# def d2(F): return lambda: 'Y' + F()
# def d3(F): return lambda: 'Z' + F()

# @d1
# @d2
# @d3
# #EL ARGUMENTO SE VA PASANDO COMO F, SOLAMENTE PARA @D3 SERIA D3(FUNC).OSEA 'ZSPAM'
# def func(): # func = d1(d2(d3(func)))
#     return 'spam'
# print(func()) # Prints "XYZspam"




#DECORATORS ARGUMENTS,ejemplo.


# def timer(label=''):
#     def decorator(func):
#         def onCall(*args): # Multilevel state retention:
#             ... # args passed to function
#             func(*args) # func retained in enclosing scope
#             print(label, ...) # label retained in enclosing scope
#         return onCall
#     return decorator # Returns the actual decorator

# @timer('==>') # Like listcomp = timer('==>')(listcomp)
# def listcomp(N): ... # listcomp is rebound to new onCall
# listcomp(...) # Really calls onCall







#Patron de diseño >>>singleton
#singleton o instancia única es un patrón de diseño que permite restringir la creación de objetos pertenecientes a una clase o el
#valor de un tipo a un único objeto.
#Su intención consiste en garantizar que una clase solo tenga una instancia y proporcionar un punto de acceso global a ella. 



# instances = {}
# def singleton(aClass): # On @ decoration
#     def onCall(*args, **kwargs): # On instance creation
#         if aClass not in instances: # One dict entry per class
#             instances[aClass] = aClass(*args, **kwargs)
#             print('>>>',instances[aClass].__dict__,aClass.__name__)
#         return instances[aClass]
#     return onCall
# #To use this, decorate the classes for which you want to enforce a single-instance model
# #(for reference, all the code in this section is in the file singletons.py):

# @singleton # Person = singleton(Person)
# class Person: # Rebinds Person to onCall
#     def __init__(self, name, hours, rate): # onCall remembers Person
#         self.name = name
#         self.hours = hours
#         self.rate = rate
#     def pay(self):
#         return self.hours * self.rate

# @singleton # Spam = singleton(Spam)
# class Spam: # Rebinds Spam to onCall
#     def __init__(self, val): # onCall remembers Spam
#         self.attr = val

# bob = Person('Bob', 40, 10) # Really calls onCall
# print(bob.name, bob.pay())
# sue = Person('Sue', 50, 20) # Same, single object
# print(sue.name, sue.pay())
# X = Spam(val=42) # One Person, one Spam
# Y = Spam(99)
# print(X.attr, Y.attr)






#Implementing Private/public Attributes, es bueno para encapsulacion ya que en python no existen clases publicas/privadas

#Admite una traza de codigo con True
# traceMe = False

# def trace(*args):
#     if traceMe: print('[' + ' '.join(map(str, args)) + ']')

# def accessControl(failIf):
#     def onDecorator(aClass):
#         if not __debug__:
#             return aClass
#         else:
#             class onInstance:
#                 def __init__(self, *args, **kargs):
#                     self.__wrapped = aClass(*args, **kargs)
#                 def __getattr__(self, attr):
#                     trace('get:', attr)
#                     if failIf(attr):
#                         raise TypeError('private attribute fetch: ' + attr)
#                     else:
#                         return getattr(self.__wrapped, attr)
#                 def __setattr__(self, attr, value):
#                     trace('set:', attr, value)
#                     if attr == '_onInstance__wrapped':
#                         self.__dict__[attr] = value
#                     elif failIf(attr):
#                         raise TypeError('private attribute change: ' + attr)
#                     else:
#                         setattr(self.__wrapped, attr, value)
#         return onInstance
#     return onDecorator


# def Private(*attributes):
#     return accessControl(failIf=(lambda attr: attr in attributes))
# def Public(*attributes):
#     return accessControl(failIf=(lambda attr: attr not in attributes))


#El atributo age,tall estan privados para solicitarlo con .age o .tall
# @Private('age','tall') # Person = Private('age')(Person)
# class Person: # Person = onInstance with state
#     def __init__(self, name, age, tall):
#         self.name = name
#         self.age = age
#         self.tall=tall


# x=Person('Zeus',10,163)
# print(x.name)



#golfin
# En el canal de Telegram salió una pregunta que puede servir para golfing!
# Para una lista [1, 2, 3, 'FIN', 4, 5, 'FIN', 6, 7, 8, 9, 'FIN'] transformarla en una lista de listas donde la palabra 'FIN' define el límite.
# Por ejemplo el resultado debería ser: [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# l=[1, 2, 3, 'FIN', 4, 5, 'FIN', 6, 7, 8, 9, 'FIN']

# r=[]
# b=0
# indice=[i for i,x in enumerate(l) if x=='FIN']
# for i,j in enumerate(l):
#     if i in indice:
#         r.append(l[b:i])
#         b=i+1
# print(r)




#IMPLEMENTACION DE GROUPBY DE ITERTOOLS, CON EL EJERCICIO DE GOLFING
# from itertools import groupby
# lista= [1, 2, 3, 'FIN', 4, 5, 'FIN', 6, 7, 8, 9, 'FIN'] 
# [list(v) for k, v in groupby(lista, lambda x: x == 'FIN') if not k]



#IMPLEMENTACION DE GROUP BY SIN ITERTOOLS
# things = [("animal", "bear"), ("animal", "wolf"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]

# clases=['animal','plant','vehicle']
# for x in clases:
#     print(f'Agrupacion por {x}')
#     for i in range(len(things)):
#         if x in things[i][0]:
#             print(f'{things[i][1]}')