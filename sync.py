from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.init import Base
from DataBase.connection import getConnection

# Crear el engine de la base de datos
engine = create_engine('mysql+mysqlconnector://root:@localhost/freetimedb')

# Crear una clase Session que permita manejar las sesiones de la base de datos
Session = sessionmaker(bind=engine)

def sync():
    # Obtén la conexión a la base de datos
    connection = getConnection()
    if connection is None:
        print("No se pudo conectar a la base de datos")
        return

    # Crear todas las tablas
    Base.metadata.create_all(engine)
    print("Base de datos sincronizada")

    # Cierra la conexión
    connection.close()

if __name__ == "__main__":
    sync()
