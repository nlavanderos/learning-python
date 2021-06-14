# import numpy as np


# def f1(arr,size):
    
#     arr=np.flip(arr)
#     return ' '.join(map(str, arr))
        
    
# print(f1(size=int(input()),arr=np.array(input().split(), dtype='int')))

#F1
#INGRESAR SIZE >>> 3
#INGRESAR LISTA >>> 1 2 3
def f1(size,lista):
    
    lista.reverse()
    return ' '.join(map(str, lista))
        
    
print(f1(int(input()),input().split()))


