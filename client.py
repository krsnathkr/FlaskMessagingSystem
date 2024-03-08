# client.py
import requests
import json

server_url = 'http://localhost:8080'

def register(client_id, port):
    url = f"{server_url}/register"
    data = {'client_id': client_id, 'port': port}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: Registration failed with status code {response.status_code}")

def share(sender_id, receiver_id, message):
    url = f"{server_url}/share"
    data = {'sender_id': sender_id, 'receiver_id': receiver_id, 'message': message}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)  # Send JSON data with headers
    if response.status_code == 200:
        print(f"Message sent to {receiver_id}: {message}")
        print(response.json())
    else:
        print(f"Error: Sharing data failed with status code {response.status_code}")

if __name__ == '__main__':
    client_id = input("Enter your client ID: ")
    port = int(input("Enter your port number: "))
    register(client_id, port)

    while True:
        receiver_id = input("Enter the receiver's client ID: ")
        message = input("Enter the message to share: ")
        share(client_id, receiver_id, message)