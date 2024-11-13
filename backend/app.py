# app.py
import os
from dotenv import load_dotenv
from __init__ import db, create_app
from routes.users import users_bp
from routes.jobs import jobs_bp
from routes.applications import applications_bp
from routes.messages import messages_bp

 # Load environment variables from .env file
load_dotenv()

# Initialize the app using create_app() from _init_.py
app = create_app()

# Register blueprints
app.register_blueprint(users_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(applications_bp)
app.register_blueprint(messages_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
