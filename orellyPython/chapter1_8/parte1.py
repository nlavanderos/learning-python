import os
import sys
#Se obtiene el directorio del usuario.
os.getcwd()

#Nos permite saber el sistema operativo.
print(sys.platform)


listadoNumeros=[1,2,4,5,7,6,10,15,11]

#Funcion para determinar si un numero es impar o par.

def valores(p):
    
    for elemento in p:
        
        if elemento%2==0:
            print("El elemento es par: {1} {0}".format(elemento,'♦♦'))
        
        else:
            print("El elemento es impar: ",elemento)
            


valores(listadoNumeros)

#Los tag <> nos permiten saber una informacion que puede ser cambiada pero no se necesitan los tag en el codigo, se usan para resaltar algo.


#Para ejecutar codigo en distintas versiones se hace 
#Por ej: py -3.6 <nombreArchivo.py>
#Mientras que >>python
#Ejecuta la version establecida en el PATH de variables de entorno.

# cd >> cambiar posicion actual
# cd.. >> retroceder posicion actual
#dir > te muestra la posicion actual

#EN CMD
#type <nombreArchivo> nos permite leer el contenido de un archivo sin ejecutarlo


#Para correr un script de manera interactiva y utilizar una funcion especifica se usa:

#python
#from <nombreArchivo> import <nombreFuncion>
#nombreFuncion(<valores>)

#Para correr un script completo y utilizar algo en el codigo no contenido en funciones se usa:
#ejemplo:

# import <nombrearchivo>
# <nombrearchivo>.listadoNumeros


#Para refrescar lo importado tienes que importar la funcion:
#from imp import reload
#se usa reload(nombreArchivo)