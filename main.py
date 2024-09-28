import sync
from multiprocessing import Process
from server import app  

def run_server():
    app.run(host='127.0.0.1', port=1337 , debug=True, use_reloader=False)


if __name__ == "__main__":
    sync.sync()
    server_process = Process(target=run_server)
    server_process.start()  

    try:
        server_process.join()  # Espera a que el servidor se detenga
    except KeyboardInterrupt:
        print("Deteniendo el servidor...")
        server_process.terminate()  
        server_process.join()  
