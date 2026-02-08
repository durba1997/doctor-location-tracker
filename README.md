Here’s a clean README for your real-time doctor tracker with last seen + online/offline 🚀


---

README.md

# Real-Time Doctor Tracking System 🚑

**Track doctors live on a map!**  
Doctors send their GPS from a mobile app, and patients/admins can see them instantly on a web dashboard. Markers show **green = online**, **gray = offline**, with last seen timestamps. No database needed — fully real-time.

---

## Features

- Real-time location updates via **SocketIO**
- **Last seen tracking** (online/offline)
- Lightweight: **no database**, in-memory storage only
- Works on **mobile (React Native/Expo)** + **web dashboard (Google Maps)**
- Easy to deploy with minimal setup

---

## Setup

### 1️⃣ Backend

```bash
cd backend
pip install -r requirements.txt
python app.py

Server runs at http://localhost:5000

2️⃣ Mobile App (Doctor)

cd mobile_app
npm install
expo start

Sends live location every few seconds

Works in background


3️⃣ Web Dashboard

Open web_dashboard/index.html in browser

Replace YOUR_SERVER_IP with backend IP

Google Maps API key required

Dashboard shows online/offline doctors with colored markers



---

How It Works

1. Doctor app → SocketIO → Flask server → dashboard


2. Backend keeps last seen timestamp


3. Dashboard updates markers live and changes online/offline status automatically




---

Notes

Offline doctors appear gray

If server restarts, last seen info is lost

Lightweight and fast, no database required

Can be extended to save history in a DB if needed later



---

