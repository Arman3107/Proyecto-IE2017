##Bases de datos myqsl

##Eliminar archivos 

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="proyecto-ie0217")
cursor1=conexion1.cursor()
#cursor1.execute("update coords set Latitud=50 where Ubicacion='Cartago'")
cursor1.execute("delete from coords where Ubicacion = 'Cartago'")
conexion1.commit()
cursor1.execute("select Ubicacion, Latitud, Longitud from coords")
for fila in cursor1:
    print(fila)
conexion1.close()   