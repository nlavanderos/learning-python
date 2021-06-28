#CHAPTER 29 : Class Coding Details, 859

#Siempre se prioriza las llamadas de un clase base v/s la clase super/heredada

#Abstract superclasses in Python 3.X and 2.6+: Preview
# from abc import ABCMeta, abstractmethod
# class Super(metaclass=ABCMeta):
#     @abstractmethod
#     def method(self):
#         pass

# But in Python 2.6 and 2.7, we use a class attribute instead:
# class Super:
#     __metaclass__ = ABCMeta
#     @abstractmethod
#     def method(self, ...):
#         pass

#PARA HACER USO DE LAS CLASES ABSTRACTAS, DEBES IMPORTAR LA LIBRERIA abc <from abc import ABCMeta, abstractmethod>
# POSTERIORMENTE DEBES CREAR UNA SUBCLASE HERADANDO LA CLASE BASE 
# QUE CUENTA CON SUPER A LA CLASE ABSTRACTA <metaclass=ABCMeta>.
#Tambien no debes olvidar definir el metodo abstracto con el decorador @abstractmethod en la clase base, para crearlo en la subclase.

class C():
    def __init__(self,X):
        self.X = X # Class attribute (C.X)
    def outer(self):
        X=34
        def inner():
            #Permite redifinir el valor de la variable X para este scope.
            nonlocal X
            #Nuevo valor para x
            X=52
            #Si no existiese X=52 tomaria el valor anterior.Independiente si nonlocal X esta definido
            self.X = X
            
        inner()

#Creacion del objeto nu e instancia de la clase C
nu=C(12)
print(nu.X)
nu.outer()
print(nu.X)
