# config.py
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DBNAME = os.getenv("MONGO_DBNAME", "mypy")
SECRET_KEY = os.getenv("SECRET_KEY", "describeme")
