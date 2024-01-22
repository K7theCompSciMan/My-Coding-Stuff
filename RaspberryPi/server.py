import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8080))
s.listen(5)
s.settimeout(5)
print("Server running")

def send(conn, message):
    print("Sending message: " + message)
    conn.send(message.encode())

def recieve(conn):
    data = conn.recv(1024).decode()
    print("Received message: " + data)
    return data

def main():
    conn, addr = s.accept()
    return conn, addr