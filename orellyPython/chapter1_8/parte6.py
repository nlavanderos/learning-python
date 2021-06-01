#Dictionaries

#Creacion de diccionario con brackets
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
D['quantity']+=1
D['age']=2
print(D)

#Forma con asignacion 
print(dict(name='pepo',age=20,job='dev'))

#Funcion zip fusiona la lista de keys con sus respectivos values y forma un diccionario.
#Tiene qe ser de la misma dimension o cantidad sino mezcla la cantidad qe es igual en ambas
#en esta caso 3x3 pero si fuera 2x3 mezcla solo 2 elementos.
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob2)

#Diccionarios pueden ser anidados
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
'jobs': ['dev', 'mgr'],
'age': 40.5}

#Se agrega un nuevo trabajo
rec['jobs'].append('janitor')

#Accedo a contenido anidado
print(rec['name']['last'])

#Trabajos
print(rec['jobs'])


pruebaDiccionario={'a': 1, 'b': 2, 'c': 3}

#Condicionales con walrus operator (i:=algo)
if not (i:='d') in pruebaDiccionario:
    print(f'No esta {i} ')

if (i:='c') in (var:=pruebaDiccionario):
    print(f'Se encontro {i} en {var} ')


#Si encuentra algo con el primer argumento del get devuelve su valor,sino devuelve el segundo argumento
valorDiccionario = D.get('food',0)
print(valorDiccionario)

#Condicional en una linea sin uso de :
valorDiccionario2 = D['color'] if 'food' in D else 0
print(valorDiccionario2)

#Aveces en versiones antiguas de python los diccionarios vienen desordenados a como fueron
#instanciados

#Ordenando las llaves
kx=list(pruebaDiccionario.keys())
kx.sort()
print(kx)

#Obtenemos la data de esas key
for key in kx :
    print(key,'=>',pruebaDiccionario[key])



#De otra forma con sorted podemos realizarlo de manera mas eficiente

for key in sorted(pruebaDiccionario):
    print(key,'=>',pruebaDiccionario[key])


