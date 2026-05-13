import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5000))

server.listen()

print("Server Started...")

clients = []

def broadcast(message):

    for client in clients:
        client.send(message)

def handle_client(client):

    while True:

        try:
            message = client.recv(1024)

            print("Message Received:", message.decode())

            broadcast(message)

        except:
            clients.remove(client)
            client.close()
            break

while True:

    client, address = server.accept()

    print("New Player Connected:", address)

    clients.append(client)

    client.send("Welcome to Game Server".encode())

    thread = threading.Thread(target=handle_client, args=(client,))

    thread.start()