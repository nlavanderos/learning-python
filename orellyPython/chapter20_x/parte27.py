import time,sys


def tiempo(func,*args):

    inicio=time.time()
    for i in range(1000):
        func(*args)
    return time.time() - inicio


def best(repeticiones,func,*args):
    
    best=2**36
    for i in range(repeticiones):
        inicio=time.time()
        #2 elevado a 100
        calculo=func(*args)
        pasado=time.time() - inicio
        if pasado<best:
            iteracion=i
            best=pasado
    return (calculo,best,' :SECONDS','ITERACION: '+str(iteracion))


#Calcula el tiempo que tarda en ejecutarse una funcion 1000 veces,no importa la cantidad de parametros...
print(tiempo(pow,2,1500))

#Reproduce 2 veces un calculo,donde devuelve el qe menos se demoro
for l in range(2):
    print(best(1000,pow,2,1000))

#en una prueba con el script timerBuiltIn.py de la carpeta stuff se obtuvo que,siendo map el builtint mas rapido,con pypy se mejoran aun mas
#los tiempos y la traza de resultados cambia donde map efectivamente es mas rapido que esta traza pero la comprension de lista es aun mas.
# forLoop  : 0.39407 => [0...9999] 0.39403690000000013
# listComp : 0.22715 => [0...9999] 0.2270932000000001
# mapCall  : 0.13000 => [0...9999] 0.12997369999999986
# genExpr  : 0.37568 => [0...9999] 0.3756516000000003
# genFunc  : 0.37425 => [0...9999] 0.37422239999999984


# Otras funciones de time para medir performance
# time.perf_counter () devuelve el valor en fracciones de segundo de un contador de rendimiento
# time.process_time () devuelve el valor en fracciones de segundo de la suma del tiempo de CPU del sistema y del usuario del proceso actual.


#PYPY INTERPRETER ES 7X MÁS RÁPIDO QUE PY INTÉRPRETE, 
# AMBOS EJECUTAN PYTHON SCRIPTS PERO PYPY SOPORTA EN ESTE MOMENTO ,PYTHON SCRIPTS CON 3.8 VER

#USO UTIL PARA TIME,Interactive python usage and API calls
#API:El término API es una abreviatura de Application Programming Interfaces,  
# Se trata de un conjunto de definiciones y protocolos que se utiliza para desarrollar e integrar 
# el software de las aplicaciones, permitiendo la comunicación entre dos aplicaciones de software a través de un conjunto de reglas.


#ejemplo para el caso interactivo
#-3 versionpython -m cargue este módulo e intente ejecutarlo como un script
#-c flag to force timeit to use time.clock
#In this mode timeit reports the average time for a single –n loop, in either microseconds (labeled
#“usec”), milliseconds (“msec”), or seconds (“sec”);
#py −3 -m timeit -n 1000 -r 5 -c "[x ** 2 for x in range(1000)]


#timeit module
#>>> import timeit
# >>> min(timeit.repeat(number=10000, repeat=3,
# stmt="L = [1, 2, 3, 4, 5]\nfor i in range(len(L)): L[i] += 1"))
# 0.01397292797131814

#con un  benchmark module de timeit,se puede ejecutar el script de pruebas en python2.x,python3.x,pypy al mismo tiempo
#es necesario el archivo de benchmark y casos de prueba



#BENCHMARK PYTHON
"""
benchPython.py: Test speed of one or more Pythons on a set of simple
code-string benchmarks. A function, to allow stmts to vary.
This system itself runs on both 2.X and 3.X, and may spawn both.
Uses timeit to test either the Python running this script by API
calls, or a set of Pythons by reading spawned command-line outputs
(os.popen) with Python's -m flag to find timeit on module search path.
Replaces $listif3 with a list() around generators for 3.X and an
empty string for 2.X, so 3.X does same work as 2.X. In command-line
mode only, must split multiline statements into one separate quoted
argument per line so all will be run (else might run/time first line
only), and replace all \t in indentation with 4 spaces for uniformity.
Caveats: command-line mode (only) may fail if test stmt embeds double
quotes, quoted stmt string is incompatible with shell in general, or
command-line exceeds a length limit on platform's shell--use API call
mode or homegrown timer; does not yet support a setup statement: as is,
time of all statements in the test stmt are charged to the total time.
"""

# import sys, os, timeit
# defnum, defrep= 1000, 5 # May vary per stmt
# def runner(stmts, pythons=None, tracecmd=False):
# """
# Main logic: run tests per input lists, caller handles usage modes.
# stmts: [(number?, repeat?, stmt-string)], replaces $listif3 in stmt
# pythons: None=this python only, or [(ispy3?, python-executable-path)]
# """
# print(sys.version)
# for (number, repeat, stmt) in stmts:
# number = number or defnum
# repeat = repeat or defrep # 0=default
# if not pythons:
# # Run stmt on this python: API call
# # No need to split lines or quote here
# ispy3 = sys.version[0] == '3'
# stmt = stmt.replace('$listif3', 'list' if ispy3 else '')
# best = min(timeit.repeat(stmt=stmt, number=number, repeat=repeat))
# print('%.4f [%r]' % (best, stmt[:70]))
# else:
# # Run stmt on all pythons: command line
# # Split lines into quoted arguments
# print('-' * 80)
# print('[%r]' % stmt)
# for (ispy3, python) in pythons:
# stmt1 = stmt.replace('$listif3', 'list' if ispy3 else '')
# stmt1 = stmt1.replace('\t', ' ' * 4)
# lines = stmt1.split('\n')
# args = ' '.join('"%s"' % line for line in lines)
# cmd = '%s -m timeit -n %s -r %s %s' % (python, number, repeat, args)
# print(python)
# if tracecmd: print(cmd)
# print('\t' + os.popen(cmd).read().rstrip())




#CASOS DE PRUEBA
"""
pybench_cases.py: Run pybench on a set of pythons and statements.
Select modes by editing this script or using command-line arguments (in
sys.argv): e.g., run a "C:\python27\python pybench_cases.py" to test just
one specific version on stmts, "pybench_cases.py -a" to test all pythons
listed, or a "py −3 pybench_cases.py -a -t" to trace command lines too.
"""
# import pybench, sys
# pythons = [ # (ispy3?, path)
# (1, 'C:\python33\python'),
# (0, 'C:\python27\python'),
# (0, 'C:\pypy\pypy-1.9\pypy')
# ]
# stmts = [ # (num,rpt,stmt)
# (0, 0, "[x ** 2 for x in range(1000)]"), # Iterations
# (0, 0, "res=[]\nfor x in range(1000): res.append(x ** 2)"), # \n=multistmt
# (0, 0, "$listif3(map(lambda x: x ** 2, range(1000)))"), # \n\t=indent
# (0, 0, "list(x ** 2 for x in range(1000))"), # $=list or ''
# (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"), # String ops
# (0, 0, "s = '?'\nfor i in range(10000): s += '?'"),
# ]
# tracecmd = '-t' in sys.argv # -t: trace command lines?
# pythons = pythons if '-a' in sys.argv


#OUTPUT
# c:\code> py −3 pybench_cases.py -a
# 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)]
# --------------------------------------------------------------------------------
# ['[x ** 2 for x in range(1000)]']
# C:\python33\python
# 1000 loops, best of 5: 499 usec per loop
# C:\python27\python
# 1000 loops, best of 5: 71.4 usec per loop
# C:\pypy\pypy-1.9\pypy
# 1000 loops, best of 5: 5.71 usec per loop
# --------------------------------------------------------------------------------