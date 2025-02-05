from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Enable WebSockets

# Store connected clients and their ships
clients = {}
ships = []  # Store ShipData objects

# ShipData structure
class ShipData:
    def __init__(self, shipID, position):
        self.shipID = shipID
        self.position = position

# When a client connects, assign them a ShipData
@socketio.on('connect')
def handle_connect():
    ship_id = len(clients)  # Unique ship ID based on the number of connected clients
    new_ship = ShipData(ship_id, {"x": 0, "y": 0, "z": 0})  # Initial position of the ship

    ships.append(new_ship)  # Store the ship in the list
    clients[request.sid] = new_ship  # Associate the client with the ship

    # Send the ShipData to the client
    emit('assign_ship', {
        "shipID": new_ship.shipID,
        "position": new_ship.position
    })
    print(f"Client {request.sid} connected and assigned ShipID {new_ship.shipID}")

# When a client sends a new target position, broadcast it to all clients
@socketio.on('set_target_position')
def handle_set_target_position(data):
    ship_id = data["shipID"]
    target_position = data["targetPosition"]

    # Find the ship and update its target position
    for ship in ships:
        if ship.shipID == ship_id:
            ship.position = target_position
            print(f"Ship {ship_id} target updated to {target_position}")
            break

    # Broadcast the new target position to all clients
    emit('move_ship', {
        "shipID": ship_id,
        "targetPosition": target_position
    }, broadcast=True)

# When a client disconnects, remove their ship data
@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in clients:
        ship = clients.pop(request.sid)  # Remove client and ship data from dictionary
        print(f"Client {request.sid} disconnected, removed ShipID {ship.shipID}")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)

