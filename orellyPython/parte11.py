import math

#uso de lambda
x = [2, 4, 5, 6, 8, 12, 7, 33]
#Saca los valores pares ya que son 0(falso) y todo lo diferente a 0 es (true)
#x=filter(lambda x: x%2 ,x)
#saca los valores impares debido a que busca el resto 0
x = filter(lambda x: x % 2 == 0, x)
print(list(x))

#number formatting
x = 1.3597521
#En este caso .2f ,2 es la cantidad de decimales y esta funcion a la vez aproxima.
#Mientras que 10. , rellenara con caracteres vacios si el numero es menor a 10 caracteres
print(f'{x:10.2f}')

#repr forma de codigo,str forma output usual
saludo = 'hola'
print(repr(saludo))
print(str(saludo))


#assert , sirve para testear funciona como un if
#En el caso que sea distinto saldra un error(AssertionError) y este puede ser definido
#con una , despues del condicionante
assert saludo == 'hola', 'El valor no es el requerido'

#(floor) y la operacion (//) nos permite  acercar un numero positivo a su valor entero sin importar deciamles
#cuando es negativo el numero ,si existen deciamles es acercado a su valor mas bajo.
numFloorA, numFloorB = math.floor(2.5), math.floor(-2.01)
print(numFloorA, numFloorB, sep='\n', end='\n')
print(12.5//5, -12.5//5)

#trunc mantiene la parte entera olvidandose de la decimal
numFloorC, numFloorD = math.trunc(2.5), math.trunc(-2.5)
print(numFloorC, numFloorD)

#cabe destacar que en python3.x los integer tienen size ilimitado,eso quiere decir
#que no contiene un subcategoria de tipado  distinto en la categoria integer
#en python2.x existe int y long

#Numeros complejos
#Contienen parte real e imaginaria.
#i en literatura o 1j en programacion.
# Es lo mismo que decir 1j=sqrt(-1) o 1j^2=(sqrt(-1))^2 es lo mismo que -1
print(4j*3j, 2+1j*3, 1j**2)

#Existen built-in de python que facilitan la conversion de una base decimal a otra base
#numeros binarios,son de base 2 es decir 0 al 1
#El calculo para pasar base binario a base decimal es
#1*(2^2)+0*(2^1)+1*(2^0)
print(0b101,bin(5))

#numeros octal,son de base 8 es decir 0 al 7
#El calculo para pasar base octal a base decimal es
#6*(8^2)+2*(8^1)+1*(8^0)
print(0o621,oct(401))

#numero hexadecimal,de base 16 donde 0-9~a-f
#El calculo para pasar base hexadecimal a base decimal es
#10*(16^2)+8*(16^1)+15*(16^0)
print(0xa8f,hex(2703))


#Para transformar un numero a una base determinada se especifica despues de la ,
#en este caso base=2 (binaria) / tambien es valido poner solamente el 2 ,envez de base=2
print(int('100',base=2))

#EVAL,evalua una string dentro de las operaciones built-in
print(eval('0x40'),eval('0b1000000'),eval('0o100'),eval('64'))

print(f'{64:o},{64:x},{64:b}')
