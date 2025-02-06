import socket
import os

HOST = "0.0.0.0"  # Listen on all network interfaces
PORT = int(os.getenv("PORT", 10000))  # Use Render's assigned port or default to 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Server running on {HOST}:{PORT}")

while True:
    client, addr = server.accept()
    print(f"Connection from {addr}")
    client.send(b"Hello from server!")
    client.close()

