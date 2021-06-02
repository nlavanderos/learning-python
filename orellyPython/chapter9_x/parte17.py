from collections import namedtuple

#1ra Forma de instanciar una tupla
tupla1 = 0, 'Ni', 1.2, 3

#2da forma de instanciar una tupla -> tuple())
print(tupla1,tuple('spam'))
#ademas tuple sirve para hacer unpacking de un interable osea x ejemplo
#tuple(diccionario.values())


#3 forma de instanciar una tupla
print(('hello','world'))

#Tupla con clase
#1 forma de instanciar una namedtuple,aceptas campos con mismo nombre
pruebaNameTuple=namedtuple('Emp', 'name jobs jobs',rename=True)
print(pruebaNameTuple._fields)

#2 forma de instanciar una namedtuple
Emp=namedtuple('Emp', ['name','jobs'])
#Nos muestra la clase y los argumentos que podemos darle
print(Emp.__doc__,Emp._fields)
empleado=Emp('Juan',('arquitecto','diseñador'))
print(empleado.name,empleado.jobs)

#El indexing en tupla funciona similar como en listas
#Para ordenar una tupla debes usar sorted(),envez de convertirla a lista y despues a tupla.

tupla2=(1,2,3,4,5,2,1,6,7,2)
#el primer parametro busca el index del numero deseado,pero el segundo argumento
#indica para este caso que busca el 2 despues de la posicion 6
print(tupla2.index(2,6))

#La gran caracteristica de la tupla esque no pueden ser reasignado los valores
#tupla2[1]=2

#convertir una tupla a diccionario
#tupla._asdict()

#unpacking de una instancia namedtuple a variables
# name,jobs = empleado
# print(name,jobs)

#Files

#Modos mas utilizados
#W-cada vez que se abre con este modo escribe y borra la info que estaba
#a- agrega alfinal informacion
#r-lectura
#+ -> Permite que la escritura y lectura

#Si un archivo necesita encoding unicode,se realiza lo siguiente.
# open('f.txt', encoding='latin-1') Python 3.X Unicode text files (str strings)

#LECTURA de cadenas de bytes
#data= open('f.bin', 'rb').read() Python 3.X bytes files (bytes strings)
#la informacion binaria puede ser tratada de la forma que desemos
#si la leemos sin especificar vendra en bytes pero si deseamos puede ver como string
#realizando slicing  data[4:8] por ejemplo
#tambien podemos obtener cierto unicode data[4:8][0],de igual forma puede ser en binario
#bin(data[4:8][0])

#LECTURA DE UN ARCHIVO EXISTENTE Y ESCRITURA SINO EXISTE
try :

    #Se especifica la ruta en el open funciona con relative path,para path se debe usar raw string r'
    lectura = open('orellyPython/chapter9_x/p17_1.txt', 'r')

    print(lectura.read())
    #read() -> lee toda la informacion del archivo
    #readline() -> lee una linea del archivo,generalmente se usa en un ciclo for
    # for line in open('myfile.txt'): 
    #     print(line, end='')
    #readlines() -> lee toda la informacion del archivo por lineas,almismo tiempo almacena en una lista la info.
    

except FileNotFoundError:

    escritura=open('orellyPython/chapter9_x/p17_1.txt',mode='w')
    #al escribir informacion con print(),alfinal del contenido siempre habra salto de lineas
    #con write(),nosotros debemos especificar si queremos un salto de linea por ejemplo.
    #escritura.write('holaMundo\n')
    print('holi',file=escritura)

finally:
    
    #Siempre se debe cerrar un archivo,en el unico caso que no se realiza es cuando
    #se usa la sentencia with -> with open(....) as f: sentencias....
    lectura.close()
    #Sin cerrar el archivo se puede hacer un flush al buffer.
    #lectura.flush()

    #lectura.seek(N)
    #Permite cambiar la posicion del archivo a algo(en este caso N) para la siguiente operacion


#REMUEVE EL FINAL DE LINEA 
#line = data.readline()
#line.rstrip()

#para dividir el contenido en una lista
#parts = line.split(',')

#para eliminar caracteres especiales en una lista,facilmente se puede realizar con comprension de listas.
# f=['43', '44\t', '45\n']
# print([int(algo) for algo in f])
