import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Use environment variable for the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .routes.users import users_bp
    from .routes.jobs import jobs_bp
    from .routes.applications import applications_bp
    from .routes.messages import messages_bp

    app.register_blueprint(users_bp, url_prefix='/users') # Add a prefix if needed
    app.register_blueprint(jobs_bp)
    app.register_blueprint(applications_bp)
    app.register_blueprint(messages_bp)
    
    return app
