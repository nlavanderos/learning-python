#FORMA DE SABER EL PATH EN QUE ESTAMOS Y 2 FORMAS DE SABER EL SISTEMA OPERATIVO COMO NT 2.1 O  2.2 WINDOWS
import sys
import os
import platform as pf
print('El entorno de trabajo es : {0}'.format(sys.platform))
print(os.getcwd())
print(os.name)
print(pf.system())