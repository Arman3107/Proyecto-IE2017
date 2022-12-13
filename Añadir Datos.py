##Bases de datos myqsl

##Muestra como añadir datos en la base de datos

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="proyecto-ie0217")

cursor1=conexion1.cursor()
sql="insert into coords (Ubicacion, Latitud, Longitud) values (%s,%s,%s)"
datos=("Cartago", 9.86444, -83.91944 )
cursor1.execute(sql, datos)
datos= ("Costa Rica", 9.748917, -83.753428)
cursor1.execute(sql, datos)
datos= ("San Jose", 9.93333, -84.08333)
cursor1.execute(sql, datos)
datos= ("Turrialba", 9.90467, -83.68352)
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()


