from sys import platform
#\x00 es null character in hexa
#python reconoce distintos string en una sentencia print
print('Googles\t' "of\x20" 'the professor')

#Para desabilitar codigo en development/production, puedes utilizar
"""
print('Piece of Code')
"""
#[slice(start,stop,step)] es lo mismo que [start:stop:step]
#Con la diferencia que los vacios se establecen como None --> [slice(None,None)] == [::]
print('pokemon'[slice(None,None,-1)])

#Character code conversions

#chr() con un unicode obtenemos su caracter
#ord() con un caracter ascii obtenemos su unicode
print(chr(120),ord('x'))

#Resta como valores unicode
print(ord('5')-ord('1'))

#Formating python 2.x
print('Basket Serie: %s Year: %i' %('Kuroko',2018))
S='angelOfTheDead'

# s String (or any object’s str(X) string)
# r Same as s, but uses repr, not str
# c Character (int or str)
# d Decimal (base-10 integer)
# i Integer
# u Same as d (obsolete: no longer unsigned)
# o Octal integer (base 8)
# x Hex integer (base 16)
# X Same as x, but with uppercase letters
# e Floating point with exponent, lowercase
# E Same as e, but uses uppercase letters
# f Floating-point decimal
# F Same as f, but uses uppercase letters
# g Floating-point e or f
# G Floating-point E or F
# % Literal % (coded as %%)


#zfill-Rellena de ceros a la izquierda
#splitlines-retorna una lista cuando existe salto de linea
print(S.zfill(20).splitlines())

#swapcase-cambia mayusculas por minusculas o viceversa
#index/find nos muestra el indice mas bajo para un caracter,en cambio rindex el mas alto index
#isidentifier -nos muestra si es un tipo valido de python
print(S.swapcase(),S.rindex('e'),S.find('e'),S.isidentifier())

#casefold
#count cuenta las ocurrencias de un character enel string
print(S.casefold(),S.count('e'))

#Permite centrar un string y relleno de string
#encambio ljust o rjust justifican el texto to right or left
print(S.center(25,'*'),S.rjust(20,'-'))


# S.translate(map)
# S.maketrans(x[, y[, z]]))

#la expresion %06d,indica que si el numero es menor que 6 caracteres lo rellenara con 0 a la izquierda
#En cambio %-6d ,tendra espacios vacios a la derecha si el numero es menor a 6 caracteres
print('%06d %-6d'%(121,25))

#Dictionary-Based Formatting Expressions

diccionario1={'comida':['apple`s','pear`s'],'values':[123,192]}
print('Tenemos distintas frutas como las %(comida)s con valores respectivos de %(values)s'%diccionario1)

tupla1=(1.29,)
print(f'Actualmente tienes {platform} y en la cuenta ${tupla1[0]}')

#En python2.x tenemos el problema que como no existe el formating f' tenemos que crear una tupla
#De forma anidada
#tupla1=((1.29,),)
#print('%s'%tupla1)

#En python2.x varias funciones de cadenas estan disponibles en la libreria string.