# client.py
import requests
import json
import socket

server_ports = [8081, 8082] #list of server ports

def register(client_id, preferred_port): #function to register the client with the server
    ports = [preferred_port] + [port for port in server_ports if port != preferred_port]
    for port in ports:
        server_url = f"http://localhost:{port}"
        url = f"{server_url}/register"
        data = {'client_id': client_id, 'port': port}
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200: #prints this if the message is sent
                print(response.json())
                if port != preferred_port:
                    print(f"Note: Your preferred server on port {preferred_port} is down. You have been registered on port {port} instead.")
                return server_url
            else:
                print(f"Error: Registration failed with status code {response.status_code}") #prints this if the message is not sent
        except requests.exceptions.RequestException:
            print(f"Error: Unable to connect to {server_url}")
    return None

def share(server_url, sender_id, receiver_id, message):
    url = f"{server_url}/share"
    data = {'sender_id': sender_id, 'receiver_id': receiver_id, 'message': message}
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, json=data, headers=headers)  # Send JSON data with headers
        if response.status_code == 200:
            print(f"Message sent to {receiver_id}: {message}")
            print(response.json())
        else:
            print(f"Error: Sharing data failed with status code {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"Error: Unable to connect to {server_url}")

if __name__ == '__main__':
    client_id = input("Enter your client ID: ")
    preferred_port = int(input("Enter your preferred server port: "))
    server_url = register(client_id, preferred_port)
    if server_url is not None:
        while True:
            receiver_id = input("Enter the receiver's client ID: ")
            message = input("Enter the message to share: ")
            share(server_url, client_id, receiver_id, message)