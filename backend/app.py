from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'eh_postgres'),
        database=os.getenv('DB_NAME', 'ehospital'),
        user=os.getenv('DB_USER', 'admin'),
        password=os.getenv('DB_PASSWORD', 'admin123')
    )
    return conn

# Health check
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"message": "Doctor Location Tracker Backend Running"})

# Get all doctors (optional)
@app.route('/doctors', methods=['GET'])
def get_doctors():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM doctor_location;")
    doctors = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(doctors)

# Get location of a doctor by ID (permission-based)
@app.route('/doctor/<int:doctor_id>/location', methods=['GET'])
def get_doctor_location(doctor_id):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT latitude, longitude, permission_granted FROM doctor_location WHERE doctor_id=%s;",
        (doctor_id,)
    )
    doctor = cursor.fetchone()
    cursor.close()
    conn.close()

    if not doctor:
        return jsonify({"error": "Doctor not found"}), 404

    if not doctor['permission_granted']:
        return jsonify({"error": "Permission not granted by doctor"}), 403

    return jsonify({
        "doctor_id": doctor_id,
        "latitude": doctor['latitude'],
        "longitude": doctor['longitude']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
