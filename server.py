from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Dictionary to store multiple ships (key = shipID)
ships = {}
next_ship_id = 1  # Auto-incrementing ship ID

# Create a New Ship
@app.route('/spawn_ship', methods=['POST'])
def spawn_ship():
    global next_ship_id
    new_ship = {
        "shipID": next_ship_id,
        "x": random.uniform(-10, 10),
        "y": random.uniform(-10, 10),
        "z": random.uniform(-10, 10)
    }
    ships[next_ship_id] = new_ship
    next_ship_id += 1
    return jsonify(new_ship), 200

# Update Ship Position
@app.route('/update_ship/<int:ship_id>', methods=['POST'])
def update_ship(ship_id):
    if ship_id not in ships:
        return jsonify({"error": "Ship not found"}), 404
    data = request.get_json()
    ships[ship_id]["x"] = data["x"]
    ships[ship_id]["y"] = data["y"]
    ships[ship_id]["z"] = data["z"]
    return jsonify({"message": "Ship updated"}), 200

# Get All Ships
@app.route('/get_all_ships', methods=['GET'])
def get_all_ships():
    return jsonify(list(ships.values())), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
