from DataBase.connection import getConnection

def add_city(city_name, state_id):
    connection = getConnection()
    cursor = connection.cursor()

    # Crear la query para insertar una nueva ciudad
    query = """
        INSERT INTO city (city_name, state_id)
        VALUES (%s, %s)
    """
    
    try:
        # Ejecutar la query con los parámetros
        cursor.execute(query, (city_name, state_id))
        connection.commit()
        print(f"Ciudad {city_name} agregada exitosamente.")
        return city_name
    except Exception as e:
        print(f"Error al agregar la ciudad: {e}")
        connection.rollback()
        return
    finally:
        cursor.close()
        connection.close()


#funcion para listar las ciudades
def list_cities():
    connection = getConnection()
    cursor = connection.cursor()

    # Crear la query para seleccionar todas las ciudades
    query = """
        SELECT city_id, city_name, state_id
        FROM city
    """

    try:
        # Ejecutar la query
        cursor.execute(query)
        # Obtener todos los resultados
        cities = cursor.fetchall()
        
        # Formatear los resultados en una lista de diccionarios
        city_list = []
        for city in cities:
            city_list.append({
                'city_id': city[0],
                'city_name': city[1],
                'state_id': city[2]
            })

        return city_list

    except Exception as e:
        print(f"Error al listar las ciudades: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
