from flask import Flask, jsonify, request
from threading import Thread
import time
from flask import Flask, jsonify, request, redirect
import socket

app = Flask(__name__)
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
        if not check_port(clients[sender_id]):
            return redirect("http://localhost:8081/share", code=307)
        return jsonify({'message': f'Message from {sender_id} to {receiver_id}: {message}'}), 200
    else:
        return jsonify({'message': 'Invalid data'}), 400

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect(('localhost', port))
        sock.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        sock.close()

def reassign_clients():
    while True:
        for client_id, port in list(clients.items()):
            if not check_port(port):
                new_port = find_new_port()  # You need to implement this function
                clients[client_id] = new_port
        time.sleep(1)  # Check every minute

@app.route('/check_and_move', methods=['POST'])
def check_and_move():
    data = request.get_json()
    client_id = data.get('client_id')
    new_port = data.get('new_port')
    if client_id in clients:
        old_port = clients[client_id]
        if not check_port(old_port):
            clients[client_id] = new_port
            return jsonify({'message': f'Client {client_id} moved to port {new_port}'}), 200
        else:
            return jsonify({'message': 'Port is working'}), 200
    else:
        return jsonify({'message': 'Invalid client_id'}), 400

if __name__ == '__main__':
    reassign_thread = Thread(target=reassign_clients)
    reassign_thread.start()
    app.run(port=8080)