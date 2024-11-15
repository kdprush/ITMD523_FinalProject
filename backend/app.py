# app.py
import os
from dotenv import load_dotenv
from . import db, create_app # Import from backend/__init__.py

# Import blueprints using relative imports
from .routes.users import users_bp
from .routes.jobs import jobs_bp
from .routes.applications import applications_bp
from .routes.messages import messages_bp

 # Load environment variables from .env file
load_dotenv()

# Initialize the app using create_app() from _init_.py
app = create_app()

# Register blueprints
try:
    app.register_blueprint(users_bp)
    app.register_blueprint(jobs_bp)
    app.register_blueprint(applications_bp)
    app.register_blueprint(messages_bp)
except ValueError as e:
    print(f"Blueprint registration error: {e}")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
