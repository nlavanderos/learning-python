import timeit


c=bytes([25])
d=int.from_bytes(c,byteorder='big')
print(c,d)
#FORMAS DE CONVERTIR UN INT A BYTES ,TIEMPOS DE EJECUCION

#LA SEGUNDA ES LA MAS RAPIDA,B por standard size tiene 1 en cambio i 4

#print(timeit.timeit('bytes([255])', number=1000000))
#print(timeit.timeit('struct.pack("B", 255)', setup='import struct', number=1000000))
#print(timeit.timeit('(255).to_bytes(1, byteorder="little")', number=1000000))

g=(10000).to_bytes(2,byteorder="little")
print(g)

palabra_magica= "Python is interesting."

# string with encoding 'utf-8'
arregloPalabra = bytearray(palabra_magica, 'utf-8')
print(arregloPalabra)
print(arregloPalabra.decode())