import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 5000))

name = input("Enter Player Name: ")

client.send(name.encode())

def receive():

    while True:

        message = client.recv(1024)

        print("\n", message.decode())

threading.Thread(target=receive).start()

while True:

    msg = input()

    message = name + ": " + msg

    client.send(message.encode())