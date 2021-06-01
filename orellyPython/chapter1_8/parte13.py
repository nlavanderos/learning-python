from sys import getrefcount
from copy import copy,deepcopy
import weakref
from re import findall,match

#Para agrega un path especifico
#sys.path.append('learning-python')

#Funcion para encontrar el elemento mas comun de una lista
#a.count('metal') en este caso arrojaria 2
a=['naruto','naruto','shingeki','shingeki','metal','metal','shingeki','naruto','naruto']
print(max(set(a),key=a.count))

#Booleans
#Es verdadero ya que 1/0 es True/False
print(isinstance(True,int))

#La sentencia is nos permite comprobar si dos objetos son distintos,existen excepciones como
#la instancia de dos variables distintas con valores integer iguales dara true
print(True is 1,type([1,2]) is list,123 is 123)

#The Dynamic Typing Interlude

#De esta manera realizamos una copia de la lista1 y nos olvidamos de las referencias(punteros)
lista1 = [2, 5, 7]
lista2 = lista1[:]
lista1[0] = 4
print(lista1)

#Otra formas de realizar copiado de informacion sin referencias
#Con deepcopy si ahi informacion enlazada, mientras si es lineal con copy debiese bastar
elementoX=[[1,22,66,[2,2,3]],[2,4]]
elementoY=deepcopy(elementoX)
elementoX[0][0] = 464584
print(elementoY,elementoX)

#Referencias de un objeto
#x ejemplo el valor de getrefcount para 1 incluye los 1 en los built-in de python + los usados en
#el archivo actual.
print(getrefcount(1))

#Weak references con una clase de ejemplo
class Worker():
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay

trabajador1=Worker('Nicolas',1222)
trabajador2=weakref.ref(trabajador1)
print(trabajador2().name,weakref.getweakrefcount(trabajador1))


#String Fundamentals-189

#Partition crea una tupla de tres elementos,si se encuentra el buscado este estara al centro[1],
#Sino se encuentra la frase entera estara en la posicion [0]
frase1='Meanwhile in yolo the desert of yolo land you know'
print(frase1.partition('yolo'))

#findall de la libreria re me permite hayar todas las ocurrencias de una palabra o caracter
#find built-in indica la posicion de un caracter
print(findall('yolo',frase1),frase1.find('M'))

#Caracteres especiales siempre con backSlash \
#Mientras que r antes de los apostrofes indica un rawString donde es el texto original con backSlash
#\t tabulacion, \n salto de linea, \x00 espacio
print(r"\t \n \" \x20 \-")

#Nos permite limpiar espacios strip(' ') o caracteres strip('d') al principio y alfinal de un string
#rstrip() por default nos limpia de espacios vacios al principio o final del string
frase2='.........,ikoikobananaiko'
print(frase2.strip('.,iko'))

#Separador de string con un delimitador en este caso ,
#replace como su nombre indica reemplaza un caracter/palabra por otro frase.replace('antiguo','nuevo')
print(frase2.split(','), frase2.replace('iko','K'))

#Algunas operaciones comunes de string
print('0x12'.isdecimal())

#Encoding/decode de un string generalmente es por region nosotros usamos el ascii-US o utf-8
fraseEncode='Maincra'.encode('utf-8')
print(fraseEncode.decode())

#Ingreso de datos a un string 
listadoNumeros=[1,2,3,5,6,7]
print('\t'.join(map(str,listadoNumeros)))

#Nos sirve para saber si un string es minuscula,mayuscula o un titulo
#De otro modo tenemos 'holi'.lower(),upper() para transformar un string a el tipo escogido.
print('DS'.islower(),'Cddd'.istitle(),'KIK'.isupper())

#Nos permite saber si un string termina con cierto caracter/frase
print('ThisJourneyEndWith.com'.endswith('.com'))

#En este caso el . es cualquier tipo de caracter y * puede ser 0 o mas ocurrencias
#El () nos indica que es parte de un grupo el contenido que esta entre p y a
print(match('sp(.*)am', 'spa4amx'))