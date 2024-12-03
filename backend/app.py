from flask import Flask
from flask_migrate import Migrate
from backend import create_app, db  # Import create_app and db
from backend.routes.applications import applications_bp  # Import the applications blueprint
from backend.routes.messages import messages_bp  # Import the messages blueprint
from backend.routes.jobs import jobs_bp  # Import the jobs blueprint
from backend.routes.users import users_bp  # Import the users blueprint

from flask_cors import CORS

# Initialize the Flask app
app = create_app()
CORS(app)
migrate = Migrate(app, db)
# Register blueprints
print("Registering applications blueprint")
try:
    app.register_blueprint(applications_bp, url_prefix='/api/users')
except ValueError:
    print("Applications blueprint already registered, skipping...")

print("Registering messages blueprint")
try:
    app.register_blueprint(messages_bp, url_prefix='/api/messages')
except ValueError:
    print("Messages blueprint already registered, skipping...")

print("Registering jobs blueprint")
app.register_blueprint(jobs_bp, url_prefix='/api/jobs')

print("Registering users blueprint")
app.register_blueprint(users_bp, url_prefix="/users/profile")


# Print the URL map for debugging purposes
with app.app_context():
    print(app.url_map)

# Home route
@app.route('/')
def home():
    return "Welcome to the Freelancer Marketplace!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don’t exist
    app.run(host='0.0.0.0', port=5000, debug=True)
