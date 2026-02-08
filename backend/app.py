from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="127.0.0.1",
        port=5432,
        database="ehospital",
        user="admin",
        password="admin123"
    )

@app.route("/", methods=["GET"])
def home():
    return {"status": "Backend running 🚀"}

@app.route("/doctor/<doctor_id>/permission", methods=["POST"])
def update_permission(doctor_id):
    data = request.get_json()
    permission = data.get("permission")

    if permission is None:
        return {"error": "permission field missing"}, 400

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO permissions (doctor_id, permission, updated_at)
        VALUES (%s, %s, %s)
        ON CONFLICT (doctor_id)
        DO UPDATE SET permission = EXCLUDED.permission,
                      updated_at = EXCLUDED.updated_at;
    """, (doctor_id, permission, datetime.utcnow()))

    conn.commit()
    cur.close()
    conn.close()

    return {
        "message": "Permission updated successfully ✅",
        "doctor_id": doctor_id,
        "permission": permission
    }

@app.route("/permissions", methods=["GET"])
def get_permissions():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""
        SELECT d.first_name, d.last_name, p.permission, p.updated_at
        FROM permissions p
        JOIN doctors d ON d.id = p.doctor_id
    """)

    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)
