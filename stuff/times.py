from time import time
from timeit import timeit

#Mediciones de tiempo

#timeit mide el tiempo de ejecucion de una linea de codigo,se pueden agregar funciones de libreria
#o funciones creadas por uno con setup=''
#El primer print para retornar el tiempo y el otro print en timeit para retornar el valor
print(timeit(stmt='print([elementos for elementos in range(10)])',number=5))


#Mientras que time tiene que ser inicializado en alguna parte del codigo para tomar el valor inicial
# y el time() del final nos devuelve el tiempo que se demoro en llegar hasta el ultimo print
inicio=time()
print([elementos for elementos in range(10)])
print(time()-inicio)