from flask import Blueprint, request, jsonify
from ..models import Job
from .. import db

jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/jobs', methods=['POST'])
def post_job():
    data = request.get_json()
    new_job = Job(
        client_id=data['client_id'],
        title=data['title'],
        description=data['description'],
        budget=data['budget'],
        image_path=data.get('image_path')
    )
    db.session.add(new_job)
    db.session.commit()
    return jsonify({"message": "Job posted successfully"}), 201

@jobs_bp.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
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

@jobs_bp.route('/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        return jsonify({"error": "Job not found"}), 404

    data = request.get_json()
    job.title = data.get('title', job.title)
    job.description = data.get('description', job.description)
    job.budget = data.get('budget', job.budget)
    db.session.commit()
    return jsonify({"message": "Job updated successfully"}), 200
