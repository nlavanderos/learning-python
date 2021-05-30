def getFirstUpperChar(text) :
    if(text[0].isupper()) :
        return text[0]
    elif(len(text)==1 and text[0].islower()):
        return 'NA'
    else:
        return getFirstUpperChar(text[1:])
    

p='osFaVsas'
print(getFirstUpperChar(p))

#Busca la primera letra mayuscula,en el caso de no encontrar ninguna mayuscula retorna 'NA'