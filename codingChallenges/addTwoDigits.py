def addTwoDigits(n):
    sumatoria=0
    for id,elemento in enumerate(str(n)):
        sumatoria+=int(elemento)
    return sumatoria  

resultado=addTwoDigits(29)
print(resultado)

