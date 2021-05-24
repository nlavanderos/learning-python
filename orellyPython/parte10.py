from decimal import Decimal,getcontext
from fractions import Fraction

X = set('lyami')
Y = {'l', 'i', 'l'}

#Las operaciones devuelven un set con valores segun (&,|,-).
#Excluyendo la operacion (>) correspondiente a superset que retorna un booleano(True/False)

#Interseccion de sets(devuelve los lementos iguales en ambos sin importar repeticiones)
print(X&Y)

#Union de sets(Une los elementos que aparecen en ambos sin repeticiones)
print(X|Y)

#Diferencia de sets(al contenido de x se le resta los elementos iguales en y )
print(X-Y)

#X es un superset de Y ,debido que x contiene todos los elementos de y
print(X>Y)

#126 Other Core Types

X = set('lyami')
Y = {'l', 'i', 'l'}

#Las operaciones devuelven un set con valores segun (&,|,-).
#Excluyendo la operacion (>) correspondiente a superset que retorna un booleano(True/False)

#Interseccion de sets(devuelve los lementos iguales en ambos sin importar repeticiones)
print(X&Y)

#Union de sets(Une los elementos que aparecen en ambos sin repeticiones)
print(X|Y)

#Diferencia de sets(al contenido de x se le resta los elementos iguales en y )
print(X-Y)

#X es un superset de Y ,debido que x contiene todos los elementos de y
print(X>Y)

#Datos repetidos son filtrados con set y convertidos llevados a una lista. 
print(list(set([1,2,3,4,4,5])))


#String formating
title='Final Fantasy XV'
print(f'{title:-^30}')


money=3000000
print('{:,}'.format(money).replace(',','.'))

#Decimales
numDecimalA=Decimal('3.141')
print(f'{numDecimalA+1}')

#Fracciones
fractionA=Fraction(1,10)
fractionB=Fraction(1,5)
print(fractionA+fractionB)

#Valores logicos True / False
print(bool(None))

#Distintas maneras de identificar si un objeto es una lista
L=[1,2,3]
if type(L) == type([]): # Type testing, if you must...
    print('yes')

if type(L) == list: # Using the type name
    print('yes')

if isinstance(L, list): # Object-oriented tests
    print('yes')


class Worker:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1]
    def aumento(self,percent):
        self.pay*=(1.0+percent)



trabajadorA=Worker('Nicolas Lavanderos',1000000)
trabajadorA.aumento(.05)
print(trabajadorA.lastName(),trabajadorA.pay)

