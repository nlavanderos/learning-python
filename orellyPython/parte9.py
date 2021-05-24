#Binary Bytes files

import struct

#Existen muchos formatos para este ejemplo
#> BIG ENDIAN byte mas significativo(mbs) a menos significativo(lbs)
#< LITTLE ENDIAN menos significativo(lbs) a mas significativo(mbs)
#i integer,pueden ir de la mano del tamaño por default es 4.
#s char array
#h short integer


#En este ejemplo 4 bytes from 4-byte integer, 
# 4 bytes from the string and 2 bytes from a 2-byte short integer.
#10bytes

packed=struct.pack('>i4sh', 7, b'spam', 8)
print(packed)
print(struct.unpack('>i4sh',packed))

with open('orellyPython/parte9.bin', 'wb') as f:
    f.write(packed)

with open('orellyPython/parte9.bin', 'rb') as g:
    print(list(g.read()))

#115 MEANS DECIMAL NUMBER ,IN OTHERWHISE 1110011 BINARY
#HEX NUMBER FOR UNICODE OF 's'
print(u'\u0073 ')

#NO ES UN ASCII UNICODE TEXT \xc4
s='sp\xc4m'

file = open('orellyPython/parte9.txt', 'w', encoding='utf-8')
file.write(s)
file.close()

#Lectura con el encoding de fuente
text = open('orellyPython/parte9.txt', encoding='utf-8').read()

#Lectura en bruto sin encoding
text2 = open('orellyPython/parte9.txt','rb').read()

#Texto con decifrador y texto con cifrado(encode)
print(text,text.encode('utf-8'))

#Texto sin decifrador y texto con decifrador
print(text2,text2.decode('utf-8'))

#Bytes differ in others ENCODES FOR EXAMPLE : ('latin-1') OR ('utf-16')

#EN PYTHON 2.X
#import codecs
#codecs.open('unidata.txt', encoding='utf8').read()


#Python comes with additional file-like tools: pipes,
#FIFOs, sockets, keyed-access files, persistent object shelves, descriptor-based files, relational
#and object-oriented database interfaces, and more.