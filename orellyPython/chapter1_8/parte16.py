from collections import defaultdict
import dbm # Named anydbm in Python 2.X

#Dictionaries

#Instancia de diccionario con lista y tuplas conteniendo key,value
#diccionario1=dict([('name','seba'),('edad',35)])

#Permite establecer una key en caso que no especifique
#diccionario1.setdefault('profesion',None)

#defaultdict
def def_value():
    print('La key no existe')
    return None
    
#Se establece un mensaje en caso de que una key no exista,ademas se agrega la key pero con valor None 
#Forma de tuplas en diccionarios
diccionario1=defaultdict(def_value,[('name','seba'),('edad',35)])

#Forma con defaultdict y definiendo tipo de dict
# diccionario1=defaultdict(list)
# diccionario1['name']='seba'
# diccionario1['edad']=25

#Creacion de un diccionario apartir de las llaves
print(dict.fromkeys('amx', 0))
print(dict.fromkeys(['amx'], 0))

#Creacion de diccionario al unir dos listas con keys y values respectivamente
print(dict(zip(['profesion','herramienta'],['SC','python'])))

#busca unas llaves en un diccionario
print('edad' in diccionario1)

#key,value en forma de tupla con items()
#keys() muestra las distintas keys en el dict,similarmente para values() 
print(diccionario1.items(),diccionario1.keys(),diccionario1.values())

#Genera una copia de un diccionario
#variable=diccionario1.copy()

#elimina todo el contenido de un diccionario
#diccionario1.clear()

#Agrega una key y su respectivo valor sino existe,en caso de que exista se reemplaza 
diccionario1.update({'asignatura':'matematicas'})
print(diccionario1)

#para eliminar el ultimo item
#diccionario1.popitem()

#Para eliminar un item especifico
#diccionario1.pop('edad')
#del diccionario1['edad']

#obtener el valor de una key
print(diccionario1.get('asignatura'))

#cambiar el valor de una key
diccionario1['asignatura']='Lenguaje'
diccionario1['x']
diccionario1['y']

#De esta manera eliminamos los registros None
diccionario1={key:value for key,value in diccionario1.items() if value!=None}
print(diccionario1)

#forma tradicional de diccionarios
diccionario2 = {'1975': 'Holy Grail','1979': 'Life of Brian','1983': 'The Meaning of Life'}

for year in diccionario2:
    print(year+'\t'+diccionario2[year])

#la key no existe,pero de esta manera estamos llamando y asignando un valor
diccionario2[99]='elementoPrueba'
print(diccionario2)

#Forma de keywords para diccionarios
print(dict(raza='pastorAleman',nombre='koke'))

#tuplekeys
Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
print(Matrix[(2,3,4)])

#Si no existen las keys
#1 forma -> if/else
if(2,3,6) in Matrix:
    print(Matrix[(2, 3, 6)])
else:
    print(0)
#2 forma -> try/catch
try:
    print(Matrix[(2,3,6)])
except KeyError:
    print(0)
#3 forma -> get con argumento de default sino lo encuentra
print(Matrix.get((2,3,6),0))


diccionario3={'b': 2, 'c': 3, 'a': 1}
for k in sorted(diccionario3): print(k, diccionario3[k])

#comparacion de magnitudes
#sorted(D1.items()) < sorted(D2.items())


'''
file = dbm.open("filename",flag='c') # Link to file
informacion=dict(name='nicolas',dev='Fullstack')
file['https://github.com/nlavanderos'] = 'nombre: {} profesion: {}'.format(informacion['name'],informacion['dev'])# Store data by key
data = file['https://github.com/nlavanderos'] # Fetch data by key
print(data)


#Apartado de cgi en carpeta stuff/webCgi y learning-python/cgi-bin
'''