from flask import Blueprint, request, jsonify # type: ignore #ignore
from sqlalchemy.orm import Session
from Models import taskModel, userModel
from datetime import datetime
task_blueprint = Blueprint('task', __name__)
COSTO_POR_HORA = 10000
@task_blueprint.route('/task/create', methods=['POST'])
def create_task():
    """
    Crear una nueva tarea basada en los datos enviados en la solicitud, incluyendo
    el cálculo automático de la oferta sugerida.
    """
    # Obtener datos del cuerpo de la solicitud
    data = request.get_json()
    user_id = data.get('user_id')  
    task_title = data.get('task_title')
    task_description = data.get('task_description')
    task_stimed_time_hours = data.get('task_stimed_time_hours')
    task_offer = data.get('task_offer')
    task_execution_date = data.get('task_execution_date')  
    task_execution_time = data.get('task_execution_time')  
    task_address = data.get('task_address')
    task_type_id = data.get('task_type_id')
    # Crear una sesión de base de datos
    session = Session()
    #Validar que el usuario existe
    user = session.query(userModel).filter_by(user_id=user_id).first()
    if not user:
       return jsonify({'error': 'Usuario no encontrado'}), 404
    # Calcular oferta sugerida 
    task_offer_suggested = float(task_stimed_time_hours) * COSTO_POR_HORA
    # Crear una nueva tarea
    new_task = taskModel(
        task_title=task_title,
        task_description=task_description,
        task_stimed_time_hours=task_stimed_time_hours,
        task_offer=task_offer,
        task_offer_suggested=task_offer_suggested,
        task_execution_date=datetime.strptime(task_execution_date, '%Y-%m-%d'),
        task_execution_time=datetime.strptime(task_execution_time, '%H:%M:%S').time(),
        task_address=task_address,
        task_type_id=task_type_id
    )
    # Guardar la tarea en la base de datos
    session.add(new_task)
    session.commit()

    return jsonify({
        'message': 'Tarea creada con éxito',
        'task_id': new_task.task_id,
        'task_offer_suggested': task_offer_suggested  
    }), 201

def list_tasks():
    """
    Función para listar todas las tareas en la base de datos.
    """
    session = Session()
    try:
        # Consulta para obtener todas las tareas
        tasks = session.query(taskModel).all()

        if not tasks:
            return []

        # Formatear las tareas en una lista de diccionarios
        task_list = []
        for task in tasks:
            task_list.append({
                'task_id': task.task_id,
                'task_title': task.task_title,
                'task_description': task.task_description,
                'task_stimed_time_hours': task.task_stimed_time_hours,
                'task_offer': task.task_offer,
                'task_offer_suggested': task.task_offer_suggested,
                'task_execution_date': task.task_execution_date.strftime('%Y-%m-%d'),
                'task_execution_time': task.task_execution_time.strftime('%H:%M:%S'),
                'task_address': task.task_address,
                'task_type_id': task.task_type_id
            })

        return task_list

    except Exception as e:
        print(f"Error al listar las tareas: {e}")
        return None
    finally:
        session.close()
