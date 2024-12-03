from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from backend.models import User
from backend import db

# Prefix all routes with /users
users_bp = Blueprint('users', __name__, url_prefix='/api/users')

@users_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    # Validate incoming data
    required_fields = ['name', 'email', 'password', 'role']
    missing_fields = [key for key in required_fields if key not in data]
    if missing_fields:
        return jsonify({"error": "Missing required fields", "missing": missing_fields}), 400

    if data['role'] not in ['client', 'freelancer', 'admin']:
        return jsonify({"error": "Invalid user type"}), 400

    try:
        # Check if user already exists
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return jsonify({"error": "User with this email already exists"}), 409

        # Create new user with hashed password
        hashed_password = generate_password_hash(data['password'])
        print(f"Hashed Password during Registration: {hashed_password}")  # Debugging line

        new_user = User(
            name=data['name'],
            email=data['email'],
            password=hashed_password,  # Store the hashed password
            role=data['role']
        )
        db.session.add(new_user)
        db.session.commit()
        print("User successfully added to database.")  # Debugging line

        return jsonify({"message": "User registered successfully", "user_id": new_user.user_id}), 201

    except Exception as e:
        db.session.rollback()
        print(f"An error occurred during registration: {str(e)}")  # Debugging line
        return jsonify({"error": f"An error occurred during registration: {str(e)}"}), 500

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate incoming data
    if not all(key in data for key in ['email', 'password']):
        return jsonify({"error": "Missing email or password"}), 400

    try:
        user = User.query.filter_by(email=data['email']).first()
        
        if user:
            print(f"User found with email: {user.email}")  # Debugging line
        else:
            print("User not found")  # Debugging line

        if user and check_password_hash(user.password, data['password']):
            print("Password matched")  # Debugging line
            return jsonify({"message": "Login successful"}), 200
        else:
            print("Invalid credentials")  # Debugging line
            return jsonify({"error": "Invalid credentials"}), 401

    except Exception as e:
        print(f"An error occurred during login: {str(e)}")  # Debugging line
        return jsonify({"error": f"An error occurred during login: {str(e)}"}), 500

@users_bp.route('/profile', methods=['PUT'])
def update_profile(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        data = request.get_json()

        if 'name' in data:
            user.name = data['name']
        if 'password' in data:
            if len(data['password']) < 6:
                return jsonify({"error": "Password must be at least 6 characters long"}), 400
            user.password = generate_password_hash(data['password'])  # Hash the new password

        db.session.commit()
        return jsonify({"message": "Profile updated successfully"}), 200

    except Exception as e:
        db.session.rollback()
        print(f"An error occurred during profile update: {str(e)}")  # Debugging line
        return jsonify({"error": f"An error occurred during profile update: {str(e)}"}), 500
