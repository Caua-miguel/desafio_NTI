import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

db = psycopg2.connect(os.getenv('DATABASE_URI'))
cursor = db.cursor()