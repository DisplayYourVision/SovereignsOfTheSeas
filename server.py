import socket
import threading

PORT = 10000
SERVER = "0.0.0.0"  # Listen on all network interfaces
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

def handle_client(conn, addr):
    print(f"New connection from {addr}")

    while True:
        try:
            message = conn.recv(1024).decode("utf-8")  # Receive message (max 1024 bytes)
            if not message:
                break  # Client disconnected

            print(f"Received: {message} from {addr}")
            
            # Optionally send a response
            response = "Message received"
            conn.send(response.encode("utf-8"))

        except ConnectionResetError:
            print(f"Client {addr} disconnected")
            break

    conn.close()

def start():
    print("Server is starting...")

    while True:
        conn, addr = server.accept()  # Accept new connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

print("Server is running...")
start()

