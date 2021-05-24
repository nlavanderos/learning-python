#Tuples 
#Interactive CODE

#This function shows the output of the data regardless of the arguments
def imprime(dato,*kwargs):
    print(dato,*kwargs)

miTupla=(1,2,3,2,2)
imprime(len(miTupla))

#Adicion temporal de dos elementos a la tupla
imprime(miTupla+(6,7))

#Mustra la posicion del elemento 2 solo una vez
#tambien muestra la cantidad de veces que el elemento se repite
imprime(miTupla.index(2),miTupla.count(2))

miTupla = (2,) + miTupla[1:]
imprime(miTupla)

#La tupla no tiene la funcion append ni pop asociada pero al contener una lista en la posicion 2
#se puede hacer uso de las funciones de listas
miTupla = 'spam', 3.0, [11, 22, 33]
miTupla[2].append(22)
imprime(miTupla)