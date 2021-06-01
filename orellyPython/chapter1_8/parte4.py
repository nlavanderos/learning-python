import re
#: contiene toda la informacion
#Se define un separador ',' a la derecha de :
#.2f deja el resultado a dos decimales y aproxima
print('{:,.2f}'.format(296999.2567))

#el segundo formatting cuando :+05d,el 0 rellena los espacios que no usa el valor-46
#osea 2 espacios en este caso,si se elimina el 0 seran espacios vacios
print(f'{3.14159:.2f} | {-46:+5d}')

#el comando help nos ayuda a ver la documentacion del metodo
#help('holi'.replace)

#dir nos ayuda a ver los posibles metodos en cierto valor
#print(dir('holi'))

#for directories raw string
url=r'C:\Users\Name\Desktop\parte3.py'
print(url)

#string with unicode
stringUnicode='sp\x15m'
print(stringUnicode)

#encoding string
print('spam'.encode('utf8'))

#pattern matching regEx
#() es un grupo
#. es cualquier caracter menos un salto de linea
#* 0,1 o mas ocurrencias de cierto patron ejemplo .* 
#[ \t] es un set de caracteres en este ejemplo un espacio vacio o un tab
#? 0 o 1 repeticion
#+ 1 o mas repeticiones
#$ Significa final del string

match = re.match('Hello[ \t](.*)world', 'Hello Python world')
print(match.group(1))

pal= 'foo1\nfoo2\n'
#re.compile me permite almacenar una expresion regular
#Usando re.MULTILINE como argumento  me permite buscar con salto de linea
c=re.compile("foo.$",re.MULTILINE)


#.finditer(string) busca cuantas veces se repitio la expresion regular
for encontrado in c.finditer(pal):
    print(encontrado)

#delimitadores los set de caracteres [/:] con almacenamiento de grupos(.*)
encontro = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')

#muestra los grupos encontrados
print(encontro.groups())
print(re.split('[/:]', '/usr/home/lumberjack'))