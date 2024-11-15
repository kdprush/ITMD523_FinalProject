# app.py
import os
from dotenv import load_dotenv
from . import create_app # Import from backend/__init__.py



 # Load environment variables from .env file
load_dotenv()

# Initialize the app using create_app() from _init_.py
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
