from flask import Blueprint, request, jsonify
from models import Application
from __init__ import db

applications_bp = Blueprint('applications', __name__)

@applications_bp.route('/applications', methods=['POST'])
def submit_application():
    data = request.get_json()
    new_application = Application(
        job_id=data['job_id'],
        freelancer_id=data['freelancer_id'],
        resume_file_path=data['resume_file_path']
    )
    db.session.add(new_application)
    db.session.commit()
    return jsonify({"message": "Application submitted successfully"}), 201

@applications_bp.route('/jobs/<int:job_id>/applications', methods=['GET'])
def get_job_applications(job_id):
    applications = Application.query.filter_by(job_id=job_id).all()
    return jsonify([{
        "application_id": app.application_id,
        "freelancer_id": app.freelancer_id,
        "resume_file_path": app.resume_file_path,
        "created_at": app.created_at
    } for app in applications])
