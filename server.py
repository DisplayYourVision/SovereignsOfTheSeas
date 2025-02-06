print("test")

import socket
import threading

PORT = 8080
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def client(conn, addr):
    print("new client")
    print(addr)
    conn.close()

def start():
    server.listen()

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=client, args=(conn,addr))
        thread.start()


print("Server is starting")
start()
