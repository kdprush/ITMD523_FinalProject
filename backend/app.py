import os
import sys
from dotenv import load_dotenv
from backend import create_app  # Import from backend/__init__.py
from backend.routes.users import users_bp
from flask import jsonify

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Initialize the app using create_app() from __init__.py
app = create_app()
app.register_blueprint(users_bp, url_prefix='/api/users')  # Optional URL prefix

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
    app.run(debug=True, host='0.0.0.0', port=5000)


