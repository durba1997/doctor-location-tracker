

README.md

# Doctor Live Tracking System

Real-time doctor location tracking using:

- **Backend:** Flask + SocketIO + Postgres (Docker)
- **Mobile App:** React Native / Expo (doctor device, background GPS)
- **Web Dashboard:** Google Maps + SocketIO (patients/admin)

---

## Setup

1️⃣ **Start Postgres**
```bash
cd postgres
docker-compose up -d

2️⃣ Run Backend

cd backend
pip install -r requirements.txt
python app.py

3️⃣ Run Mobile App (Doctor)

cd mobile_app
npm install
expo start

4️⃣ Open Web Dashboard

Open web_dashboard/index.html in browser

Update YOUR_SERVER_IP & Google Maps API key



---

How it works

Doctor app sends GPS → Flask server → Postgres → broadcasts → web dashboard updates markers live.

Works in background; last location saved if offline.



---

Enjoy your live doctor tracking 🚀

This is simple, clear, and enough for quick setup.  

If you want, I can make an **ultra-mini one-line version** too for GitHub description.
