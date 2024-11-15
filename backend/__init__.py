import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # Import Flask-Migrate

db = SQLAlchemy()
migrate = Migrate() # Initialize Migrate

def create_app():
    app = Flask(__name__)
    
    # Use environment variable for the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Check if the database URI is set
    if not app.config['SQLALCHEMY_DATABASE_URI']:
        raise ValueError("SQLALCHEMY_DATABASE_URI is not set in the environment")
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .routes.users import users_bp
    from .routes.jobs import jobs_bp
    from .routes.applications import applications_bp
    from .routes.messages import messages_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(jobs_bp)
    app.register_blueprint(applications_bp)
    app.register_blueprint(messages_bp)
    
    return app
