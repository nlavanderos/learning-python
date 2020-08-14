# random bytearray
random_byte_array = bytearray('ABC', 'utf-8')
print('Before updation:', random_byte_array)

mv = memoryview(random_byte_array)

# update 1st index of mv to -
mv[1] = 45
print('After updation:', random_byte_array)

m = memoryview(bytearray(b'abc'))
mm= m.toreadonly() #SOLO MEMORIA DE LECTURA
print(mm.tolist()) #LISTA LOS VALORES COMO INT 
m[0]=43
print(m.tolist())
m.release() #ESTA LINEA HACE UN CLEAR A LO QUE TENGA EN MEMORIA
m= memoryview(bytearray('afdsdc','utf-8'))
print('El valor en memoria es: '+m.tobytes().decode()+'\ty ',m)
