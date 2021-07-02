# Static and Class Methods , en primera instancia sin decoradores.con palabras staticmethod y classmethod


#1.METODO ESTATICO, no tengo la necesidad de pasarle como argumento la variable o self a el metodo deseado.

# class Spam:
#     numInstances = 0
#     def __init__(self):
        
#         Spam.numInstances = Spam.numInstances + 1
#     def printNumInstances():
#         print("Number of instances created: %s" % Spam.numInstances)
#     printNumInstances = staticmethod(printNumInstances)

# class Sub(Spam):
#     def printNumInstances(): # Override a static method
#         print("Extra stuff...") # But call back to original
#         Spam.printNumInstances()
#     printNumInstances = staticmethod(printNumInstances)


# a=Sub()
# b=Sub()
# b.printNumInstances()


#2.METODO DE CLASE /METODO ESTATICO, definidos ej: smeth = staticmethod(smeth) 
#3.Metodos CLASE/ESTATICO con decoradores, @staticmethod - @classmethod

#cls for the first argument to class methods.
#self for the first argument to instance methods.
#metodo super(), para llamar las superclases de la clase.

class Mx1:
    def __init__(self):
        print('estas en MX1')
        Mx1.imeth(self,self._numero)
        super().__init__()
        print('saliste en MX1')


    def imeth(self, x): 
        print([self, x*x])

class Mx2:
    def __init__(self):
        print('estas en MX2')
        Mx2.imeth(self,self._numero)
        #No es necesario definir de esta manera , super(Mx2,self).__init__().Cuando ya tenemos object como base
        super().__init__()
        print('saliste en MX2')

    def imeth(self, x): 
        print([self, x+x])


class Methods(Mx2,Mx1):

    def __init__(self):
        self._numero=0

    @property
    def imeth(self):
        #no es necesario instanciarlo, de esta manera super(Methods,self).__init__() .pero es buena practica
        super().__init__()
        #tambien podria llamar a todos los metodos imeth()
        #super().imeth()
        print('Estas en Methods en MX')
        return print([self, self._numero])

    @imeth.setter
    def imeth(self, value):
        print("setter method called")
        self._numero=value


    @staticmethod
    def smeth(x): 
        print([x])
    @classmethod
    def cmeth(cls, x): 
        print([cls.__name__, x])
    # smeth = staticmethod(smeth) 
    # cmeth = classmethod(cmeth)

#Instancia normal, con decoradores
x=Methods()
x.imeth=10
x.imeth


#Metodo estatico, sin pasar instancia
Methods.smeth(55)

#Metodo de clase, donde como primer argumento le paso el nombre de la clase base como cls, similar a self para instancias.
Methods.cmeth(21)



#Como cambiar una instancia de superclase en el runtime
#class C(X), en este caso la clase X sera cambiada por el nombreClaseSuper.Entonces class C(nombreClaseSuper)
# nombreClase.__bases__ = (nombreClaseSuper,)

#para llamar a la primera base de la clase nombreClase.__bases__[0].metodo(self)