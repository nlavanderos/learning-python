#pydoc 
#Documentacion de modulos en forma grafica GUI,en servidor web local
#-m corre el modulo como un script y -b alerta errores de los bytes y los usa como strings
#python -m pydoc -b

#Para un modulo especifico(ej timeit) se usa:
#python -m pydoc timeit

#para un archivo especifico
#set PYTHONPATH=.;%PYTYONPATH%
#python -m pydoc -g

#si no se usa -m se debe establecer un path y utilizar python nombre.py
#el path de todos los modulos generalmente esta en tools/scripts de la carpeta python.


#PARA GENERAR DOCUMENTACION DE UN PROYECTO A HTML SE PUEDE USAR SPHINX O SWAGGER
#PARA SPHINX VER : https://www.youtube.com/watch?v=b4iFyrLQQh4&ab_channel=avcourt
#https://www.sphinx-doc.org/en/master/
#pip install -U Sphinx

#CREAR CARPETA
#sphinx-quickstart
#seleccionar n
#en index.rst debes agregar la palabra modules debajo de :captions para admitir multiples archivos py
#en conf.py descomentar desde os hasta sys 3 lineas y especificar . o .. el directorio actual o el directorio padre
#ademas para generar el html automaticamente debes modificar extensions = ['sphinx.ext.autodoc']
#opcionalmente puedes crear carpeta output
#el punto (.) recoge los modulos del directorio actual sino lo puedes especificar
#sphinx-apidoc -o output . 
#.\make html
#FINALMENTE EN LA CARPETA BUILD HTML ENCONTRAS EL INDEX.HTML CON LA DOCUMENTACION CREADA

#.\make builder 


#DOCUMENTACION DE PYTHON
#http://www.python.org/
