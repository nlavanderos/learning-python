import numpy as np


def ArrayChallenge(arr):

  # code goes here
    if arr==[]:
        return -1

    arr=np.array(arr)
    posicionValorMinimo=np.argmin(arr)
    profit=arr[posicionValorMinimo]
    contador=0

    if (posicionValorMinimo!=len(arr)):
        for i in range(posicionValorMinimo+1,len(arr),1):
            if(profit<arr[i]):
                profit=arr[i]
                contador+=1

    if(contador==0):
        return -1
    else:
        return profit-arr[posicionValorMinimo]
    


# keep this function call here 
print(ArrayChallenge([5,10,4,6,7]))