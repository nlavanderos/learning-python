#1 METODO DE IMPORTACION DE DISTINTA RUTA
#Agrega a variables de entorno de python,la ruta relativa donde se encuentra el modulo.
# import sys
# sys.path.append('orellyPython\chapter9_19')
#nombre del modulo
# from parte20 import  menu,opciones


#METODO 1.5
#Lo mismo pero con prioridad
#sys.path.insert(1, "./model")
#tambien parent directory 
# sys.path.append ( '.')

#METODO 2 (python 2.x)
#Es crear archivo vacio __init__.py
#donde la manera de importar son las carpetas contenedores de ese init
#ejemplo  orellyPython.chapter20_x.nombreModulo


#Sirve para primar los nombres globales del archivo actual vs uno con el mismo nombre pero importado.
# tambien se ejecuta la funcion solo cuando es ejecutado no cuando es importado
# if __name__ == '__main__':
#   somefunc()


#modulo os,import os
#la ruta absoluta del archivo actual
# absolutepath = os.path.abspath(__file__)

#directorio actual
# print(os.getcwd())
#cambia el directorio actual
# os.chdir("PATH")

#directorio del archivo actual,lo mismo qe absolute path
fileDirectory = os.path.dirname(absolutepath)

#Ruta del directorio padre
parentDirectory = os.path.dirname(fileDirectory)

#navega a ruta meme
newPath = os.path.join(parentDirectory, 'meme') 


#en cmd puedes configurar el encoding,path de python
# set PYTHONIOENCODING=utf-8
#set PYTHONPATH=C:\code
