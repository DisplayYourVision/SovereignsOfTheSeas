print("test")

import socket
import threading

PORT = 10000
SERVER = "3.125.183.140"
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
        print(threading.active_count-1)


print("Server is starting")
start()
