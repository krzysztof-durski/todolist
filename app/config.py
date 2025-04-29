from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, '..', 'todo.db')}"
else:
    SQLALCHEMY_DATABASE_URI = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

SQLALCHEMY_TRACK_MODIFICATIONS = False