from http import client
import socket

from flask import app, jsonify, request

def check_port(port):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)  # Set a timeout for the connection attempt

    try:
        # Try to connect to the port on localhost
        sock.connect(('localhost', port))
        sock.shutdown(socket.SHUT_RDWR)
        return True
    except Exception as e:  # Specify the exception class
        return False
    finally:
        sock.close()

clients = {}  # Define the "clients" dictionary

@app.route('/check_and_move', methods=['POST'])
def check_and_move():
    data = request.get_json()
    client_id = data.get('client_id')
    new_port = data.get('new_port')

    if client_id in clients:  # Use the "clients" dictionary
        old_port = clients[client_id]
        if not check_port(old_port):
            clients[client_id] = new_port
            return jsonify({'message': f'Client {client_id} moved to port {new_port}'}), 200
        else:
            return jsonify({'message': 'Port is working'}), 200
    else:
        return jsonify({'message': 'Invalid client_id'}), 400