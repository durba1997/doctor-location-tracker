from flask import Flask, request
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")

# =========================
# REAL-TIME LOCATION SOCKET
# =========================
@socketio.on("location_update")
def handle_location(data):
    """
    Expects:
    data = {
        "doctor_id": int,
        "latitude": float,
        "longitude": float
    }
    """
    print(f"Live location received: {data}")
    
    # Broadcast live location to all clients
    socketio.emit("location_broadcast", data)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
