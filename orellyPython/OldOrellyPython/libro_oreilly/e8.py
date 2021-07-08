"""
LISTAS o'relly
"""

M = ['bb', 'aa', 'cc']



def ordenada_alrevez(a):

 print('LISTA INICIAL',a)
 print('LISTA ORDENADA al revez',sorted(a,reverse=True))
 print('LISTA ORDENADA ',sorted(a))
 
 

#SLICING REMEMBER START:STOP:STEP
#EN ESTE CASO TODO EL ARRAY Y AVANCE DE ATRAS -1 -2 -3 

ordenada_alrevez(M)
print('CON SLICING {}'.format(M[::-1]))


B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]] 

sacandoItem=[row[1] for row in B]
print(sacandoItem)
sacandoItem2=[row[1] + 1 for row in B]
print(sacandoItem2)
sacandoItem3=[row[1] for row in B if row[1] % 2 == 0]
print(sacandoItem3)

diag = [B[i][i] for i in [0, 1, 2]] 
print(diag)
doubles = [c * 2 for c in 'goku']
print(doubles)
#Range parte de 0 hasta el numero del rango,el siguiente argumento es el limite y que por cierto
#no se incluye y el tercer argumento  es el avance

elevados=[[x ** 2, x ** 3] for x in range(4)] 
print(elevados)
elevado_condicional= [[x, x // 2, x * 2] for x in range(-6, 7, 2) if x > 0]
print(elevado_condicional)

suma_matricial = (sum(row) for row in B)
for x in suma_matricial:
    print(x)

#165 quede
#next(suma_matricial) se usa para avanzar en los valores del row de la suma total de cada iteracion
