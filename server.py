from flask import Flask
from Routers.cityRouter import city_router  
from Routers.supportRouter import support_router
from Routers.offerRouter import offer_router
from Routers.userRouter import user_router
from flask_cors import CORS

app = Flask(__name__)

# Direccion del frontend
CORS(app, origins=["http://localhost:4200"])

app = Flask(__name__)

# Registrar los blueprints
app.register_blueprint(city_router)
app.register_blueprint(support_router)
app.register_blueprint(offer_router)
app.register_blueprint(user_router)