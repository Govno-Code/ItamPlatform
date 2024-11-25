from flask import Flask
from flask_cors import CORS
from app.models import db
from app.routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Инициализация CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp, url_prefix='/api')

    return app
