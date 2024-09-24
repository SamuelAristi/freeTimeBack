import mysql.connector
from connection import getConnection

def fetchData():
    connection = getConnection()

    if connection is None:
        print("No se pudo conectar a la base de datos")
        return
    
    try:
        cursor = connection.cursor()

        query = "SELECT * FROM estudiantes"

        cursor.execute(query)

        results = cursor.fetchall()

        for row in results:
            print(row)
        
    except mysql.connector.Error as err:
        print("Error:{err}")

    finally: 
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    fetchData()