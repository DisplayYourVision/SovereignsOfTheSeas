import socket
import threading

print("boot...")

PORT = 10000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_IENT, socket.SOCK_STREAM)
server.bind(ADDR)

def start():
    server.listen()
    while True:
        conn, addr = server.accept()

print("connecting..")
start()
