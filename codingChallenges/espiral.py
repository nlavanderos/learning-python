#https://ourcodeworld.com/articles/read/827/how-to-format-a-given-array-matrix-in-spiral-form-snail-or-clockwise-spiral-sorting-in-python
#MATRIX SPIRAL N X M 
def spiral_traversal(matrix):

    resultado = []

    #POSICION INICIAL FILA
    filaInicio=0

    #CANTIDAD DE MATRICES
    filaFin=len(matrix)-1

    #ELEMENTOS EN MATRIZ
    columnaFin=len(matrix[0])-1

    #POSICION INICIAL COLUMNA
    columnaInicio=0


    #Caso base cuando la matriz es vacia.
    if matrix == resultado:
        return resultado


   

    while filaInicio<=filaFin and columnaInicio <= columnaFin:
        
        #SE AUMENTA EL CONTADOR DE FILAINICIO PARA AVANZAR A LA SIGUIENTE FILA
        for i in range(columnaInicio,columnaFin+1):
            resultado.append(matrix[filaInicio][i])
        filaInicio+=1

        #SE RESTA EL CONTADOR DE COLUMNAFIN PARA DENOTAR EL LIMITADOR COLUMNAFIN
        for i in range(filaInicio, filaFin+1):
            resultado.append(matrix[i][columnaFin])
        columnaFin -= 1

        #IMPRIME LOS ELEMENTOS DE LA ULTIMA COLUMNA EMPEZANDO DESDE LA POSICION 1(SI EXISTE)
        #SE REDUCE LA CANTIDAD DE ELEMENTOS POR FILA PARA DENOTAR EL LIMITADOR FILAFIN
        if filaInicio <= filaFin:
            for i in range(columnaFin, columnaInicio-1, -1):
                resultado.append(matrix[filaFin][i])
        filaFin -= 1
        
        #IMPRIME LOS ELEMENTOS ENTREMEDIO HACIA ARRIBA IGNORANDO LOS TOPES DE INICIO Y TERMINO 
        if columnaInicio <= columnaFin:
            for i in range(filaFin, filaInicio-1, -1):
                resultado.append(matrix[i][columnaInicio])
        columnaInicio += 1
    


       
        
    return print(resultado)
       

matrix = [
    [5, 2, 9],
    [6, 3, 10], 
    [8, 1, 31]
]
spiral_traversal(matrix)

#https://leetcode.com/problems/spiral-matrix/