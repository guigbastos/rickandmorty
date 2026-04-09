from flask import Flask
from flask_cors import CORS
from src.models import db, ma
from config.settings import DATABASE_URI
from src.routes.character_routes import character_bp
from src.utils.constants import Environments
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

front_end_url = os.getenv("FRONT_END_URL")
environment = os.getenv("ENVIRONMENT")

origins_map = {
    Environments.LOCAL.value: ["*"],
    Environments.PRODUCTION.value: [front_end_url]
}

allowed_origin = origins_map.get(environment, origins_map[Environments.PRODUCTION.value])

CORS(app, origins=allowed_origin)
# resources={r"/*": {"origins": "http://localhost:5173"}}

db.init_app(app)
ma.init_app(app)

app.register_blueprint(character_bp, url_prefix='/character')

# @app.route('/')
# def hello_world():
#     return jsonify ({
#         "hello": "world"
#     })

if __name__ == '__main__':
    app.run(debug=True, port=5001)