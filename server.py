import socket
import threading

print("boot...")

HOST = "0.0.0.0"
PORT = 10000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

def start():
    server.listen()
    while True:
        conn, addr = server.accept()

print("connecting..")
start()
