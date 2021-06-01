#files

#a agrega alfinal de la linea el contenido de write
#Si el archivo existe hace el append sino
#crea el archivo y agrega la informacion.
with open('orellyPython\parte8.txt','a+') as f:
    f.write('hello\n')
    f.close()

#Lectura solo se necesita read(),pero para guardar el contenido en una lista ise uso de split()
#y elimino el ultimo espacio ya que el separador lo cuenta como caracter.
with open('orellyPython\parte8.txt','r') as f:
    lectura=f.read().split('\n')
    if lectura[-1]=='':
        lectura.pop()

print(lectura)

#Es curioso pero no pueden haber mas de una instancia de lectura por with o open()
#read() muestra solo el string hello en pantalla aplicando caracteres especiales como \n
#readlines() me trae todo el contenido incluyendo los caracteres espciales como \n de manera literal o raw
#readline() para una linea

#Con with no es necesario cerrar el archivo.
#Por el contrario sin with es necesario cerrar el archivo con close()

#El modo w permite escribir y crear un archivo.Pero tambien elimina el contenido del archivo si este
#existia previamente

