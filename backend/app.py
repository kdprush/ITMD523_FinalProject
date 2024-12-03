from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL@1234",
    database="freelancer_marketplace"
)

@app.route('/')
def home():
    return "Welcome to the Freelancer Marketplace!"

# Get all jobs
@app.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        cursor = db.cursor(dictionary=True)
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

        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO jobs (client_id, title, description, budget, image_path) VALUES (%s, %s, %s, %s, %s)",
            (data['client_id'], data['title'], data['description'], data['budget'], data.get('image_path'))
        )
        db.commit()
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

        cursor = db.cursor()
        query = "UPDATE jobs SET title = %s, description = %s, budget = %s WHERE job_id = %s"
        cursor.execute(query, (
            data.get('title'), 
            data.get('description'), 
            data.get('budget'), 
            job_id
        ))
        db.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Job not found"}), 404

        return jsonify({"message": "Job updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
