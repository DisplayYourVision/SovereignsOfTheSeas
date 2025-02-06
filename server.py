import socket
import threading

print("boot...")

HOST = "127.0.0.1"
PORT = 10000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        print(f"Connected by {addr}")

print("connecting..")
start()
