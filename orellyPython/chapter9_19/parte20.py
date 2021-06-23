# menu con sentencia switch implementada

choices = dict(inscribirse={1, 1.0}, cancelar=2, salir=3)
valores = list(choices.values())
llaves = list(choices.keys())
defaultMessage = 'Acabas de elegir la opcion: '
opcion = None
valid = False


def menu():
    global opcion
    global valid
    print('\nBienvenido al sistema de carreras\n')
    print('{:*^33}'.format(''))
    print('{:^30}'.format('1.Inscribirse: '))
    print('{:^30}'.format('2.Cancelar: '))
    print('{:^30}'.format('3.Salir: '))
    print('{:*^33}'.format(''))
    valoresValidos={'1', '2', '3', '1.0'}
    opcion = str(input('Selecciona una opcion: '))
    if opcion not in valoresValidos :
        valid = False
        #El primer argumento es una expresion/valor perteneciente a choices,si lo encuentra retorna lo que contiene el 2do argumento.
        # Handling switch defaults 373
        print(choices.get(False, f'{opcion}  Es una opcion erronea\n'))
    else:
        valid = True


def opciones():
    
    #De igual forma while valid is not True:
    while valid != True:
        
        menu()

    if float(opcion) in valores[0]:
        print(defaultMessage, llaves[0])
    elif int(opcion) == valores[1]:
        print(defaultMessage, llaves[1])
    elif int(opcion) == valores[2]:
        print(defaultMessage, llaves[2])


menu()
opciones()

# pylint + normas pep8 aseguran un desarollo con buenas practicas
# pylint nombreArchivo.py
#En VScode puedes seleccionar todo el texto y elegir formato python que es PEP8 automaticamente


#booleans en sentencias logicas en su mayoria si es verdadero es el valor de la derecha
print(['f', 't'][bool('spam')])

#en este caso elige el primer valor que contenga algo diferente a vacio como asignacion de X
#X=c or a or b
pruebaLista=[1, 0, 2, 0, 'spam', '', 'ham', []]
#Selecciona los valores verdaderos 1 forma con funcion filter()
print(list(filter(bool,pruebaLista)))
#2 forma con comprensionde listas
print([x for x in pruebaLista if x])

#all() si todos los valores son distintos de vacio,0 o False es verdadero
#any() Si el iterable esta vacio es falso

print(all(pruebaLista),any(pruebaLista))