from flask import Blueprint, request, jsonify
from backend.models import Message
from backend import db

messages_bp = Blueprint('messages', __name__)

@messages_bp.route('/messages', methods=['POST'])
def send_message():
    """
    Endpoint to send a message between client and freelancer.
    """
    try:
        data = request.get_json()

        # Validate required fields
        if not all(key in data for key in ('client_id', 'freelancer_id', 'message')):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Create a new message
        new_message = Message(
            client_id=data['client_id'],
            freelancer_id=data['freelancer_id'],
            message=data['message']
        )
        db.session.add(new_message)
        db.session.commit()

        return jsonify({"message": "Message sent successfully", "message_id": new_message.message_id}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    

@messages_bp.route('/messages', methods=['GET'])
def get_messages():
    """
    Endpoint to retrieve messages between a client and a freelancer
    """
    try:
        client_id = request.args.get('client_id')
        freelancer_id = request.args.get('freelancer_id')

        # validate query parameters
        if not client_id or not freelancer_id:
            return jsonify({"error": "Both client_id and freelancer_id are required"}), 400
        
        # Fetch messages
        messages = Message.query.filter_by(client_id=client_id, freelancer_id=freelancer_id).all()

        if not messages:
            return jsonify({"messages": "No messages found"}), 404
        
        # Serialize and return messages
        return jsonify([{
            "message_id": msg.message_id,
            "message": msg.message,
            "created_at": msg.created_at
    } for msg in messages]), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
