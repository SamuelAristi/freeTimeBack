from flask import Flask
from Routers.cityRouter import city_router  
from Routers.supportRouter import support_router

app = Flask(__name__)

# Registrar los blueprints
app.register_blueprint(city_router)
app.register_blueprint(support_router)


