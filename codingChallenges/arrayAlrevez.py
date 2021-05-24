# import numpy as np


# def f1(arr,size):
    
#     arr=np.flip(arr)
#     return ' '.join(map(str, arr))
        
    
# print(f1(size=int(input()),arr=np.array(input().split(), dtype='int')))


def f1(size,lista):
    
    lista.reverse()
    return ' '.join(map(str, lista))
        
    
print(f1(int(input()),input().split()))


