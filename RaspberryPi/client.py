import socket
import sys
import json

def get_device(target):
    with open("devices.json") as f:
        data = json.load(f)
    for device in data["devices"]:
        if device["name"] == target:
            return device
def send(s, message):
    print("Sending message: " + message)
    s.send(message.encode())

def recieve(s):
    data = s.recv(1024).decode()
    print("Received message: " + data)
    return data

def main(target):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((get_device(target)["ip"], 5000))
    return s

if __name__ == "__main__":
    main(sys.argv[1])