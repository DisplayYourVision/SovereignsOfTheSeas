from flask import Flask, request, jsonify

app = Flask(__name__)

ships = {}

@app.route('/save_ship', methods=['POST'])
def save_ship():
    data = request.get_json()
    ships[data["shipID"]] = data
    return jsonify({"message": "Ship saved"}), 200

@app.route('/get_ship/<int:ship_id>', methods=['GET'])
def get_ship(ship_id):
    return jsonify(ships.get(ship_id, {"error": "Ship not found"}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)