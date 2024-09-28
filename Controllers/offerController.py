from DataBase.connection import getConnection

# Método para crear una nueva oferta
def add_offer(offer_date, offer_inicial_price, address, task_id, 
                user_id_fulltimer, offer_start_date, offer_end_date, 
                offer_state_id, user_id_freetimer=None, offer_freetimer_calification=None, 
                offer_fulltimer_calification=None, offer_final_price=None):
    connection = getConnection()
    cursor = connection.cursor()

    query = """
        INSERT INTO offer (
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
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        # Ejecutar la query con los parámetros
        cursor.execute(query, (
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
        ))
        connection.commit()
        print(f"Oferta creada exitosamente.")
        return True
    except Exception as e:
        print(f"Error al crear la oferta: {e}")
        connection.rollback()
        return False
    finally:
        cursor.close()
        connection.close()

# Método para listar todas las ofertas
def list_offers():
    connection = getConnection()
    cursor = connection.cursor()

    query = """
        SELECT 
            offer_id, 
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
        FROM offer
    """

    try:
        cursor.execute(query)
        offers = cursor.fetchall()

        offer_list = []
        for offer in offers:
            offer_list.append({
                'offer_id': offer[0],
                'offer_date': offer[1],
                'offer_inicial_price': offer[2],
                'address': offer[3],
                'task_id': offer[4],
                'user_id_fulltimer': offer[5],
                'offer_start_date': offer[6],
                'offer_end_date': offer[7],
                'offer_state_id': offer[8],
                'user_id_freetimer': offer[9],
                'offer_freetimer_calification': offer[10],
                'offer_fulltimer_calification': offer[11],
                'offer_final_price': offer[12]
            })

        return offer_list

    except Exception as e:
        print(f"Error al listar las ofertas: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
