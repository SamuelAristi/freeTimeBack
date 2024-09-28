from flask import Flask
from Routers.cityRouter import city_router  
from Routers.supportRouter import support_router
app = Flask(__name__)
from Routers.offerRouter import offer_router # Importa un
# Registrar los blueprints
app.register_blueprint(city_router)
app.register_blueprint(support_router)
app.register_blueprint(offer_router) # Añade el
