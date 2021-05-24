contactos=[]
aux=[]
file=open('contactos.txt', 'r') 
contactos=file.readlines()
file.close()

for ele in range(len(contactos)):
    contactos[ele]=contactos[ele].replace("+",'').replace("\n","")

for numeroElementos in range(len(contactos)):
    i=0
    j=11
    x=len(contactos[numeroElementos])//11
    for enu in range(x):
        aux.append(contactos[numeroElementos][i:j])
        i+=11
        j+=11

print(aux)

