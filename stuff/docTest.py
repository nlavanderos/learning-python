def impar(n):
    '''
    La función impar(n) devuelve:
    -  True: si número es impar
    - False: si número no es impar
    >>> impar(0)
    False
    >>> impar(1)
    True
    >>> impar(2)
    False
    >>> impar(3)
    True
    '''
    if n%2 != 0:
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()

#Con python <nombreArchivo.py> -v
#me muestra un informe de la traza -v:verbose 

#Omitiendo la clausula if
# python3 -m doctest fmatemat1.py -v
#-m mod: run the library module as a script.