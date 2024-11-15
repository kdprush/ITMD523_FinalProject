from flask import Blueprint, request, jsonify
from ..models import Application
from .. import db

applications_bp = Blueprint('applications', __name__)

@applications_bp.route('/applications', methods=['POST'])
def submit_application():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        required_fields = ['job_id', 'freelancer_id']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400
    
        new_application = Application(
            job_id=data['job_id'],
            freelancer_id=data['freelancer_id'],
            resume_file_path=data['resume_file_path']
        )
        db.session.add(new_application)
        db.session.commit()

        return jsonify({
            "message": "Application submitted successfully",
            "application_id" : new_application.application_id
        }), 201

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    

@applications_bp.route('/jobs/<int:job_id>/applications', methods=['GET'])
def get_job_applications(job_id):
    try:
        applications = Application.query.filter_by(job_id=job_id).all()
        if not applications:
            return jsonify({"message": "No applications found for this job"}), 404

        return jsonify ([{
            "application_id": app.application_id,
            "freelancer_id": app.freelancer_id,
            "resume_file_path": app.resume_file_path,
            "created_at": app.created_at.isoformat()
        } for app in applications])

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500