'''
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)

ships = {}  # Dictionary to store all ships

# 1️⃣ Add a new ship and return a unique ship ID
@app.route('/add_ship', methods=['POST'])
def add_ship():
    shipID = random.randint(1000, 9999)  # Generate a unique ID
    data = request.get_json()  # Get ship position

    # Store new ship
    ships[shipID] = {
        "shipID": shipID,
        "x": data["x"],
        "y": data["y"],
        "z": data["z"]
    }

    return jsonify({"shipID": shipID}), 200  # Return the new ship ID

# 2️⃣ Update an existing ship's position
@app.route('/update_ship', methods=['POST'])
def update_ship():
    data = request.get_json()
    shipID = data["shipID"]

    if shipID in ships:
        ships[shipID]["x"] = data["x"]
        ships[shipID]["y"] = data["y"]
        ships[shipID]["z"] = data["z"]
        return jsonify({"message": "Ship position updated"}), 200
    else:
        return jsonify({"error": "Ship not found"}), 404

# 3️⃣ Get all ships
@app.route('/get_all_ships', methods=['GET'])
def get_all_ships():
    return jsonify(list(ships.values())), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
'''

print("test")

import socket
import threading

PORT = 5050
SERVER = "192.168.0.128"
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
