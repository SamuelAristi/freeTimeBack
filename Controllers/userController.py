from DataBase.connection import getConnection
from Models.userModel import User
from Models.roleModel import Role
from Models.userRoleModel import UsersRole

def add_user(user_full_name, user_address, user_email, user_nickname, user_document, user_password, user_photo, user_enable, user_points, user_phone_number, city_id, role_id):
    connection = getConnection()
    cursor = connection.cursor()

    # Verificar si el rol existe en la tabla Role
    query = """
        SELECT * FROM Role
        WHERE role_id = %s
    """
    cursor.execute(query, (role_id,))
    role = cursor.fetchone()
    if role is None:
        print(f"Error: Rol con ID {role_id} no existe.")
        return

    # Crear el usuario
    query = """
        INSERT INTO User (user_full_name, user_address, user_email, user_nickname, user_document, user_password, user_photo, user_enable, user_points, user_phone_number, city_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (user_full_name, user_address, user_email, user_nickname, user_document, user_password, user_photo, user_enable, user_points, user_phone_number, city_id))
    user_id = cursor.lastrowid

    # Crear la entrada en la tabla UsersRole
    query = """
        INSERT INTO UsersRole (user_id, role_id)
        VALUES (%s, %s)
    """
    cursor.execute(query, (user_id, role_id))

    connection.commit()
    print(f"Usuario {user_full_name} agregado exitosamente con rol {role_id}.")
    return user_id



def list_users():
    connection = getConnection()
    cursor = connection.cursor()

    # Crear la query para seleccionar todas las ciudades
    query = """
        SELECT user_id, user_full_name, user_address, user_email, user_nickname, user_document, user_password, user_photo,
        user_enable, user_points, user_phone_number, city_id
        FROM user
    """

    try:
        # Ejecutar la query
        cursor.execute(query)
        # Obtener todos los resultados
        users = cursor.fetchall()
        
        # Formatear los resultados en una lista de diccionarios
        user_list = []
        for user in users:
            user_list.append({

                'user_id':user[0],
                'user_full_name':user[1],
                'user_address' :user[2],
                'user_email':user[3],
                'user_nickname':user[4],
                'user_document':user[5],
                'user_password' :user[6],
                'user_photo':user[7],
                'user_enable' :user[8],
                'User_points' :user[9],
                'user_phone_number' :user[10],
                'city_id':user[11],
            })

        return user_list

    except Exception as e:
        print(f"Error al listar los usuarios {e}")
        return None
    finally:
        cursor.close()
        connection.close()
