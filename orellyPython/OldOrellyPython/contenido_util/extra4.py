import itertools as itera
colores=['rojo','azul','amarillo','verde']
posiciones=['derecha','izquierda']
for i,color in enumerate(colores):
    print(i+1,'--->',color)
    #el color puede ser tambien colores[i]


for x,y in itera.zip_longest(colores,posiciones,fillvalue='centro'):
    print(x,y)


#COMBINACIONES DE PARES EN ESTE CASO
#print([''.join(i) for i in itera.combinations_with_replacement('NICOLAS', 2)])
#print([''.join(i) for i in itera.product('NICO',repeat=4)])
#EL PRODUCTO DE REPETIR UN STRING VARIAS VECES EN ESTE CASO EJ NNNN NNNNO NNNNI NNNC NNNIN NNIC

#POSIBLES PALABRAS CON UN STRING

vari=str(input('Escribe un nombre: '))
f = open('txts/nombres{}.txt'.format(vari), 'w')
print([''.join(i) for i in itera.permutations(vari)], file = f)