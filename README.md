
---

Real-Time Multi-Doctor Tracking System 🚑

Track multiple doctors live on a map!
This project simulates doctors sending GPS locations to a backend. A web dashboard shows real-time locations, online/offline status, and last seen timestamps. No real doctors required — fully simulated for college/demo purposes.


---

Features

🌐 Real-time location updates via SocketIO

⏱ Last seen tracking (online/offline markers)

⚡ Multi-doctor simulation (3–5 fake doctors)

💻 Web dashboard with Google Maps

📱 Fake mobile app (React Native/Expo) simulates doctors sending location

🛠 Lightweight: in-memory storage, no database needed

✅ Easy to run for college/demo



---

Hardware Requirements

Component	Minimum	Recommended

CPU	Dual-core 2.0 GHz	Quad-core 2.5+ GHz
RAM	4 GB	8 GB+
Storage	1 GB free	5 GB free
Internet	Stable 2G/3G	Stable 4G/5G
Mobile (Doctor app)	Android/iOS device or simulator	Modern smartphone
PC/Browser (Dashboard)	Any modern browser	Chrome/Firefox/Edge latest



---

Software Requirements

Component	Version / Notes

Python	3.9+
Flask	Latest
Flask-SocketIO	Latest
pip	Latest
Node.js / npm	16+
Expo CLI	Latest
Google Maps API	Enabled for dashboard
Browser	Chrome / Firefox / Edge (latest)
Operating System	Windows / Linux / macOS



---

Folder Structure

doctor_tracker/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── fake_doctor_app/
│   ├── App.js
│   ├── package.json
│   └── node_modules/ (created after npm install)
└── web_dashboard/
    └── index.html


---

Setup & Run

1️⃣ Backend

cd backend
pip install -r requirements.txt
python app.py

Runs on http://localhost:5000



---

2️⃣ Fake Doctor App (React Native / Expo)

cd fake_doctor_app
npm install
expo start

Sends random GPS locations for 3–5 fake doctors every 5 seconds

Works on simulator or real phone



---

3️⃣ Web Dashboard

Open web_dashboard/index.html in browser

Replace YOUR_SERVER_IP with backend IP

Google Maps API key required

Shows doctors as green (online) or gray (offline) markers with last seen timestamps



---

How It Works

1. Fake doctor app → SocketIO → Flask backend → Web dashboard


2. Backend keeps last seen timestamps in memory


3. Dashboard updates markers live, shows online/offline automatically




---

Notes

Offline doctors appear gray

Last seen info is lost if server restarts

Can be extended to save history in a database

Lightweight, fast, and perfect for college/demo projects



---

Optional Improvements for Demo

Assign different speeds or paths for each doctor to look realistic

Use different colors per doctor

Add doctor names on markers instead of IDs



