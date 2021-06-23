#__NAME__ Y __MAIN__
# There is a really nice use case for the __name__ variable, whether you want a file 
# that can be run as the main program or imported by other modules. 
# We can use an if __name__ == "__main__" block to allow or prevent parts of code
# from being run when the modules are imported.


#COMO FUNCIONA UN IMPORT
#1. Busca el archivo del módulo.
# 2. Compíla en código de bytes (si es necesario).>>>>>>en python3.x se cra carpeta __pycache__,con archivo .pyc.En python2.x se crea solo
#el archivo .pyc
# 3. Ejecuta el código del módulo para construir los objetos que define.


#Se pueden anadir carga de librerias creando un archivo  pydirs.pth,en el root del interprete de python 
#donde pydirs debe conter por ejemplo c:\pycode\utilities
#COMO tambien en las variables de entorno de windows especificando una carpeta contenedora



# Python also supports the notion of .pyo optimized byte code files, created and
# run with the -O Python command-line flag

#RECORDAR el from imp import reload ,es util en sesion interactiva con python
# >>>>Proporciona una forma de volver a cargar el código de un módulo sin detener Python
# >>> from imp import reload
# >>reload(changer)


#Como llamar una funcion de otro archivo
#ejemplo archivo f1.py 
#contiene def imprime(texto):
#print(texto)

#en archivo llamada.py 
#import f1
#instanciamos f1.imprime('Shingeki')



#FORMAS DE IMPORTAR UN ARCHIVO/MODULO
# import modulo1  >>> importa todo lo que contiene el archivo con el prefijo modulo1,osea una funcion seria modulo1.funcion()
# import modulo1 as md1>> renombra el prefijo a md1.funcion()
# from modulo import printer >> del modulo solo importa la funcion printer,para instanciarla solo es necesario usar printer() sin el prefijo
# from modulo1 import * >> importa todas las funciones,variables del modulo sin el prefijo modulo1


#Desde un archivo importado podemos instanciar los argumentos de funciones sin problemas al igual que una propiedad de clase.
#import dm
# dm.x=1200
# print(dm.x)

#En este caso importa el valor de x pero como existe una asignacion de x,prioriza el x del archivo actual.
#Distinto seria si existe un print(x) antes la asignacion de x
# from dm import x 
# x=111111
# print(x)

#ES BUENA PRACTICA IMPORT LAS MODULOS AL PRINCIPIO DEL SCRIPT,PERO DE IGUAL MANERA FUNCIONAN SI SON DECLARADOS ABAJO.

#Como saber el contenido de un import sin ejecturarlo?
#list(modulo.__dict__.keys())
#Solamente lo creado por el programador
#list(nombre for nombre in modulo.__dict__.keys() if not name.startswith('__'))



#Se puede pedir un valor de multiples archivos/modulos.
#en un archivo hipotetic m1.py existe el siguiente script
# X = 1
# import m2
# print(X, end=' ') # My global X
# print(m2.X, end=' ') # mod2's X
# print(m2.m3.X)

#m2.py contiene
# X = 2
# import m3
# print(X, end=' ') # My global X
# print(m3.X)

#m3.py
#X=3

#La traza de m1.py es la siguiente:
#Dado la importacion m2,que incluye imprimir por consola.
#2 3
#Posteriormente imprime el contenido de m1.py
#1 2 3 
#m2.m3.X significa que en el modulo <m2>,existe la importacion del modulo m3.En ese escenario pedimos el valor de X en m3