from flask import Flask
from Routers.cityRouter import city_router  # Importa un conjunto de rutas (router) desde otro archivo
from Routers.supportRouter import support_router

app = Flask(__name__)  # Crea una instancia de la aplicación Flask

# Registrar el blueprint de city
app.register_blueprint(city_router)  # Añade el conjunto de rutas al servidor Flask
app.register_blueprint(support_router)  # Registrar el blueprint del soporte



app.run(host='127.0.0.1', port=1336, debug=True)