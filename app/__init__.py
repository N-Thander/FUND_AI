from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

def create_app():

    app = Flask(__name__)

    # add the logic to integrate app here

    return app