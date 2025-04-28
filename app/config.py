from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False