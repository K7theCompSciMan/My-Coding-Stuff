import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8080))
s.listen(5)
s.settimeout(5)
print("Server running")

def send(message):
    print("Sending message: " + message)
    conn.send(message.encode())

def recieve():
    data = conn.recv(1024).decode()
    print("Received message: " + data)
    return data

while True:
    conn, addr = s.accept()
    print("Connected to " + addr[0] + ":" + str(addr[1]))
    send("Hello from the server")
    recieve()
