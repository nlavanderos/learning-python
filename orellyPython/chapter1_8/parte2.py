#Dos formas de agregar comas y puntos a un valor determinado.

ingreso=int(input('Ingrese un valor: '))
print(f'El valor es el siguiente {ingreso:,}'.replace(',','.'))

ingreso2='125,236,141.      001'
final=ingreso2.translate(ingreso2.maketrans(',.','.,',' '))

print('El valor con translate es : {}'.format(final))


#Me permite revisar todos los nombres en el modulo sean variables,funciones,clases...
#dir(<nombremodulo>)

#Otra manera de ejecutar un codigo de manera interactiva es mediante:
#exec(open(<'nombre.py>).read())
#La ventaja que trae esta manera esque cuando asigno varias variables de formas interactiva y en el codigo importado se uso nombres iguales
#Reasigna todos los valores declarados anteriormente al exec
