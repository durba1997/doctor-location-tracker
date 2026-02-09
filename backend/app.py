from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# In-memory storage for doctor locations
doctors = {}

# Receive location updates
@socketio.on("location_update")
def handle_location(data):
    doctor_id = data["id"]
    latitude = data["lat"]
    longitude = data["lon"]
    
    doctors[doctor_id] = {
        "lat": latitude,
        "lon": longitude,
        "last_seen": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "online": True
    }
    
    # Broadcast updated data to all dashboard clients
    socketio.emit("update_doctors", doctors)

# Handle disconnects (simulate offline)
@socketio.on("disconnect")
def handle_disconnect():
    for doc_id in doctors:
        doctors[doc_id]["online"] = False
        doctors[doc_id]["last_seen"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    socketio.emit("update_doctors", doctors)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
