# app.py
import os
from dotenv import load_dotenv
from . import create_app # Import from backend/__init__.py



 # Load environment variables from .env file
load_dotenv()

# Initialize the app using create_app() from _init_.py
app = create_app()

@app.route('/')
def home():
    return "Welcome to the Freelancer Marketplace API"

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"}), 200


if __name__ == '__main__':
    with app.app_context():    
        print(app.url_map)
    app.run(debug=True, port=5000)

