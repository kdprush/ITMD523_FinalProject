from flask import Blueprint, request, jsonify
from ..models import User
from __init__ import db

users_bp = Blueprint('users', __name__)

@users_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(
        name=data['name'],
        email=data['email'],
        password=data['password'],  # Use hashed passwords in production
        user_type=data['user_type']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email'], password=data['password']).first()
    if user:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@users_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user.name = data.get('name', user.name)
    user.password = data.get('password', user.password)  # Again, hash passwords in production
    db.session.commit()
    return jsonify({"message": "Profile updated"}), 200
