from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from Models import taskModel, userModel
from Controllers.taskController import  list_tasks, create_task
from datetime import datetime

# Crear el blueprint para las rutas de 'task'
task_router = Blueprint('task_router', __name__)

CostoPorHora = 10000

# Ruta para crear una nueva tarea
@task_router.route('/task/create', methods=['POST'])
def create_task_route():
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

    if not (user_id and task_title and task_stimed_time_hours and task_execution_date and task_execution_time and task_address and task_type_id):
        return jsonify({'error': 'Faltan datos obligatorios'}), 400
   
    session = Session()

    # Validar que el usuario existe
    user = session.query(userModel).filter_by(user_id=user_id).first()
    if not user:
        session.close()
        return jsonify({'error': 'Usuario no encontrado'}), 404

    # Calcular oferta sugerida
    task_offer_suggested = float(task_stimed_time_hours) * CostoPorHora
    # Crear una nueva tarea
    try:
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

    except Exception as e:
        session.rollback()
        return jsonify({'error': f'Error al crear la tarea: {str(e)}'}), 500

    finally:
        session.close()
        
@task_router.route('/task/list', methods=['GET'])
def list_tasks_route():
    tasks = list_tasks()
    
    if tasks is not None and len(tasks) > 0:
        return jsonify(tasks), 200
    elif tasks == []:
        return jsonify({'message': 'No hay tareas disponibles'}), 200
    else:
        return jsonify({'error': 'Error al listar las tareas'}), 500