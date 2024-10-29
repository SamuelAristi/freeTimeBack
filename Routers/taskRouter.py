from flask import Blueprint,request,jsonify
from Controllers.taskController import list_task

task_router = Blueprint('task_router',__name__)

@task_router.route('/listtask', methods=['GET'])
def list_task_route():
    tasks = list_task()
    if tasks is not None:
        return jsonify(tasks), 200
    else:
        return jsonify({"error": "Error al listar las tareas"}, tasks), 500