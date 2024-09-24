import sync
from multiprocessing import Process
from server import app  

def run_server():
    app.run(debug=True, use_reloader=False)  

if __name__ == "__main__":
    server_process = Process(target=run_server)
    server_process.start()  

    sync.sync()

    server_process.join()
