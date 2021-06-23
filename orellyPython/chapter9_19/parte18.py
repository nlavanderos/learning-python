#Storing Native Python Objects: pickle - 290
from pickle import load as pickleLoad,dump as pickleDump
from json import load as jsonLoad,dumps as jsonDumps,dump as jsonDump
from csv import reader,writer,QUOTE_MINIMAL
from struct import pack,unpack
from types import FunctionType

#pickle me permite guardan la informacion tal como es escrita
#el metodo dump me permite agregar
#el metodo load cargar datos
tupla1=('led','cars')
try :
    lectura=open('orellyPython/chapter9_x/p18_1.pkl',mode='rb')
    print(pickleLoad(lectura))
except FileNotFoundError:
    with open('orellyPython/chapter9_x/p18_1.pkl',mode='wb') as f:
        pickleDump(tupla1,f)



diccionario1=dict(raza='Rotwailer',nombre='Zeus')
try :
    lectura=open('orellyPython/chapter9_x/p18_1.json',mode='r')
    print(jsonLoad(lectura))
    lectura.close()
except FileNotFoundError:
    with open('orellyPython/chapter9_x//p18_1.json',mode='w') as f:
        #LA SENTENCIA DESPUES DEL WITH puede ser declarada en fp,osea open(..)
        jsonDump(diccionario1,fp=f,indent=4)
        #print(jsonDumps(diccionario1,indent=4),file=f)
        #f.write(jsonDumps(diccionario1,indent=4))

#DELIMITADOR DE EXCEL ;
#DELIMITADOR CSV ,
try :
    lectura=open('orellyPython/chapter9_x/p18_1.csv',mode='r')
    spamReader=reader(lectura, delimiter=';', quotechar='|')
    for row in spamReader:
        print(', '.join(row))
except FileNotFoundError:
    with open('orellyPython/chapter9_x/p18_1.csv',mode='w') as f:
        spamwriter = writer(f, delimiter=';',quotechar='|', quoting=QUOTE_MINIMAL)
        spamwriter.writerow(['Anime'] * 5)
        spamwriter.writerow(['Naruto', 'Shingeki', 'SAO','Death Note','FullMetal'])


#big ENDIAN >
struct1=pack('>i4sh',7,b'lala',8)
try :
    lectura=open('orellyPython/chapter9_x/p18_1.bin',mode='rb')
    values=unpack('>i4sh',lectura.read())
    print(values)
    
except FileNotFoundError:
    with open('orellyPython/chapter9_x//p18_1.bin',mode='wb') as f:
        f.write(struct1)
        
finally:
    lectura.close()
    
#RESUMEN CLASIFICACION DE OBJETOS
 
# TIPO OBJETO   CATEGORIA   MUTABLE

# Numbers(all)  Numeric     No
# Strings(all)  Sequence    No
# Lists         Sequence    Yes
# Dictionaries  Mapping     Yes
# Tuples        Sequence    No
# Files         Extension   N/A
# Sets          Set         Yes
# Frozenset     Set         No
# bytearray     Sequence    Yes

#Definicion de clase
#OPERATOR OVERLOADING __iter__ por ejemplo

class MySequence():
    def __init__(self,lista):
        self.lista=lista

    def __getitem__(self, index):
        return self[index]
    def __add__(self, other):
        return self + other
    
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        x = self.n
        self.n += 1
        return self.lista[x]

    def __len__(self):
        return len(self.lista)


item1=[7,5,7,10]

Objeto1=MySequence(item1)
item=iter(Objeto1)
print({next(item) for i in range(len(Objeto1))})
   
#Dado una lista pido el valor de una posicion
print(MySequence.__getitem__(item1,2))
#La suma de dos variables
print(MySequence.__add__(item1[-1],2))

#Sirve para comparar si un elemento es una funcion
#Con la libreria types y el metodo usado es FunctionType
print(type(MySequence.__add__)==FunctionType)


def pruebaYield():
    step=1
    print('PASO 1')
    yield step

    step+=1
    print('PASO 2')
    yield step
    
    step+=1
    print('PASO 3')
    yield step


for i in pruebaYield():
    print(i)

#Similarmente 
# test=pruebaYield()
# for i in range(3):
#     print(next(test))