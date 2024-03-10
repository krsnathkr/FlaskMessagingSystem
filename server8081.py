# server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Store registered clients
clients = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    client_id = data.get('client_id')
    port = data.get('port')
    if client_id and port:
        clients[client_id] = port
        return jsonify({'message': f'Client {client_id} registered on port {port}'}), 200
    else:
        return jsonify({'message': 'Invalid data'}), 400

@app.route('/share', methods=['POST'])
def share():
    data = request.get_json()
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    message = data.get('message')
    if sender_id and receiver_id and message and sender_id in clients and receiver_id in clients:
        # In a real-world application, you would send the message to the receiver here
        return jsonify({'message': f'Message from {sender_id} to {receiver_id}: {message}'}), 200
    else:
        return jsonify({'message': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(port=8081)