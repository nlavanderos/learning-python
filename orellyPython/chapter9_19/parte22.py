from functools import reduce
from pickle import FALSE
from random import SystemRandom,shuffle


file1 = 'orellyPython\chapter9_x\p17_1.txt'
#Cuenta todas las lineas incluyendo espacios
#print(len(open(file1).readlines()))
#Cuenta todas las lineas sin espacios
print(len([line for line in open(file1) if line.strip() != '']))


listaCaracteres=['A','B','C','D','E','F',1,9,7,3,5,6]
shuffle(listaCaracteres)
parteSerial=''
serial=[]
for i in range(4):
    for j in range(4):

        parteSerial+=''.join(str(listaCaracteres[SystemRandom().randrange(0,len(listaCaracteres))]))

        if (j == 3):
            serial.append(parteSerial)
            parteSerial=''

#La funcion reduce funciona similarmente a la funcion map
#Porque reduce admite como argumentos una funcion y un iterable
#Finalmente retorna un solo valor.Por otro lado map retorna cada valor del iterable entorno a una funcion.
print(reduce(lambda x,y:x+'-'+y,serial))



tuple1=(4,5,2)
tuple2=(8,1,14)
unzip1,unzip2=zip(*zip(tuple1,tuple2))
print(unzip1)

