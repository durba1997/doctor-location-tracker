from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# =========================
# REAL-TIME LOCATION SOCKET
# =========================
@socketio.on("location_update")
def handle_location(data):
    """
    data = {
        doctor_id: int,
        name: str,
        latitude: float,
        longitude: float
    }
    """
    print("Live location received:", data)
    
    # Broadcast live location to all connected clients
    socketio.emit("location_broadcast", data)

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    print("Starting real-time doctor tracking server...")
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
