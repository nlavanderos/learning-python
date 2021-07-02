#Storing Objects in a Database
#pickle, dbm(anydbm in python 2.x), shelve

#CREACION: como usar shelve para guardar objetos con su key.
# import shelve
# db = shelve.open('persondb') # Filename where objects are stored
# for obj in (bob, sue, tom): # Use object's name attr as key
#   db[obj.name] = obj # Store object on shelve by key
# db.close() # Close after making changes


#esta libreria de python permite encontrar todos los match de un string
#import glob
#glob.glob('person*')
# ['person-composite.py', 'person-department.py', 'person.py', 'person.pyc',
# 'persondb.bak', 'persondb.dat', 'persondb.dir']

#Lista segun propiedad almacenada en este caso el nombre <obj.name>, con su direccion en memoria.
#print(open('persondb.dir').read())
# 'Sue Jones', (512, 92)

#lectura de informacion cargada en la base de datos.
# print(open('persondb.dat','rb').read())
# b'\x80\x03cperson\nPerson\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00jobq\x03NX\x03\x00

#UPDATE : de valores almacenados usando shelve
# import shelve
# db = shelve.open('persondb') # Reopen shelve with same filename
# for key in sorted(db): # Iterate to display database objects
#     print(key, '\t=>', db[key]) # Prints with custom format
# sue = db['Sue Jones'] # Index by key to fetch
# sue.giveRaise(.10) # Update in memory using class's method
# db['Sue Jones'] = sue # Assign to key to update in shelve
# db.close() # Close after making changes


#TERMINOS ESENCIALES PARA DESAROLLAR EN PYTHON.
#GENERALMENTE EL PRIMER ITEM DESCRITO VIENE CON PYTHON.
#GUIs : tkinter, WxPython and PyQt
#Websites: CGI, Django, TurboGears, Pylons, Flask, web2Py, Zope, or Google’s App Engine
#Web services: Apis,SOAP or XML-RPC
#Databases: SQLite, MySQL, Oracle, or PostgreSQL.ZODB object-oriented database system (OODB),ZODB, for example, is similar to Python’s
#shelve but addresses many of its limitations.
#ORMs: Object-relational mappers (ORMs) like SQLObject and SQLAlchemy can automatically map relational tables and rows to and from Python
#classes and instances