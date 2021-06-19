from functools import reduce
vardum=180
#Manipulacion de datos en funciones de manera global
def cambio():
    global vardum;vardum = 360
    return vardum

#Manipulacion de datos en funciones de manera no global
xvar='pe'
def fuera():
    xvar='anime'
    print(xvar,end='')
    def dentro():
        nonlocal xvar; xvar='series'
        return xvar
    return dentro()


print(f'Antes: {vardum} Despues: {cambio()}')
print(' >>>>',fuera(),end='\n')

print(reduce(lambda x,y: x+y,[1,2,3,45]))


#sys.modules['name'] == import 'name'


def numero(N):
    def elevado(X): 
        return N ** X 
    return elevado

#se instancia numero(2),me devuelve la funcion elevado sin la llamada entonces...
#al agregar () y un argumento obtenemos un resultado.
print(numero(2)(3))




def mkA():
    #acts de manera local
    acts = []
    for i in range(5):
        #Se debe inicializar i por cada iteracion para que no sean todos los valores el ultimo del rango..en este seria 4
        #sino existiese i=i
        acts.append(lambda x,i=i:i ** x)
    return acts

#acts global
acts = mkA()
print([l(2) for l in acts])


def tester(start):
    state = start # cada llamada obtiene su propio state
    def nested(label):
        nonlocal state # recuerda state en el alcance adjunto/enclosing scope
        #el builtin de nonlocal solamente funciona con variables definidas en un def/funcion anterior,
        # se puede utilizar un global state para compatibilidad con python2.x  global state;state = start
        #la visibilidad del valor de state solamente esta reservado al alcance adjunto
        print(label, state)
        state += 1 # Cada vez que exista una instancia de nested() se incrementare en 1 el valor state y se guardara 
    return nested

acts2=tester(99)
acts2('ham')
acts2('flower')
acts3=tester(28)
acts3('mym')
acts3('plop')

#Cabe destacar que la funcion de nonlocal facilmente se puede reemplazar con una clase y funcion con metodo __init__
#donde eventualmente cada objeto instanciado contara con su funcion de contador de state y imprimir en consola.

# class tester: 
#   def __init__(self, start):
#       self.state = start 
#   def nested(self, label):
#       print(label, self.state) 
#       self.state += 1


#PARA CAMBIAR DETERMINADO BUILTIN(PARA ESTE EJEMPLO USARE OPEN),SE DEBE UTILIZAR:
# import builtins
# def makeopen(id):
#     original = builtins.open
#     def custom(*kargs, **pargs):
#         print('Custom open call %r:' % id , kargs, pargs)
#         return original(*kargs, **pargs)
#     builtins.open = custom