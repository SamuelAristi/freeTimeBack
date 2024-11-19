from DataBase.connection import getConnection
from datetime import datetime

# Función para crear un soporte
def create_support(support_description, user_id, support_state_id):
    connection = getConnection()
    cursor = connection.cursor()

    # Crear la query para insertar un nuevo soporte
    query = """
        INSERT INTO support (support_date, support_description, user_id, support_state_id)
        VALUES (%s, %s, %s, %s)
    """
    
    try:
        # Ejecutar la query con los parámetros
        cursor.execute(query, (datetime.now(), support_description, user_id, support_state_id))
        connection.commit()
        return {
            "success": True,
            "message": "Soporte creado exitosamente.",
            "support_data": {
                "support_id": support_id,  # Ahora retorna el ID del soporte creado
                "user_email": user_email,  # Ahora retorna el correo del usuario
                "support_description": support_description,
                "user_id": user_id,
                "support_state_id": support_state_id
            }
        }
    except Exception as e:
        print(f"Error al crear soporte: {str(e)}")
        connection.rollback()
        return {
            "success": False,
            "message": f"Error al crear soporte: {str(e)}"
        }
    finally:
        cursor.close()
        connection.close()
        
# Función para listar todos los soportes junto con los datos del usuario
def get_supports():
    connection = getConnection()
    cursor = connection.cursor()

    # Crear la query para obtener soportes y los datos del usuario
    query = """
        SELECT s.support_id, s.support_description, s.support_date, s.user_id, 
               s.support_state_id, u.user_full_name, u.user_email
        FROM support s
        JOIN user u ON s.user_id = u.user_id
    """

    try:
        # Ejecutar la query
        cursor.execute(query)
        supports = cursor.fetchall()

        # Formatear los resultados en una lista de diccionarios
        support_list = []
        for support in supports:
            support_list.append({
                "support_id": support[0],
                "support_description": support[1],
                "support_date": support[2],
                "user_id": support[3],
                "support_state_id": support[4],
                "user_name": support[5],
                "user_email": support[6]
            })

        return {
            "success": True,
            "supports": support_list
        }

    except Exception as e:
        print(f"Error al listar soportes: {str(e)}")
        return {
            "success": False,
            "message": f"Error al listar soportes: {str(e)}"
        }
    finally:
        cursor.close()
        connection.close()
