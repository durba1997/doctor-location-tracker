from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# In-memory store (NOT DB polling)
doctor_locations = {}

@app.route("/")
def home():
    return "Real-time Doctor Location Tracker is running 🚀"

# Doctor sends live location
@socketio.on('update_location')
def handle_location(data):
    """
    data = {
        "doctor_id": "uuid",
        "lat": 22.5726,
        "lng": 88.3639
    }
    """
    doctor_id = data["doctor_id"]
    doctor_locations[doctor_id] = {
        "lat": data["lat"],
        "lng": data["lng"]
    }

    # Broadcast instantly to all clients
    emit("location_update", {
        "doctor_id": doctor_id,
        "lat": data["lat"],
        "lng": data["lng"]
    }, broadcast=True)

    print(f"📍 Live update from {doctor_id}: {data['lat']}, {data['lng']}")

# Client requests current location (optional)
@socketio.on('get_location')
def get_location(data):
    doctor_id = data["doctor_id"]
    location = doctor_locations.get(doctor_id)

    emit("location_response", {
        "doctor_id": doctor_id,
        "location": location
    })

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
