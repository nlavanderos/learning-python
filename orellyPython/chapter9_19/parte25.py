#INVV-investigar libreria tkinter

#eventualmente podria existir un parametro sin *,para usar una funcion osea def example(function,*args,**kwargs)
#*args >>> Non-Keyword Arguments  , **dict >>> keywords arguments
def func(*args,**dict):
    return [args,dict.items()]

diccionario1=dict(kills=8,deaths=5,assist=4)
print(func(1,2,3,**diccionario1))


lista1 = [1, [2, [3, 4], 5], 6, [7, 8]]
#funcion suma el contenido de una lista sin importar si tiene sublistas..
def sumTree(l1):
    tot=0
    for l in l1:
        if not isinstance(l,list):
            
            tot+=l
            print(tot)
        else:
            tot+=sumTree(l)
    
    return tot

print(sumTree(lista1))


#Modificacion de cantidad de recursiones permitidas
#sys.getrecursionlimit(), 1000 por default
# sys.setrecursionlimit(cantidad),permite incrementar la funcion
# help(sys.setrecursionlimit) # lectura de documentacion.


#Funcion para llamar de manera indirecta a otra pormedio de sus argumentos
def echo(m):
    print(m)

def indirect(func, arg):
  func(arg)

indirect(echo, 'Argument call!')


#Nombres de variables contenidas en una funcion en especifica(ej:sumTree)
print(sumTree.__code__.co_varnames)
#Numero de parametros de una funcion.
print(sumTree.__code__.co_argcount)


#Anotaciones en python parametro: <esperado>, def funcion()->tipo de dato que retorna la funcion
#podria establecerse ademas un default value ejemplo: vars: int=6.No es valido para (*)starred expression
def anotacionesPrueba(*vars: int) -> int:
    return sum(vars)
print(anotacionesPrueba(1,2,3))
print(anotacionesPrueba.__annotations__)


#Anonymous function >>> Lambda

#Similarmente en lambda se puede utilizartambien default values 
def Caballeros():
    title = 'Sir'
    action = (lambda x='Anonymous': title + ' ' + x) 
    return action 

act = Caballeros()
print(act(),act('Camilo'))


#Cada elemento x va siendo imprimido despues de utilizar la funcion map
showall = lambda x: [print(ele) for ele in x]
t = showall(['spam\n', 'toast\n', 'eggs\n'])


#Concatenacion de funciones con lambda
print(list(filter(lambda x:x>1,range(-5,5))))


from tkinter import Button, mainloop,Frame 

#Clase para manejo de caracteristicas de ventana tkinter
class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

x = Button(
text='Presiona',
border=5,
height=3,
width=10,
background='red',
command=(lambda:print('Depana '*10,)))

#Configuracion de ventana
myapp=App()
myapp.master.title("Primer interfaz con Tkinter")
myapp.master.maxsize(1000, 400)

#Enpaqueta el contenido del boton
x.pack()

# Inicia el programa,en modo consola es opcional.
# myapp.mainloop()


