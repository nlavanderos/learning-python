# CHAPTER 25 :Advanced Module Topics,745

# al importar una var con nombre _a por ejemplo, con from modulo import *
# no se podra visualizar.tendremos que importarla con import modulo y llamarla asi modulo._a

# pero al definir un __all__=[a,_b,c] ,podras usar from modulo import * y llamar _b.Pero
# estara limitado a las variables presentes en all.siexiste otra var en el modulo esta la omitira y producira
# namerror en el script principal


# Al ejecutar una archivo en el cmd,puedes establecer flags propias de python como -m,pero
# al correr un modulo de python y estableces argumentos se pueden llamar con sys.argv


# import sys,parte30
# name='prueba'

#Nos muestra el contenido de __doc__
# print(sys.__dict__['__doc__']) 

#Muestra todo el contenido de sys
# print(sys.__dict__)

#Valores de variables con modulos 
# print(sys.modules['parte30'].name) # Index loaded-modules table manually
# print(getattr(parte30, 'name')) # Call built-in fetch function


#De otra forma podemos establecer variables con nombres de modulos e usar el metodo __import__(nombreModulo)
# >>> modname = 'parte28'
# >>> string = __import__(modname)


#lists the namespaces en stuff
# >>>import nameSpaces
# >>>listing(nombreModulo)

#Recursive Reloader  en stuff
# >>> from reloadAll import reload_all
# >>> reload_all(nombreModulo)

# si usas un import en el modulo tiene que ser con import nombremodulo,no con from ya que 
# de esa formano funciona el reload_all