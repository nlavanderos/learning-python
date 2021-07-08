#ENCODINGS

#Default encoding
# Python 2.x: ASCII
#Python 3.x: UTF-8


#Permite saber el encoding actual
#sys.getdefaultencoding()
#cambio el encoding actual
#sys.setdefaultencoding("UTF-8")
# File content, names
#sys.getfilesystemencoding()

#Configuracion de encoding
#al principio del archivo podemos definir el encoding, con la sgt linea.En este caso latin-1
#-*- coding: latin-1 -*-
#a nivel CMD, set variablesPYTHONIOENCODING=utf-8
#script, export PYTHONIOENCODING=UTF-8
#ejecucion de script cmd, PYTHONIOENCODING=utf8 python3 yourprogram.py



#Libreria que exclusivamente estan en un tipo de dato, en este caso bytearray
# S = b'eggs'
# print(S)
# print(str(S,encoding='ascii'))
# print(set(dir(b'abc')) - set(dir('abc')))




# special byte order marker BOM
#forces Python to both skip and write a BOM on input and output, respectively, but the general “utf-8” does not
# open('temp.txt', 'r', encoding='utf-8-sig').read()
# #utf-16-be denotes big-endian format.
# open('temp.txt', 'r', encoding='utf-16-be').read()
# #utf-16-le” denotes little-endian format.
# open('temp.txt', 'r', encoding='utf-16-le').read()


#RegEx
#Learn by doing, https://regexr.com/
import re

#REGEX EN STR
S = 'BugGGgger all dGown here on eGarth!' # Line of text
#Todos las palabras que contengan una G 
regS=(re.findall('(\w*G\S+)', S))
print(regS)

#Cuenta las cantidad de G, agrupada por palabra encontrada
print([x.count('G') for x in regS])


#grupos con exclusion de palabras.
print(re.match('(.*) all (.*) on (.*)', S).groups())


#REGEX EN BYTEARRAY
#B = b'Bugger all down here on earth!'
# re.match(b'(.*) down (.*) on (.*)', bytearray(B)).groups()



# Python 3.X default protocol=3=binary
# ASCII protocol 0,

#pero como pickle(bytes object) basicamente es un objeto contenedor de bytes, seguira siendo bytes aunque cambie el protocolo
#pickle.dumps([1, 2, 3], protocol=0)


# XML Parsing Tools

#1.pattern matching
# import re
# with open('orellyPython\chapter37_41\mybooks.xml') as texto:
#     found = re.findall('<title>(.*)</title>', texto.read())
#     for title in found: 
#         print(title)


#2.we could perform complete XML parsing with the standard library’s DOM parsing support
#https://docs.python.org/3/library/xml.dom.minidom.html

# from xml.dom.minidom import parse, Node
# xmltree = parse('orellyPython\chapter37_41\mybooks.xml')
# for node1 in xmltree.getElementsByTagName('title'):
#     for node2 in node1.childNodes:
#         if node2.nodeType == Node.TEXT_NODE:
#             print(node2.data)


#3.Python’s standard library supports SAX parsing for XML
#https://docs.python.org/3/library/xml.sax.handler.html

# import xml.sax.handler
# class BookHandler(xml.sax.handler.ContentHandler):
#     def __init__(self):
#         self.inTitle = False
#     def startElement(self, name, attributes):
#         if name == 'title':
#             self.inTitle = True
#     def characters(self, data):
#         if self.inTitle:
#             print(data)
#     def endElement(self, name):
#         if name == 'title':
#             self.inTitle = False
# import xml.sax
# parser = xml.sax.make_parser()
# handler = BookHandler()
# parser.setContentHandler(handler)
# parser.parse('orellyPython\chapter37_41\mybooks.xml')

# 4.ElementTree system available in the etree package of the standard library can often achieve the same effects as XML DOM parsers
#https://docs.python.org/3/library/xml.etree.elementtree.html

# from xml.etree.ElementTree import parse
# tree = parse('orellyPython\chapter37_41\mybooks.xml')
# for E in tree.findall('title'):
#     print(E.text)



# 5.XPATH XML con libreria lxml 4.6.3 >>>combina las librerias libxml2/libxslt 
#https://lxml.de/xpathxslt.html#xpath
#otras alternativas son -> liberias PyXML,xpath,Amara.

# from lxml import etree
# doc = etree.parse("orellyPython\chapter37_41\mybooks.xml")

# #Es buena practica obtener el root de los tag
# #root = doc.getroot()

# #1.La busqueda puede ser realizada con sintax propio de xpath
# #etree.XPath("count(//*[local-name() = $name])")
# #2.tambien puede ser realizada con '/books/title'

# busqueda=doc.xpath('title')
# cont=0
# for x in busqueda:
#     print('Traza')
#     #No es necesario especificar el tag, ya que la hereda de x.Mas bien x.iter('title') es para establecer 
#     # otro elemento a buscar o dejarlo detallado
#     for j in x.iter():
#         cont+=1
#         print(j.tag,j.attrib,j.text)

# #Cantidad de elementos con el tag title, incluyendo si tiene hijos asociados
# print(cont)


#The XML processing modules are not secure against maliciously constructed data.
#https://docs.python.org/3/library/xml.html#xml-vulnerabilities

#Use of this package is recommended for any server code that parses untrusted XML data
#https://pypi.org/project/defusedxml/