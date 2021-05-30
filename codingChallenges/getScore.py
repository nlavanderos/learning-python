def getScore( values ) :
	contador=0
	for i in range(len(values)):
		if i%2==0:
			contador+=3

	restaImpar=list(filter(lambda values: values%2 ,values))
	contador-=len(restaImpar)*2
	return contador

a=[2,3,5]
print(getScore(a))

#Se suma 3 a contador con indices pares
#Con valores impares se le resta 2 por cada aparicion