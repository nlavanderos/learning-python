#LOGICA

#'|' COMO TAMBIEN LLAMADO 'or'
#Si son impares ambos valores elige el mas grande
#Si son pares e impares los suma
print(1|3)

#'&' es el llamado 'and',donde es una multiplicacion logica
#aplicado a numeros si son ambos impares es true osea 1
print(1&5)

condicion=True
#negacion de una veracidad con '!' que a su vez es 'not'
print(not condicion)


x=[3,2,3]
d=[1,2,3]
#Interseccion
temp=set(d)
#Con repeticiones
print([i for i in x if i in temp])
#sin repeticiones
print(temp.intersection(x))

#union
print(x+d)

#diff
print(list(set(d)-set(x)))