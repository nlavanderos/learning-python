'''En ese archivo veras informacion relacionada a listas'''
#De esta forma agregas una descripcion cuando haces referencia a help(parte5) de manera interactiva
#Las funciones tambien pueden contener docstring


#Para tener el contenido de filter se necesita hacer uso de la funcion list() o usar un for.
#Porque filter retorna el resultado con yield.
l=[i**2 for i in range(10)]

def par(x):
    '''Esta funcion retorna ,si el elemento es par'''
    return x % 2==0

l=filter(par,l)
print(list(l)[::2])


#Modificacion de la lista,para ordenarla desde el ultimo elemento al primero con reverse()
listFunciones=[2,2,3,4,5,6]
listFunciones.reverse()
print(listFunciones)

#Funcion para agregar un elemento en una posicion determinada
listFunciones.insert(6,'Holi')
print(listFunciones)

#remove() nos elimina el elemento deseado una vez,usando un for se pueden eliminar todos los
#otras repeticiones de dicho elemento.
for algo in range(len(listFunciones)):
    try:
        listFunciones.remove(2)
    except ValueError:
        pass
print(listFunciones)


#COMPRENSION DE LISTAS ----> LIST COMPREHENSION

M = [[1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]]


#valores de la columna 3,internamente en el (row in m)  el campo row seria row[fila]
# Despues seleccionamos el campo que queremos siendo 2 ,quedaria row[fila][2]  
print( [row[2] for row in M])


#a la 3 columna se le sumara 1 a cada elemento 
print([row[2] + 1 for row in M])


#Condicionales en list comprehension
print([row[2] for row in M if row[2] % 2 == 0])


#diagonal en matriz,con dos formas
#1 forma con rango dinamico y otra con rango estatico
print([M[i][i] for i in range(len(M))])
print([M[i][i] for i in [0, 1, 2] ])


#Generar una lista con list comprehension
print([[x ** 2, x ** 3] for x in range(4)])


#recordar que range() es como el slicing de una lista lista[start:stop:step] entonces range(start,stop,step)
print([[x, x // 2, x * 2] for x in range(-6, 7, 2) if x > 0])


#Dado que sum contiene los yield de row y a su vez el metodo iter()
#Sera necesario hacer uso de next(G) para saber el contenido de la suma
#Lo bueno del uso de sum esque es por la iteracion completa de una lista y no es el total de la matriz 
G = (sum(row) for row in M)

#Finalmente cada iteracion de next(G) me trae la suma de la fila iterada
print([next(G) for iteracion in range(len(M))])

#De otra forma,usando map se consige lo mismo qe en list comprehension
#la funcion map como argumentos necesita una funcion y los valores(funcion,valores)
print(list(map(sum, M)))


#Con syntaxis de comprehension puedes crear listas,sets,diccionarios y generadores

#SET no admite duplicados
print({sum(row) for row in M})

#Diccionario key:value, en este caso a sum se le paso la fila entera
print({i : sum(M[i]) for i in range(3)})

#Generador de valores,retorna yield para ser usado con la concatenacion del metodo iter() y finalmente next()
print((ord(x) for x in 'spaam'))


    
#Cada caracter sera transformado a mayuscula con upper()
for caracter in 'fizz':
    print(caracter.upper())

#While

x=4
while (x>0):
    print('Spam!!!!'*x)
    x-=1