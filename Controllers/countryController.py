from DataBase.connection import getConnection

def add_country(country_name):
    connection = getConnection()
    cursor = connection.cursor()

    # Crear la query para insertar un nuevo país
    query = """
        INSERT INTO country (country_name)
        VALUES (%s)
    """

    try:
        # Ejecutar la query con el parámetro
        cursor.execute(query, (country_name,))
        connection.commit()
        print(f"País {country_name} agregado exitosamente.")
        return country_name
    except Exception as e:
        print(f"Error al agregar el país: {e}")
        connection.rollback()
        return
    finally:
        cursor.close()
        connection.close()

# Función para listar los países
def list_countries():
    connection = getConnection()
    cursor = connection.cursor()

    # Crear la query para seleccionar todos los países
    query = """
        SELECT country_id, country_name
        FROM country
    """

    try:
        # Ejecutar la query
        cursor.execute(query)
        # Obtener todos los resultados
        countries = cursor.fetchall()
        
        # Formatear los resultados en una lista de diccionarios
        country_list = []
        for country in countries:
            country_list.append({
                'country_id': country[0],
                'country_name': country[1]
            })

        return country_list

    except Exception as e:
        print(f"Error al listar los países: {e}")
        return None
    finally:
        cursor.close()
        connection.close()