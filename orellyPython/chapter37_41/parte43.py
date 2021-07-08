#Pregunta de grupo telegram
# class Fibo():

#     def __init__(self, limit, secuence=[0,1], first=True):
#         self.secuence = secuence
#         self.first = first
#         self.limit=limit
#         if self.first==True:
#             self.secuence=[0,1]
#             print(len(self.secuence))


#     def fiboani2(self):

#         if self.limit > 2:
#             self.secuence.append(self.secuence[-1] + self.secuence[-2])

#         elif self.limit > 1:
#             return self.secuence
#         else:
#             return self.secuence[:self.limit]
#         return Fibo(self.limit-1,self.secuence,first=False).fiboani2()

# print(Fibo(5).fiboani2())
# print(Fibo(10).fiboani2())






#Metodo de sobrecarga : __getattribute__

# class D(object):
#     def __init__(self):
#         self.test1=20
#         self.test2=21
#     def __getattribute__(self,name):
#         if name=='test2':
#             assert False,'No se puede acceder al atributo'
#         else:
#             return object.__getattribute__(self, name)

# Se inicializa la clase
# d = D()

# Se pide el contenido del atributo
# print(d.test1)
# Valor encapsulado con assert
# print(d.test2)







#EJEMPLO DE METACLASE

#CREACION DE CLASE DE MANERA DINAMICA
#x = type('Spam', (), {'data': 1, 'meth': (lambda x, y: x.data + y)})




# class = Meta(classname, superclasses, attributedict)
# Meta.__new__(Meta, classname, superclasses, attributedict)
# Meta.__init__(class, classname, superclasses, attributedict)


#CREACION DE METACLASE 
# class Meta(type):
#     def __new__(meta, classname, supers, classdict):
#     # Run by inherited type.__call__
#         return type.__new__(meta, classname, supers, classdict)


#EJEMPLO 1
# class MetaOne(type):
#     def __new__(meta, classname, supers, classdict):
#         print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
#         return type.__new__(meta, classname, supers, classdict)
# class Eggs:
#     pass

# print('making class')
# class Spam(Eggs, metaclass=MetaOne): # Inherits from Eggs, instance of MetaOne
#     data = 1 # Class data attribute
#     def meth(self, arg): # Class method attribute
#         return self.data + arg

# print('making instance')
# X = Spam()
# print('data:', X.data, X.meth(2))



#Ejemplo 2
# class A(type):
#     def x(cls): print('ax', cls) # A metaclass (instances=classes)
#     def y(cls): print('ay', cls) # y is overridden by instance B
# class B(metaclass=A):
#     def y(self): print('by', self) # A normal class (normal instances)
#     def z(self): print('bz', self) # Namespace dict holds y and z

# obj1=B()

# #Metodos de clase B
# obj1.y()
# obj1.z()

# #Metodos de clase A
# B.x()
# B.y()#Metodo sobrescrito, en este caso prima la clase B sobre la metaclase


