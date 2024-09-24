from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
DATABASE_URL = 'mysql+mysqlconnector://root:@localhost/freetimedb'

# Crear el motor
engine = create_engine(DATABASE_URL)

# Crear el objeto MetaData y reflejar las tablas
metadata = MetaData()
metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

def table_exists(table_name):
    return table_name in metadata.tables

def column_exists(table_name, column_name):
    with engine.connect() as connection:
        query = f"""
        SELECT COUNT(*)
        FROM information_schema.COLUMNS
        WHERE TABLE_NAME = '{table_name}' AND COLUMN_NAME = '{column_name}';
        """
        result = connection.execute(text(query))
        count = result.scalar()
    return count > 0

def get_foreign_keys(table_name, column_name):
    # Consultar claves foráneas asociadas a la columna
    with engine.connect() as connection:
        query = f"""
        SELECT CONSTRAINT_NAME
        FROM information_schema.KEY_COLUMN_USAGE
        WHERE TABLE_NAME = '{table_name}' AND COLUMN_NAME = '{column_name}';
        """
        result = connection.execute(text(query))
        foreign_keys = [row[0] for row in result]
    return foreign_keys

def drop_foreign_keys(table_name, foreign_keys):
    with engine.connect() as connection:
        for fk in foreign_keys:
            query = f"ALTER TABLE {table_name} DROP FOREIGN KEY {fk};"
            connection.execute(text(query))

def add_column_to_table(table_name, column_name, column_type):
    try:
        # Crear la nueva columna
        with engine.connect() as connection:
            # Generar la consulta SQL para agregar la columna
            alter_table_query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type};"
            # Ejecutar la consulta utilizando text()
            connection.execute(text(alter_table_query))
        print(f"Columna '{column_name}' añadida exitosamente a la tabla '{table_name}'.")
    except SQLAlchemyError as e:
        print(f"Error al agregar la columna: {e}")

def drop_column_from_table(table_name, column_name):
    try:
        # Verificar si la columna existe
        if not column_exists(table_name, column_name):
            print(f"La columna '{column_name}' no existe en la tabla '{table_name}'.")
            return

        # Obtener claves foráneas asociadas a la columna
        foreign_keys = get_foreign_keys(table_name, column_name)
        if foreign_keys:
            print(f"Eliminando claves foráneas asociadas a la columna '{column_name}'.")
            drop_foreign_keys(table_name, foreign_keys)

        # Eliminar la columna
        with engine.connect() as connection:
            # Generar la consulta SQL para eliminar la columna
            alter_table_query = f"ALTER TABLE {table_name} DROP COLUMN {column_name};"
            # Ejecutar la consulta utilizando text()
            connection.execute(text(alter_table_query))
        print(f"Columna '{column_name}' eliminada exitosamente de la tabla '{table_name}'.")
    except SQLAlchemyError as e:
        print(f"Error al eliminar la columna: {e}")

def main():
    while True:
        print("\nOpciones:")
        print("1. Agregar una columna a una tabla")
        print("2. Eliminar una columna de una tabla")
        print("3. Salir")
        choice = input("Seleccione una opción: ").strip()

        if choice == '3':
            print("Saliendo del programa.")
            break

        if choice == '1':
            while True:
                table_name = input("Ingrese el nombre de la tabla: ").strip()
                if not table_exists(table_name):
                    print(f"La tabla '{table_name}' no existe.")
                    print("1. Volver al menú principal")
                    print("2. Salir")
                    error_choice = input("Seleccione una opción: ").strip()

                    if error_choice == '2':
                        print("Saliendo del programa.")
                        return
                    elif error_choice == '1':
                        break  # Regresar al menú principal
                else:
                    column_name = input("Ingrese el nombre de la nueva columna: ").strip()
                    column_type = input("Ingrese el tipo de la columna (por ejemplo, 'VARCHAR(255)', 'INT'): ").strip()

                    # Validar el tipo de columna y crear la columna
                    add_column_to_table(table_name, column_name, column_type)
                    break  # Salir del bucle de agregar columna después de realizar la operación

        elif choice == '2':
            while True:
                table_name = input("Ingrese el nombre de la tabla: ").strip()
                if not table_exists(table_name):
                    print(f"La tabla '{table_name}' no existe.")
                    print("1. Volver al menú principal")
                    print("2. Salir")
                    error_choice = input("Seleccione una opción: ").strip()

                    if error_choice == '2':
                        print("Saliendo del programa.")
                        return
                    elif error_choice == '1':
                        break  # Regresar al menú principal
                else:
                    column_name = input("Ingrese el nombre de la columna que desea eliminar: ").strip()
                    
                    # Eliminar la columna
                    drop_column_from_table(table_name, column_name)
                    break  # Salir del bucle de eliminar columna después de realizar la operación

if __name__ == "__main__":
    main()
