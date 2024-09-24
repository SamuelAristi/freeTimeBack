from flask import Blueprint, request, jsonify
from Controllers.cityController import add_city, list_cities

# Crear el blueprint para las rutas de 'city'
city_router = Blueprint('city_router', __name__)

# Ruta para agregar una ciudad
@city_router.route('/addCity', methods=['POST'])
def add_city_route():
    data = request.json
    city_name = data.get('city_name')
    state_id = data.get('state_id')

    if not city_name or not state_id:
        return jsonify({"error": "Faltan datos"}), 400

    response = add_city(city_name, state_id)
    if(response != None):
        return jsonify({"message": f"Ciudad {city_name} agregada exitosamente"}), 201
    else:
        return jsonify({"message": f"Error al agregar la ciudad"}), 404
    

@city_router.route('/listCities', methods=['GET'])
def list_cities_route():
    cities = list_cities()
    if cities is not None:
        return jsonify(cities), 200
    else:
        return jsonify({"error": "Error al listar las ciudades"}), 500