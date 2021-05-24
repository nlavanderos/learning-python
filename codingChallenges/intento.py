
def spiralMatrix(m):

    resultado=[]
    filaInicio=0
    columnaInicio=0
    filas=len(m)-1
    columnaElementos=len(m[0])-1

    if m == resultado:
        return resultado
    
    while filaInicio<=filas and columnaInicio<=columnaElementos:

        for i in range(columnaInicio,columnaElementos+1):
            resultado.append(m[columnaInicio][i])
        filaInicio+=1

        for i in range(filaInicio,filas+1):
            resultado.append(m[i][columnaElementos])
        columnaElementos-=1

        if filaInicio<=filas:
            for i in range(columnaElementos,columnaInicio-1,-1):
                resultado.append(m[filas][i])
            filas-=1
            
        if columnaInicio<=columnaElementos:
            for i in range(filaInicio,filas-1,-1):
                resultado.append(m[i][columnaInicio])
            columnaInicio+=1

    return print(resultado)







matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

spiralMatrix(matrix)