from sqlalchemy import create_engine
from Models.init import Base
from DataBase.connection import getConnection

def sync():
    # Obtén la conexión a la base de datos
    connection = getConnection()
    if connection is None:
        print("No se pudo conectar a la base de datos")
        return

    # Crear un engine con la URL de conexión
    engine = create_engine('mysql+mysqlconnector://root:@localhost/freetimedb')
    
    # Crear todas las tablas
    Base.metadata.create_all(engine)
    print("Base de datos sincronizada")

    # Cierra la conexión
    connection.close()

if __name__ == "__main__":
    sync()



