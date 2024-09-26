from flask import Blueprint, request, jsonify
from Controllers.supportController import create_support, get_supports

#Crear el blueprint para las rutas de 'support'
support_router = Blueprint('support_router', __name__)

#Ruta para crear un soporte
@support_router.route('/addSupport', methods=['POST'])
def add_support_route():
    data = request.json
    support_description = data.get('support_description')
    user_id = data.get('user_id')
    support_state_id = data.get('support_state_id')

    if not support_description or not user_id or not support_state_id:
        return jsonify({"error": "Faltan datos"}), 400

    response = create_support(support_description, user_id, support_state_id)
    if response is not None:
        return jsonify({"message": "Soporte creado exitosamente"}), 201
    else:
        return jsonify({"error": "Error al crear el soporte"}), 400

#Ruta para listar todos los soportes
@support_router.route('/listSupports', methods=['GET'])
def list_supports_route():
    supports = get_supports()
    if supports is not None:
        return jsonify(supports), 200
    else:
        return jsonify({"error": "Error al listar los soportes"}), 500