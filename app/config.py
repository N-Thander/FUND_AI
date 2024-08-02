import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('HOST')}/{os.getenv('DBNAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False