# try/finally combinations come in handy to guarantee that termination actions
# try/except to catch errors raised by code
#No existen problemas al mezclar todos try,except y finally
#Para atrapar los errores comunes, except Exception as x: print(x)

#Creacion de la clase AlreadyGotOne, con argumento la clase Exception
class AlreadyGotOne(Exception): 
    def __init__(self,value):
        self.error=value # User-defined exception

def grail():
    #Genera la excepcion
    raise AlreadyGotOne(402)
    

try:
    grail()

#PUEDEN EXISTIR MULTIPLES EXCEPT Y TERMINANDO PARA TODOS LOS OTROS CASOS CON UN ELSE.
#Cuando se topa con una instancia de AlreadyGotOne, se va a la excepcion
except AlreadyGotOne as x: # Catch class name
    print(x.args,x.__dict__)
    print('Una excepcion encontrada')


#Si la assert es verdadera el string no se mostrara, de lo contrario se mostrara un assertionError con el mensaje del string.
# assert True, 'Nobody expects the Spanish Inquisition!' 


# with statement tiene metodos de sobrecarga __enter__ y __exit__.Generalmente with se usa con manejo de archivos,
#o usar una clase particular como >>>with NombreClase() as action: action.message('test 1').Donde en NombreClase
#debera tener los metodo enter y exit de sobrecarga si requiere un uso customizado no es obligatorio.


#Ademas en un with statement puede haber dos o mas as >>> with open('data') as fin, open('res', 'w') as fout:
#USO TIPICO
# >>> with open('script2.py') as fin, open('upper.py', 'w') as fout:
# ... for line in fin:
# ... fout.write(line.upper())


#Herencia de excepciones con user-defined.
# class General(Exception): pass
# class Specific1(General): pass
# class Specific2(General): pass


#Excepciones al usar una funcion de una libreria
# mathlib.py
# class Divzero(Exception): pass
# class Oflow(Exception): pass
# class Uflow(Exception): pass
# client.py
# try:
# mathlib.func(...)
# except (mathlib.Divzero, mathlib.Oflow, mathlib.Uflow):
# ...handle and recover...


#El nesting con try es posible.
# try:
#     try:
#         action2()
#     except TypeError: # Most recent matching try
#         print('inner try')
# except TypeError: # Here, only if nested handler re-raises
#     print('outer try')


#Traceback a archivo,uso type archivo.exc.
#mientras que en el main del .py se ejecturara bye..
# import traceback
# def inverse(x):
# return 1 / x
# try:
# inverse(0)
# except Exception:
# traceback.print_exc(file=open('badly.exc', 'w'))
# print('Bye')


#Excepciones comunes
# IndexError
# EOFError
# TypeError
# FileNotFoundError
# IOError
# NameError
# ValueError


# Development Tools for Larger Projects
# PyDoc and docstrings
# PyChecker and PyLint
# PyUnit (a.k.a. unittest)
# doctest