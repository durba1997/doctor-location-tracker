from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
import psycopg2
from datetime import datetime

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# ------------------------
# Postgres connection
# ------------------------
DB_PARAMS = {
    "dbname": "doctor_db",
    "user": "postgres",
    "password": "postgres",
    "host": "db",   # Docker service name
    "port": 5432
}

# Initialize DB
def init_db():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS doctors (
            doctor_id INT PRIMARY KEY,
            name TEXT,
            last_lat DOUBLE PRECISION,
            last_lon DOUBLE PRECISION,
            last_seen TIMESTAMP
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

init_db()

# ------------------------
# Socket: receive doctor location
# ------------------------
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
    now = datetime.utcnow()
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO doctors (doctor_id, name, last_lat, last_lon, last_seen)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (doctor_id)
        DO UPDATE SET name = EXCLUDED.name,
                      last_lat = EXCLUDED.last_lat,
                      last_lon = EXCLUDED.last_lon,
                      last_seen = EXCLUDED.last_seen
    """, (data['doctor_id'], data['name'], data['latitude'], data['longitude'], now))
    conn.commit()
    cur.close()
    conn.close()

    # Broadcast to all connected clients
    socketio.emit("location_broadcast", data)

# ------------------------
# REST API: all doctors
# ------------------------
@app.route("/doctors")
def get_doctors():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("SELECT doctor_id, name, last_lat, last_lon, last_seen FROM doctors")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    result = [{"doctor_id": r[0], "name": r[1], "latitude": r[2], "longitude": r[3], "last_seen": r[4]} for r in rows]
    return jsonify(result)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
