#CHAPTER 8 - Lists and Dictionaries

#Funciones temporales con listas atravez de map 
print(list(map(lambda a:a*a,[1,2,3])))

#Recordar que .sort() es un metodo y sorted(arg) una funcion
lista0=['AFC','aDc','AbC']
#True significa modo descendente
print(sorted([i.lower() for i in lista0],reverse=True))

lista1=[1,200,1000,5]
#Ordena los elementos en forma descendente segun la sentencia if 
#despues vienen los elementos del else en forma ascendente
#- o reverse=True como arguemento ->descendiente 
#  o reverse=False-> ascendiente (sin signo)
lista1.sort(key=lambda a: -a if a%2==0 else a)
print(lista1)

#En cuanto a funciones recordar que existen *args y **kwargs
#*args --> son cualquier tipo de variable/valor
#**kwargs--> son diccionarios keywords arguments
def prueba1(*args):
    return sum(args)

def prueba2(**kwargs):
    return [{key:value} for key,value in kwargs.items()]
        
    
print(prueba1(12,14,15))
print(prueba2(name='Jorge',edad=27))

#Extiende una lista agregando otra lista con datos
lista1.extend([121])

#Remueve todos los elementos de una lista
#lista1.clear()

#Remueve un elemento -> remove(numero)
#Remueve un elemento con slicing-> del l[0]
lista1.remove(121)

#Adicionalmente de la libreria copy junto con sus metodos de copy y deepcopy
#existe copy() una funcion propia de listas y es lo mismo que realizar [::] 

#Similar a la funcion find de string existe index,dado un valor nos devuelve su posicion
print('La posicion del valor 1 es: ',lista1.index(1))

#Existiendo las operaciones append y pop que agregan alfinal de una lista por default
#Sin embargo puede eleminar un elemento por posicion con pop(1),ademas retorna el valor
#Si quieres agregar un elemento sin reemplazar/eliminar existe insert
lista1.insert(2,11)
print('Valor 11 agregado a la posicion 2:',lista1)

lista2=['m  anuel','manuel','manuel','david','david','martin','martin','martin','martin',123]
#Esta linea convierte todo a string para asegurarnos antes un posible error
tem=map(str,set(lista2))
#max recibe el iterable y una key que recoge el valor primer valor de tem y lo compara con la lista3
#No tan solo con el primer item sino con lo que posea el iterable
print(max(tem,key=lista2.count))

#Slice assignment

#Eliminacion/remplazo del elemento 0 y 1
lista1[0:2]=[600,400]
print(lista1)

#Agrega en una posicion sin eliminar
lista1[2:2]=[200,100]
print(lista1)

#Elimina un valor 
lista1[4:5]=[]
print(lista1)

#Agregar al inicio
lista1[:0]=[800]
#Agrega al final
lista1[len(lista1):]=[7,9]
print(lista1)