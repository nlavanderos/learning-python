import random
caracteres='0123456789@!#$%^&*()aeioumnbvcxzsdfghjklñpytrwq?/><,.;\'":}{[]+=_-~`AEIOUMNBVCXZSDFGHJKLÑPYTRWQ'
#Se convierte el string en una lista,siendo cada caracter un indice distinto.
orden=list(caracteres)
#Se ordena la lista creada con el metodo shuffle de la libreria random
random.shuffle(orden)

nombre=input('Ingresa el nombre del archivo: ')
cantidad=int(input("Ingresa la cantidad de generaciones de contraseñas: "))
extension=int(input("Ingresa la extension de las contraseñas: "))


def crearContra(extension,cantidad):
    clave=''
    listadoDeClaves=[]
    for j in range(cantidad):
        for i in range(extension):
            #Join permite agrega un caracter de determinado string
            #El metodo SystemRandom() es mas seguro que usar random.randrange()
            #Porque depende del sistema operativo y hace que el proceso mas lento como tambien seguro.
            clave+=''.join(orden[random.SystemRandom().randrange(0,len(caracteres))])

            if (extension-1 == i):
                listadoDeClaves.append(clave)
                clave=''
                
    return listadoDeClaves

resultados=crearContra(extension,cantidad)

#Con esta forma no es necesario cerrar el archivo.
with open(f"{nombre}.txt","w") as file:

    for resultado in resultados:
        file.write(resultado+'\n')

#Con la forma tradicional se realiza
#variable=open(f"{nombre}.txt","w")
#operaciones asociadas a lectura o escritura...
#variable.close()

