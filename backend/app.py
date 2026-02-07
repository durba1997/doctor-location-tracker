from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

# Database config (Docker-safe)
DB_HOST = os.getenv("DB_HOST", "eh_postgres")
DB_NAME = os.getenv("DB_NAME", "doctor_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )


@app.route("/")
def home():
    return jsonify({"status": "Backend running 🚀"})


@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"db": "connected ✅"})
    except Exception as e:
        return jsonify({"db": "failed ❌", "error": str(e)}), 500


@app.route("/init-db")
def init_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            latitude FLOAT,
            longitude FLOAT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": "Database initialized 🧱"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/doctors", methods=["POST"])
def add_doctor():
    data = request.json
    name = data.get("name")
    lat = data.get("latitude")
    lon = data.get("longitude")

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO doctors (name, latitude, longitude) VALUES (%s, %s, %s)",
            (name, lat, lon)
        )

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": "Doctor added 🧑‍⚕️"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/doctors", methods=["GET"])
def get_doctors():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT id, name, latitude, longitude FROM doctors;")
        rows = cur.fetchall()

        cur.close()
        conn.close()

        doctors = []
        for r in rows:
            doctors.append({
                "id": r[0],
                "name": r[1],
                "latitude": r[2],
                "longitude": r[3]
            })

        return jsonify(doctors)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
