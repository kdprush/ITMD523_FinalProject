from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Directly set Flask configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:MySQL@1234@localhost:3306/freelancer_marketplace"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "your_secret_key"

    db.init_app(app)

    # Register blueprints or routes here
    from backend.routes.applications import applications_bp
    app.register_blueprint(applications_bp, url_prefix="/applications")

    return app


# Home route
@app.route('/')
def home():
    return "Welcome to the Freelancer Marketplace!"

# Get all jobs
@app.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        # Use SQLAlchemy for database queries
        cursor = db.session.connection().cursor()
        cursor.execute("SELECT * FROM jobs;")
        jobs = cursor.fetchall()
        return jsonify(jobs), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Create a new job
@app.route('/jobs', methods=['POST'])
def post_job():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        required_fields = ['client_id', 'title', 'description', 'budget']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        cursor = db.session.connection().cursor()
        cursor.execute(
            "INSERT INTO jobs (client_id, title, description, budget, image_path) VALUES (%s, %s, %s, %s, %s)",
            (data['client_id'], data['title'], data['description'], data['budget'], data.get('image_path'))
        )
        db.session.commit()
        return jsonify({"message": "Job created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update an existing job
@app.route('/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        cursor = db.session.connection().cursor()
        query = "UPDATE jobs SET title = %s, description = %s, budget = %s WHERE job_id = %s"
        cursor.execute(query, (
            data.get('title'), 
            data.get('description'), 
            data.get('budget'), 
            job_id
        ))
        db.session.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Job not found"}), 404

        return jsonify({"message": "Job updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create all tables if they don't exist
    app.run(host='0.0.0.0', port=5000, debug=True)
