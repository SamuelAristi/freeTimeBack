from flask import Flask
from Routers.cityRouter import city_router  # Importa un conjunto de rutas (router) desde otro archivo

app = Flask(__name__)  # Crea una instancia de la aplicación Flask

# Registrar el blueprint de city
app.register_blueprint(city_router)  # Añade el conjunto de rutas al servidor Flask



app.run(host='127.0.0.1', port=1337, debug=True)