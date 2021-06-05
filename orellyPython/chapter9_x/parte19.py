#Introducing Python Statements - chapter 10, page 319
#Algunos statements no vistos con anterioridad

from sys import stdout

for i in range(3):
    if i%2:
        print('impar')
        #sigue con la siguiente iteracion
        continue
    elif(i==2):
        #no hace nada y continua la iteracion actual
        pass
        #rompe el ciclo iterativo
        break
    print('par')


monster='Azir'
#Reasignacion de variables globales en funcion
def callingMonster():
    global monster;
    monster='Xohl'
    return monster

print(callingMonster())


def oneAdd(str):
    try:
        str+=1
        print(str)
    except TypeError as exc:
        raise TypeError(f'No puedes sumar \'{str}\' con numeros') from exc
        #Tambien en una situacion personalizada se puede establecer -> raise Exception('')

#Activa el raise
#oneAdd('elemento')


#starred expression
#solamente puede haber una starred expression en un conjunto de Datos
#en el caso que queremos todo el contenido >> *stExp, <<  en solamente una variable starred
nostExp,*stExp=['pikachu','staryu','abra','geodude']

#multiple target assignment
#es sumamente util cuando necesitamos inicializar tipos de datos ejemplo
#lista1=lista2=[]
stExp[0]=stExp[1]='Evee'
print(nostExp,stExp)

#list assignment (positional)
[laPosA,laPosB]=['b','bbsadsd']
print(laPosA,laPosB)


#slicing
recorteA,recorteB,recorteC=list(laPosB[:2])+[laPosB[2:]]
print(recorteA,recorteB,recorteC)

cicleTest=[23,59,4,7]
while cicleTest:
    #similarmente con starred expression
    #handTest,*cicleTest=cicleTest
    headTest,cicleTest=cicleTest[0],cicleTest[1:]
    print(headTest , cicleTest)


# alternativa de extension de lista con caracteres
#se admite con += pero con + solamente no.
listaExtension=[]
listaExtension+='spam'
print(listaExtension)

#papel de underscore _
#definire algunos ....en una asignacion _ ignora los valores
#funciones que empiezan con _ ,osea def _name(): se ignoran de una posible importacion
#en una propiedad de clase self.__c=3 ,para acceder se hace uso de un metodo especial print(nombreobjeto._nombreclase__nombrevariable)

#ESTILO DE PROGRAMACION PEP-8
#https://www.python.org/dev/peps/pep-0008/

#Separador de informacion
DD=19
YY=2019
MM=10
print(DD,MM,YY,sep='/')

#Otra forma de escribir 
stdout.write('Book X'+'\n')

#para pasar codigo de python2.x a python3.x
#existe el script 2to3  generalmente viene instalada con python en Tools/scripts
#uso >> python path2to3 -w nombrearchivo.py
#se genera un archivo de backup de la ver 2 y el archivo convertido mantiene su nombre en version3

#Declaracion de print en 2.x se necesita ese modulo
#from __future__ import print_function