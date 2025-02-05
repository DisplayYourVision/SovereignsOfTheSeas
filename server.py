from flask import Flask, request, jsonify

app = Flask(__name__)

# Store all ships (key = shipID)
ships = {}

# Update ship position
@app.route('/update_ship', methods=['POST'])
def update_ship():
    data = request.get_json()
    shipID = data["shipID"]
    ships[shipID] = data  # Store ship position
    return jsonify({"message": "Ship position updated"}), 200

# Get all ship positions
@app.route('/get_all_ships', methods=['GET'])
def get_all_ships():
    return jsonify(list(ships.values())), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

