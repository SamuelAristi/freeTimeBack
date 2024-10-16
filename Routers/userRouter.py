from flask import Blueprint, request, jsonify
from Controllers.userController import add_user, list_users

user_router = Blueprint('user_router', __name__)

@user_router.route('/adduser', methods=['POST'])

def add_user_route():
    data = request.json
    user_data = data.get('user', {})

    user_full_name = user_data.get('user_full_name')
    user_address = user_data.get('user_address')
    user_email = user_data.get('user_email')
    user_nickname = user_data.get('user_nickname')
    user_document = user_data.get('user_document')  
    user_password = user_data.get('user_password')
    user_photo = user_data.get('user_photo')
    user_enable = user_data.get('user_enable')
    user_phone_number = user_data.get('user_phone_number')
    city_id = user_data.get('city_id')
    role_id = data.get('role_id')

    # Validar que todos los campos necesarios estén presentes
    if not all([user_full_name, user_email, user_password, city_id, role_id, user_document]):
        return jsonify({"error": "Faltan datos"}), 400

    # Llamar a la función add_user con todos los parámetros
    response = add_user(
        user_full_name, user_address, user_email, user_nickname, 
        user_document, user_password, user_photo, user_enable, user_phone_number, city_id, role_id
    )
    
    if response:
        return jsonify({"message": f"Usuario {user_full_name} agregado exitosamente con rol {role_id}"}), 201
    else:
        return jsonify({"message": f"Error al agregar el usuario"}), 404

@user_router.route('/listusers', methods=['GET'])
def list_users_route():
    users = list_users()
    if users is not None:
        return jsonify(users), 200
    else:
        return jsonify({"error": "Error al listar los usuarios"}),  500