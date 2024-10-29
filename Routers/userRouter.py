from flask import Blueprint, request, jsonify
from Controllers.userController import add_user, add_role_to_user, add_task_type_to_user, list_users

user_router = Blueprint('user_router', __name__)

@user_router.route('/adduser', methods=['POST'])
def add_user_route():
    data = request.json

    user_full_name = data.get('user_full_name')
    user_address = data.get('user_address')
    user_email = data.get('user_email')
    user_nickname = data.get('user_nickname')
    user_document = data.get('user_document')  
    user_password = data.get('user_password')
    user_photo = data.get('user_photo')
    user_enable = data.get('user_enable')
    user_phone_number = data.get('user_phone_number')
    city_id = data.get('city_id')

    # Validar que todos los campos necesarios estén presentes
    if not all([user_full_name, user_email, user_password, city_id, user_document]):
        return jsonify({"error": "Faltan datos"}), 400

    # Llamar a la función add_user
    user_id = add_user(
        user_full_name, user_address, user_email, user_nickname, 
        user_document, user_password, user_photo, user_enable, 
        user_phone_number, city_id
    )
    
    if user_id:
        return jsonify({"message": f"Usuario {user_full_name} agregado exitosamente", "user_id": user_id}), 201
    else:
        return jsonify({"message": "Error al agregar el usuario"}), 400


@user_router.route('/adduserrole', methods=['POST'])
def add_role_route():
    data = request.json
    user_id = data.get('user_id')
    role_id = data.get('role_id')

    if not user_id or not role_id:
        return jsonify({"error": "Faltan datos"}), 400

    result = add_role_to_user(user_id, role_id)
    if result is not None:
        return jsonify({"message": f"Rol con ID {role_id} agregado al usuario con ID {user_id}"}), 201
    else:
        return jsonify({"error": "Error al agregar el rol al usuario"}), 404


@user_router.route('/addusertasktype', methods=['POST'])
def add_task_type_route():
    data = request.json
    user_id = data.get('user_id')
    task_type_id = data.get('task_type_id')

    if not user_id or not task_type_id:
        return jsonify({"error": "Faltan datos"}), 400

    result = add_task_type_to_user(user_id, task_type_id)
    if result is not None:
        return jsonify({"message": f"Tipo de tarea con ID {task_type_id} agregado al usuario con ID {user_id}"}), 201
    else:
        return jsonify({"error": "Error al agregar el tipo de tarea al usuario"}), 404


@user_router.route('/listusers', methods=['GET'])
def list_users_route():
    users = list_users()
    if users is not None:
        return jsonify(users), 200
    else:
        return jsonify({"error": "Error al listar los usuarios"}), 500