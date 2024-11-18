from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User
from .. import db

users_bp = Blueprint('users', __name__)

@users_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate incoming data
    required_fields = ['name', 'email','password','user_type']
    missing_fields = [key for key in required_fields if key not in data]
    if missing_fields:
        return jsonify({"error": "Missing required fields","missing": missing_fields}), 400
    
    # Check if user already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "User with this email already exists"}), 409
    
    try:
        new_user = User(
            name=data['name'],
            email=data['email'],
            password=generate_password_hash(data['password']),  # Use hashed passwords in production
            user_type=data['user_type']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully", "user_id": new_user.user_id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate incoming data
    if not all(key in data for key in ['email', 'password']):
        return jsonify({"error": "Missing email or password"}), 400
    
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@users_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    try:
        if 'name' in data:
            user.name = data['name']
        if 'password' in data:
            user.password = generate_password_hash(data['password']) # Hash the new password

        db.session.commit()
        return jsonify({"message": "Profile updated"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": f"An error occurred: {str(e)}"}), 500
