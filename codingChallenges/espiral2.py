#https://ourcodeworld.com/articles/read/827/how-to-format-a-given-array-matrix-in-spiral-form-snail-or-clockwise-spiral-sorting-in-python
#MATRIX SPIRAL N X M 
def spiral_traversal(matrix):
    resultado = []
    ini=0
    verticales=0
    horizontales=0
    #CANTIDAD DE MATRICES
    largo=len(matrix)

    #ELEMENTOS EN MATRIZ
    extension=len(matrix[0])
    #En caso de que la matriz venga vacia
    if matrix == resultado:
        return resultado

    #Recorre la fila 1
    for elemento in range(ini,extension):
        resultado.append(matrix[0][elemento])
    #recorre la ultima columna
    for ultimo in range(ini+1,largo):
        if ultimo <largo-1:
            resultado.append(matrix[ultimo][-1])
        #recorre la ultima fila menos el primer elemento de esta
        if ultimo == largo-1:
            for algo in range(-1,-extension-1,-1):
                resultado.append(matrix[ultimo][algo])
                # if matrix[ultimo][algo] != matrix[ultimo][0]:
    #recorre la primera columna considerando todo menos el primer y ultimo elemento .
    for primera in range (largo-2,ini,-1):
        verticales+=1
        resultado.append(matrix[primera][0])
                    
    

       
        
    return print(resultado,verticales)
       

matrix = [[1,2,3],
[5,6,7],
[9,10,11],
[13,14,15]]
spiral_traversal(matrix)

#https://leetcode.com/problems/spiral-matrix/