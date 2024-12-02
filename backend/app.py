# app.py
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv
from . import create_app # Import from backend/__init__.py
from flask import jsonify
from routes.users import users_bp


 # Load environment variables from .env file
load_dotenv()



# Initialize the app using create_app() from _init_.py
app = create_app()
app.register_blueprint(users_bp)

@app.route('/')
def home():
    return "Welcome to the Freelancer Marketplace API"

@app.route('/test', methods=['GET'])
def test():
    return "Test endpoint works!", 200

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"}), 200

if __name__ == '__main__':
    print(app.url_map)  # Debugging: Print all routes
    app.run(debug=True, port=5000)


