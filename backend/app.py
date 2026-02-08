from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# Dictionary to store latest location per doctor
doctor_locations = {}

@socketio.on("location_update")
def handle_location(data):
    """
    data = {
        "doctor_id": str/int,
        "latitude": float,
        "longitude": float
    }
    """
    doctor_id = data.get("doctor_id")
    doctor_locations[doctor_id] = {
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude")
    }

    print(f"Doctor {doctor_id} location:", doctor_locations[doctor_id])

    # Broadcast live location to all connected clients
    socketio.emit("location_broadcast", doctor_locations)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
