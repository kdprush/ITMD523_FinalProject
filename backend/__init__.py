from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Directly set Flask configurations with no placeholders
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:MySQL@1234@localhost:3306/freelancer_marketplace"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "your_secret_key"

    print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")


    db.init_app(app)

    # Register blueprints or routes here
    from backend.routes.applications import applications_bp
    app.register_blueprint(applications_bp, url_prefix="/applications")

    return app
