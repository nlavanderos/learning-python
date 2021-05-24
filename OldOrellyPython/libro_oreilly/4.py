g=(
    (1,2,3),
    (5,4,2)
)
#SIRVE PARA TUPLA O PARA LISTA


h=[]
#EN ESTA LINEA DIGO QUE EL ELEMENTO G[0][0] SE AGREGE A LA NUEVA LISTA H
for i in g:
    for j in i:
        h.append(j)

print(h)
f='cxxxx'
for j in range (2,6):
    
    for i in range(6):
         c= f[:j] 
         print(c,end=' ')
    print('\n')

