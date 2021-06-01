from math import pi
import random

#Como usar una libreria directamente en un print
print(__import__("math").pi)

#usando la libreria importada
print(f'el valor de pi es {pi}')

#representacion de un valor y su tipo
print(f'valor pi en string {repr(pi)} y el tipo {type(repr(pi))}')

#retorna un valor 0 a 9
print(random.randrange(0,10))
#retorna un valor aleatorio incluido en la lista
print(random.choice([1,2,3,4,5]))

#Como cambiar el contenido de un string
#Convertir el contenido a una lista y con el metodo
#''.join(lista) se genera el string modificado
name='minato'
recorrido=list(name)
recorrido[0]='d'
print(''.join(recorrido))


#bytearrays
c=bytearray(b'juegos')
c.extend(b'depana')
print(c.decode())

#con encondign utf-16,con el metodo decode() no podremos 
#ver el contenido se requiere cambiar el encoding del editor
d=bytearray('estonoes','utf-16')
print(d)

#Operaciones comunes de string pt1
operacionesString='Huevos'
print(operacionesString.find('u'))
print(operacionesString.replace('Hu','Nu'))

#Operaciones comunes string pt2
#podemos ver que se pueden concatenar los metodos
oracion='hola,esto,es,un,ejemplo\n'
print(oracion.upper())
#rstrip elimina los espacios y caracteres vacios a la derecha
#split crea una lista nueva con recorte de ,
print(oracion.rstrip().split(','))
#isalpha ve si los elementos son del alfabeto a...z
print('nones'.isalpha())
print('non121212es'.isalnum())