

def SearchingChallenge(strParam):

    contador=0
    repeticionElementos=[]
    revisados=[]
    if len(set(strParam))==len(strParam):
        return strParam[0]


    for i in range(len(strParam)):
        if(strParam[i] not in revisados):
            revisados.append(strParam[i])

    for j in range(len(revisados)):
        repeticionElementos.append([strParam.count(revisados[j]),revisados[j]])

    menor=repeticionElementos[0]

    for k in range(1,len(repeticionElementos),1):
        if(menor[0]>repeticionElementos[k][0]):
            menor=repeticionElementos[k]
    
    
    return menor[1]



# keep this function call here 
print(SearchingChallenge(str(input())))