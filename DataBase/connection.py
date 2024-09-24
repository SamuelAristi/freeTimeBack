import mysql.connector

def getConnection():
    config={
        'user': 'root',
        'password' : '',
        'host': 'localhost',
        'database': 'freetimedb',
        'raise_on_warnings' : True
    }

    try:
        connection = mysql.connector.connect(**config)
        print("Conexion con la Base de Datos Exitosa")
        return connection
        
    except mysql.connector.Error as err:
            print("Error: {err}")
            return None

