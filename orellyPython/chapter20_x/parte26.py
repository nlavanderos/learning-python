from os import walk
from random import randint

#Inicializo matrix
matrix1 = [[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]]

mTop=len(matrix1)-1
#Diagonal 1,5,9
print([matrix1[i][i] for i in range(mTop+1)])
#Diagonal 7,5,3
print([matrix1[i][mTop-i] for i in range(mTop,-1,-1)])

#Los comprehension son buenos pero es mala practica usarlos en ciclos anidados,porque se hace dificil para mantenibilidad de codigo.
#KISS principle: Keep It Simple Sir

#Puede existir mas de un yield es una misma funcion
def gen(N):
	for i in range(N):
		yield i*i


for acumuladorYield in gen(5):
	print(acumuladorYield,end=' YIELD ')

#Eventualmente si esta en scope global o de funcion se puede seguir usando el valor de la variable para recorrer el yield
acumuladorYield+=23
print(acumuladorYield)

#Usando el modulo os,con la funcion walk podemos buscar en un directorio especifico los archivos.
busquedaArchivos= walk(r'orellyPython\chapter9_19')
print([l for l in busquedaArchivos])

#subs busca todas las sub carpetas y las retorna como listas
#root busca todas las carpetas con su directorio relativo
#files archivos presentes en el directorio actual excluyendo nombre carpetas
for (root, subs, files) in walk('.'): # Posiciona el buscador en el directorio actual
	for names in files:
		#Funciona como un find de windows/linux en python
		if names.startswith('README'):
			print(names,root,end=' <<< EN DIRECTORIO FUE ENCONTRADO \n')




#Uso de send con yields.
def cf():
	while True:
		#Cada valor enviado por send es imprimido y multiplicado x2
		val = yield
		print (val*2,end=' ')

def pf(c):
	while True:
		#Genera valor y lo manda a funcion cf()
		val = randint(1,10)
		c.send(val)
		#Se usa yield para establecer limites,dependiendo de un rango en este caso 10 sino se ejecuta eternamente
		yield
		


c = cf()
#Se debe inicializar el sender con None cada vez que queramos usar la funcion send
c.send(None)
p = pf(c)

for wow in range(10):
	next(p)


#PERMUTACIONES CON YIELD SIN USO DE LA LIBRERIA itertools

def permutacion(N):

	if len(N)==1:
		yield N
	else:

		for i in range(len(N)):
			rest = N[:i] + N[i+1:]
			
			for j in permutacion(rest):
	
				yield N[i:i+1]+j


#Traza, combinaciones para primera iteracion del primer rango i=0 .. osea 1,2,3 y 1,3,2
# i=0
# for i in range(3):
# 	rest = N[:i] + N[i+1:] ,donde rest es [2,3]
# 	for j in f(2,3):
# 		yield [1]+f(2,3)

# >>EN 0
# yield[1]+(YIELD[2]+[3])
# >>EN 1
# yield[1]+(YIELD[3]+[2])

listadoPermutaciones=permutacion([1,2,3])
print([l for l in listadoPermutaciones])

