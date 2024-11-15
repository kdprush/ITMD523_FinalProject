from flask import Blueprint, request, jsonify
from ..models import Job
from .. import db

jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/jobs', methods=['POST'])
def post_job():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        required_fields = ['client_id', 'title','description','budget']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400
    
        new_job = Job(
            client_id=data['client_id'],
            title=data['title'],
            description=data['description'],
            budget=data['budget'],
            image_path=data.get('image_path')
        )
        db.session.add(new_job)
        db.session.commit()
        return jsonify({"message": "Job posted successfully", "job_id": new_job.job_id}), 201

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
@jobs_bp.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    try:
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
        })
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@jobs_bp.route('/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    try:
        job = Job.query.get(job_id)
        if not job:
            return jsonify({"error": "Job not found"}), 404

        data = request.get_json()
        if not data:
            return jsonify ({"error": "No data provided"}), 400
        
        # Update only fields that are provided in the request    
        job.title = data.get('title', job.title)
        job.description = data.get('description', job.description)
        job.budget = data.get('budget', job.budget)

        db.session.commit()
        return jsonify({"message": "Job updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500