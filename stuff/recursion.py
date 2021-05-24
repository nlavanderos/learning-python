def count_recursive(n=1):
    """Count to 3, using recursion."""

    if n > 3:
        return 
    
    print('EN LA RECURSIVIDAD')
    count_recursive(n + 1)
    print(n)


lista=[2,5,8,10,7,1,0,25]

def odd(lista):
    i=0
    tipos=[str,int]
    if (lista == [] or type(lista) in tipos):
        return 0
        
    elif (lista[i] == 0) :
        print(True)
        return odd(lista[1:])
    elif (lista[i] == 1) :
        print(False)
        return odd(lista[1:])
        
    else:
        lista[i]=lista[i]-2
        return odd(lista)
        
odd(lista)
count_recursive()


