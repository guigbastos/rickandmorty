from flask import Flask
from flask_cors import CORS
from src.models import db, ma
from config.settings import DATABASE_URI
from src.routes.character_routes import character_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
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