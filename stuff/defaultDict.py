from collections import defaultdict

#Metodo que retorna un mensaje default en caso de no existir la key del diccionario
def default_value():
    return 'Not present'

#gracias a la libreria collections importamos la funcion defauldict que nos permite inicializar el 
#diccionario con el mensaje del metodo
#Esto resuelve el mensaje de keyError
diccionario=defaultdict(default_value)
diccionario['a']=1
diccionario['b']=2

print(diccionario['a'],diccionario['b'],diccionario['c'])
