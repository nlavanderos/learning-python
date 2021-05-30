import math,random,decimal
from fractions import Fraction
#BITWISE

#OR
#En binario seria 100 | 1010
print(4|10)

#AND
#Si ambos valores son del mismo tipo se usa el primer valor como output
#Si ambos valores son de distinto tipo es 0 en el caso de los numeros
#Onda comparando pares/impares 
print(1&2)

#XOR
#SI ambos valores son de distinto tipo se suman
#En caso contrario se resta
print(7^1)

#Shift operator
#a la derecha disminuye,a la izquierda aumenta el valor
#el numero a la izquierda es el valor,el otro numero corresponde 
#a los segmentos binarios para aumentar o disminuir.

print(2>>1,2<<1)

#Con el metodo bit_length contamos solamente el contenido a la derecha de 0b,en vez de usar
#len('0b101001')-2
print(0b101001.bit_length())

#Van con mayuscula ya que son constantes
PI=math.pi
E=math.e

#Algunas operaciones matematicas mas usadas,cabe destacar que min,max,round,pow y abs son propias
#del built-in de python
print(math.sin(2*PI/180),math.sqrt(16),pow(2,4),2**4)
print(abs(-51),sum((1,2,3,4,5)),min(15,100,254,365),max(15,100,254,365))
print(round(2.654))

#Usos de libreria random

print(random.random())
print(random.randint(1,5))
series = ['naruto', 'shingeki', 'fullMetal']
#Choice solamente elige un item de los elementos
print(random.choice(series))
#Choices puede repetir elementos y ademas podemos especificar la cantidad de elementos
print(random.choices(series, k=2))
#Sample no repite elementos
print(random.sample(series, k=2))
#para revolver los datos de series existe shuffle.
random.shuffle(series)
print(series)

#Me permite modificar la cantidad de decimales que contendra una instancia de decimal
decimal.getcontext().prec=4
print(decimal.Decimal(1)/decimal.Decimal(7))

#Con el statement with podemos establecer una precision temporal concatenando el metodo
#localcontext()
with decimal.localcontext() as nu:
    nu.prec=2
    print(decimal.Decimal(str(2000+1.3)))
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
    print(decimal.Decimal(1.00) / decimal.Decimal(3.00))

#10E+02 significa qe un numero esta elevado a 2 o tmb puede ser E-02 elevado a -2

#Fractions
fraction1, fraction2=Fraction(3,9), Fraction(2,7) 
print(f'{float(fraction1+fraction2):.2f} can be : {fraction1+fraction2}' )

#Transformacion de un flotante a fraccion,siempre debera ser instanciado como string.
print(Fraction('0.22225'))

print((2.5).as_integer_ratio())

#Para simplificar fractiones
print((fraction1/fraction2).limit_denominator(10))


#SETS
#La mayoria de las operaciones de set requieren dos set 
set1=set('holi')
set2=set('hlidmn')

#Diferencia simetrica
print(set1^set2)

#Interseccion de dos set
print(set1.intersection(set2))

set1.add('spam')
set1.update(set(['a','b']))
set1.remove('a')
print(set1)

#a>b a ,a es superset de b es lo mismo que a.isuperset(b)
#a<b a ,a es subset de b es lo mismo que a.issubset(b)