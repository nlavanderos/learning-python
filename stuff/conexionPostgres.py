import psycopg2

#Definiciones de la conexion
conn = psycopg2.connect(
    host = "localhost",
    database = "random",
    user = "postgres",
    password = "root"
)

#
cursor = conn.cursor()

#Aca podria ir una sentencia de dropTable si es que existe
#cursor.execute()

#Creacion de tabla 
# sql="""CREATE TABLE ALUMNO(
#     NOMBRE VARCHAR(20),
#     APELLIDO_PATERNO VARCHAR(20) NOT NULL,
#     EDAD INT,
#     SEXO CHAR(1),
#     CALIFICACION FLOAT
# )
# """

# cursor.execute(sql)

#Dos formas de agregar informacion a la tabla creada
#agregar="INSERT INTO ALUMNO(NOMBRE,APELLIDO_PATERNO,EDAD,SEXO,CALIFICACION)"+"VALUES('David','Miranda',25,'m',6.0)"+";"
agregar2="""INSERT INTO ALUMNO(NOMBRE,APELLIDO_PATERNO,EDAD,SEXO,CALIFICACION) VALUES('Martin','Rojas',26,'m',6.0);"""
cursor.execute(agregar2)
conn.commit()
conn.close()