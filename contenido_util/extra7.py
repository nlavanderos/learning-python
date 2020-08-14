
import numpy
import timeit

numero=str(input('Ingresa numero cientifico: '))
decimal,exponente = numero.split('e-')
a, b = decimal.split('.')
print('0.'+'0'*(int(exponente)-1) + a + b)


#DE ESTA FORMA PODEMOS EJECUTAR 10000 VECES UNA FUNCION PARA SABER CUANTO SE DEMORA EN HACER ESAS ITERACIONES
cod='''
def arigato():
    numerazo=[[1,7,5],[2,4,5],[3,2,1]]
    nn=(sum(ab) for ab in numerazo)
    suma=0
    for val in nn:
        print(val)
        suma+=val
    print(suma)    
'''
#ESTO PERMITE QUE NO SALGA COMO NUMERO CIENTIFIICO SI ES MUY CHICO O GRANDE
print(numpy.format_float_positional(timeit.timeit(stmt=cod,number=1,))+' seconds')