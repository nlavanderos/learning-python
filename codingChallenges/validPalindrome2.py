
resultado=[]

def veri(low,largo,cadenas,encontrado):

    if(cadenas=='' or cadenas[low]!=cadenas[largo]):
        resultado.append('false')
    elif(cadenas[low]==cadenas[largo]) and encontrado==False:
        resultado.append(-1)
    else:
        resultado.append(encontrado[1])
   


def palindromo(querys,cadenas):
    for i in range(querys):

        if(cadenas[i].strip()==''):
            cadenas[i]=cadenas[i].strip()

        largo=len(cadenas[i])-1
        low=0
        encontrado=False

        while(largo>=low and largo!=0):
           
            #Cuando el primero y el ultimo caracter son iguales
            if cadenas[i][low]==cadenas[i][largo]:
                low+=1
                largo-=1
            
            #Cuando el penultimo y primero son iguales
            if(cadenas[i][low]==cadenas[i][largo-1]):
                encontrado=(True,largo)
                largo-=1

            #Cuando el segundo y ultimo son iguales
            if(cadenas[i][low+1]==cadenas[i][largo]):
                encontrado=(True,low)
                low+=1

            else:

                break
                
                       
            
        veri(low,largo,cadenas[i],encontrado)

    return ' '.join(map(str,resultado))

print(palindromo(3, 'abc mtm '.split(' ')))
#print(palindromo(int(input()), str(input().split(' '))))