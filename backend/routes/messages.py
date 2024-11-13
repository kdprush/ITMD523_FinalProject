from flask import Blueprint, request, jsonify
from models import Message
from __init__ import db

messages_bp = Blueprint('messages', __name__)

@messages_bp.route('/messages', methods=['POST'])
def send_message():
    data = request.get_json()
    new_message = Message(
        client_id=data['client_id'],
        freelancer_id=data['freelancer_id'],
        message=data['message']
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify({"message": "Message sent successfully"}), 201

@messages_bp.route('/messages', methods=['GET'])
def get_messages():
    client_id = request.args.get('client_id')
    freelancer_id = request.args.get('freelancer_id')
    messages = Message.query.filter_by(client_id=client_id, freelancer_id=freelancer_id).all()
    return jsonify([{
        "message_id": msg.message_id,
        "message": msg.message,
        "created_at": msg.created_at
    } for msg in messages])
