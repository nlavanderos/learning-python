#!LUGAR INSTALACION PYTHON
# -*- coding: utf-8 -*-
from http.server import HTTPServer, CGIHTTPRequestHandler
class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]
httpd = HTTPServer(("", 8000), Handler)
httpd.serve_forever()

#python
# Crear los metodos http para montar el server
#Crear carpeta del cgi-bin y script
#crear carpeta de archivos html
#finalmente en localhost:8000/c.html


#XAMPP
#Donde cgi-bin ya esta creada en la carpeta root,deberas solamente poner el script .py en la ruta
#el archivo html debe ir en htdocs
#Finalmente inicializar apache
#localhost/carpeta/archivo.html