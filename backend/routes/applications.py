from flask import Blueprint, request, jsonify
from backend.models import Application, Job, User
from backend import db

applications_bp = Blueprint('applications', __name__)

@applications_bp.route('/', methods=['POST'])
def submit_application():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Validate required fields
        required_fields = ['job_id', 'freelancer_id']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400
        
        # Validate job_id and freelancer_id
        job = Job.query.get(data['job_id'])
        freelancer = User.query.get(data['freelancer_id'])
        if not job:
            return jsonify({"error": "Invalid job_id"}), 404
        if not freelancer or freelancer.user_type != 'freelancer':
            return jsonify({"error": "Invalid freelancer_id or user is not a freelancer"}), 404

        # Create a new application
        new_application = Application(
            job_id=data['job_id'],
            freelancer_id=data['freelancer_id'],
            resume_file_path=data.get('resume_file_path')  # Optional field
        )
        db.session.add(new_application)
        db.session.commit()

        return jsonify({
            "message": "Application submitted successfully",
            "application_id": new_application.application_id
        }), 201

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    

@applications_bp.route('/jobs/<int:job_id>/applications', methods=['GET'])
def get_job_applications(job_id):
    try:
        # Fetch applications for the given job_id
        applications = Application.query.filter_by(job_id=job_id).all()
        if not applications:
            return jsonify({"message": "No applications found for this job"}), 404

        return jsonify([{
            "application_id": app.application_id,
            "freelancer_id": app.freelancer_id,
            "resume_file_path": app.resume_file_path,
            "created_at": app.created_at.isoformat()
        } for app in applications]), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
