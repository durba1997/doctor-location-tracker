from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# -----------------------------
# In-memory last seen store
# -----------------------------
last_seen = {}  # doctor_id -> {name, latitude, longitude, timestamp}

# -----------------------------
# Receive doctor location
# -----------------------------
@socketio.on("location_update")
def handle_location(data):
    doctor_id = data['doctor_id']
    now = datetime.utcnow()
    
    # Update last seen
    last_seen[doctor_id] = {
        "name": data['name'],
        "latitude": data['latitude'],
        "longitude": data['longitude'],
        "timestamp": now
    }

    # Broadcast live location to all clients
    socketio.emit("location_broadcast", {
        "doctor_id": doctor_id,
        "name": data['name'],
        "latitude": data['latitude'],
        "longitude": data['longitude'],
        "online": True
    })

# -----------------------------
# REST API to get last seen
# -----------------------------
@app.route("/last_seen")
def get_last_seen():
    now = datetime.utcnow()
    result = {}
    for doctor_id, info in last_seen.items():
        online = (now - info['timestamp']) < timedelta(seconds=30)  # online if updated in last 30s
        result[doctor_id] = {
            "name": info['name'],
            "latitude": info['latitude'],
            "longitude": info['longitude'],
            "last_seen": info['timestamp'].isoformat(),
            "online": online
        }
    return jsonify(result)

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    print("Starting real-time doctor tracking server with last seen...")
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
