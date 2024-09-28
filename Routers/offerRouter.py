from flask import Blueprint, request, jsonify
from Controllers.offerController import add_offer, list_offers

# Crear el blueprint para las rutas de 'offer'
offer_router = Blueprint('offer_router', __name__)

# Ruta para agregar una oferta
@offer_router.route('/addOffer', methods=['POST'])
def add_offer_route():
    data = request.json
    
    offer_date = data.get('offer_date')
    offer_inicial_price = data.get('offer_inicial_price')
    address = data.get('address')
    task_id = data.get('task_id')
    user_id_fulltimer = data.get('user_id_fulltimer')
    offer_start_date = data.get('offer_start_date')
    offer_end_date = data.get('offer_end_date')
    offer_state_id = data.get('offer_state_id')

    # Campos opcionales
    user_id_freetimer = data.get('user_id_freetimer')
    offer_freetimer_calification = data.get('offer_freetimer_calification')
    offer_fulltimer_calification = data.get('offer_fulltimer_calification')
    offer_final_price = data.get('offer_final_price')

    # Verificación de campos obligatorios
    if not all([offer_date, offer_inicial_price, address, task_id, user_id_fulltimer, offer_start_date, offer_end_date, offer_state_id]):
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    # Llamada al método de agregar oferta
    response = add_offer(
        offer_date, 
        offer_inicial_price, 
        address, 
        task_id, 
        user_id_fulltimer, 
        offer_start_date, 
        offer_end_date, 
        offer_state_id, 
        user_id_freetimer, 
        offer_freetimer_calification, 
        offer_fulltimer_calification, 
        offer_final_price
    )

    if response:
        return jsonify({"message": "Oferta agregada exitosamente"}), 201
    else:
        return jsonify({"error": "Error al agregar la oferta"}), 500

# Ruta para listar todas las ofertas
@offer_router.route('/listOffers', methods=['GET'])
def list_offers_route():
    offers = list_offers()
    if offers is not None:
        return jsonify(offers), 200
    else:
        return jsonify({"error": "Error al listar las ofertas"}), 500
