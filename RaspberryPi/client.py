import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('raspberrypi', 5000))


def send(message):
    print("Sending message: " + message)
    s.send(message.encode())

def recieve():
    data = s.recv(1024).decode()
    print("Received message: " + data)
    return data

while True:
    print(f"Connected to server")
    recieve()
    send(sys.argv[1])
    