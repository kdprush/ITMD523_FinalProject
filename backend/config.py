from dotenv import load_dotenv
import os

load_dotenv("/vagrant/backend/.env")  # Adjust the path as needed

DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
