from flask import Blueprint, request, jsonify
from backend.models import Job, User
from backend import db

jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/api/jobs', methods=['POST'])
def post_job():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Validate required fields
        required_fields = ['client_id', 'title', 'description', 'budget']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        # Validate client_id
        client = User.query.get(data['client_id'])
        if not client or client.user_type != 'client':
            return jsonify({"error": "Invalid client_id or user is not a client"}), 400

        # Validate budget
        try:
            budget = float(data['budget'])
            if budget <= 0:
                raise ValueError
        except ValueError:
            return jsonify({"error": "Budget must be a positive number"}), 400

        # Create new job
        new_job = Job(
            client_id=data['client_id'],
            title=data['title'],
            description=data['description'],
            budget=budget,
            image_path=data.get('image_path')  # Optional field
        )
        db.session.add(new_job)
        db.session.commit()
        return jsonify({"message": "Job created successfully", "job_id": new_job.job_id}), 201

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@jobs_bp.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    try:
        # Fetch job by ID
        job = Job.query.get(job_id)
        if not job:
            return jsonify({"error": "Job not found"}), 404

        return jsonify({
            "job_id": job.job_id,
            "client_id": job.client_id,
            "title": job.title,
            "description": job.description,
            "budget": str(job.budget),
            "image_path": job.image_path,
            "created_at": job.created_at
        }), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@jobs_bp.route('/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    try:
        # Fetch job by ID
        job = Job.query.get(job_id)
        if not job:
            return jsonify({"error": "Job not found"}), 404

        # Get request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Update only the fields provided
        job.title = data.get('title', job.title)
        job.description = data.get('description', job.description)
        
        # Validate and update budget if provided
        if 'budget' in data:
            try:
                budget = float(data['budget'])
                if budget <= 0:
                    raise ValueError
                job.budget = budget
            except ValueError:
                return jsonify({"error": "Budget must be a positive number"}), 400

        db.session.commit()
        return jsonify({"message": "Job updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
