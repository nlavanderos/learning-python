
def strangeCounter(t):
	cantidadDeElementos=0
	#Iteracion sera el multiplicador del valor inicial 3
	iteracion=0
	while (cantidadDeElementos<t):
		cantidadDeElementos+=3*(2**iteracion)
		iteracion+=1
	return cantidadDeElementos-t+1
	


	
print(strangeCounter(1023))
