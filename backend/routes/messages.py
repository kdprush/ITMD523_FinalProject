from flask import Blueprint, request, jsonify
from backend.models import Message, User
from backend import db

messages_bp = Blueprint('messages', __name__, url_prefix='/api/messages')

@messages_bp.route('/', methods=['POST'])
def send_message():
    data = request.get_json()

    # Validate incoming data
    if not all(key in data for key in ['client_id', 'freelancer_id', 'message']):
        return jsonify({"error": "Missing required fields"}), 400

    # Check if client and freelancer exist
    client = User.query.get(data['client_id'])
    freelancer = User.query.get(data['freelancer_id'])
    if not client or not freelancer:
        return jsonify({"error": "Invalid client_id or freelancer_id"}), 400

    try:
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
    
@messages_bp.route('/conversations', methods=['GET'])
def get_messages():
    try:
        client_id = request.args.get('client_id')
        freelancer_id = request.args.get('freelancer_id')

        # Base query for all messages
        query = Message.query

        # Filter by client_id if provided
        if client_id:
            query = query.filter_by(client_id=client_id)

        # Filter by freelancer_id if provided
        if freelancer_id:
            query = query.filter_by(freelancer_id=freelancer_id)

        # Execute the query
        messages = query.all()

        # Serialize the messages to JSON
        messages_list = [
            {
                'message_id': message.message_id,
                'client_id': message.client_id,
                'freelancer_id': message.freelancer_id,
                'message': message.message,
                'created_at': message.created_at.isoformat()
            }
            for message in messages
        ]

        return jsonify(messages_list), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

