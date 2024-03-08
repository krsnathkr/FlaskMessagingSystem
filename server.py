# server.py
from flask import Flask, request, jsonify
import requests
import threading

app = Flask(__name__)
clients = {}
servers = []

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    client_id = data['client_id']
    port = data['port']
    clients[client_id] = {'ip': request.remote_addr, 'port': port}
    return jsonify({'message': 'Registered successfully'})

@app.route('/share', methods=['POST'])
def share():
    data = request.get_json()
    sender_id = data['sender_id']
    receiver_id = data['receiver_id']
    message = data['message']
    if receiver_id in clients:
        receiver_ip = clients[receiver_id]['ip']
        receiver_port = clients[receiver_id]['port']
        send_message(receiver_ip, receiver_port, message)
        return jsonify({'message': 'Data shared successfully'})
    else:
        return jsonify({'message': 'Receiver not found'}), 404

@app.route('/receive', methods=['POST'])
def receive():
    message = request.form.get('message')
    print(f"Received message: {message}")
    return jsonify({'message': 'Message received'})

def send_message(ip, port, message):
    url = f"http://{ip}:{port}/receive"
    data = {'message': message}
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")
    else:
        print(f"Message sent successfully: {message}")

def run_server(port):
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    ports = [8080, 8081, 8082]  # List of ports to run server instances on

    for port in ports:
        server = threading.Thread(target=run_server, args=(port,))
        servers.append(server)
        server.start()

    for server in servers:
        server.join()