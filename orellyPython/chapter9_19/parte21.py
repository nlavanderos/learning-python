'''Documentacion de os y urlib.request'''
from os import popen,system
from urllib.request import urlopen

#DO WHILE
def exitTest():
    '''Funcion que permite una sentencia doWhile '''
    return True

i = 1
while True:
    print(i)
    i = i + 1
    #Se ejecuta una vez
    if exitTest():
        print(i*2)
    print(i**3)
    break

#... == Ellipsis
#bool(...)==True bool(None)== False ,ademas Ellipsis object 
# peremite hacer slicing en matrices en numpy lib a[...] , a[1,...]
#a[...,1] ,etc...

#Continue statement
x = 10
while x:
    x = x-1
    if x % 2 != 0: continue 
    print(x, end=' ')

print('')
#Enumerate
S='pokemon'
print('\n'.join([f'{i}){x}' for i,x in enumerate(S)]))

#Todo el contenido de un path actual
#print(popen('dir').readlines())

#Informacion del equipo,esta limitado a 4 campos de systeminfo 0...3
print('\n'.join([j.strip() for i,j in enumerate(popen('systeminfo')) if i<4]))

#Similar pero con limpieza de saltos de linea y espacios
# print(system('systeminfo'))

#LECTURA DE CODIGO FUENTE DE UN URL
# with urlopen('http://www.facebook.com/') as f:
#     print(f.read(100).decode('utf-8'))

#Trae la documentacion de una clase/funcion con el metodo __doc__
#En este caso utilizamos la funcion exitTest
print(exitTest.__doc__)