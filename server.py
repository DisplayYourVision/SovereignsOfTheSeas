import socket
import json

HOST = "0.0.0.0"  # Listen on all network interfaces
PORT = 65432       # Port number (ensure it's open in your firewall)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server is listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        command = {
            "functionName": "MovePlayer",
            "parameters": { "x": 3, "y": 5 }
        }

        message = json.dumps(command)
        conn.sendall(message.encode('utf-8'))  # Send command to Unity
        print(f"Sent command: {message}")

        data = conn.recv(1024)  # Receive response
        if not data:
            break
        print(f"Received from Unity: {data.decode('utf-8')}")

    conn.close()

if __name__ == "__main__":
    start_server()

