
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    load_dotenv()

    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('HOST')}/{os.getenv('DBNAME')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
