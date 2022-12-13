##Bases de datos myqsl

## Como entrar a una base de datos especifica

import mysql.connector


conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="proyecto-ie0217")

cursor1=conexion1.cursor()
cursor1.execute("show tables")

for tabla in cursor1:
    print(tabla)
conexion1.close()