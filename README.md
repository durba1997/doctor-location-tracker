
---

# 🩺 Doctor Location Tracker (Backend)

A Dockerized Flask backend service for tracking doctor locations securely using PostgreSQL.
Designed to work with an **existing database container** and easy to run on any machine using Docker.

---

## 🚀 Features

* Flask REST API
* PostgreSQL database (Docker)
* Uses existing DB (`ehospital`)
* Docker & Docker Compose ready
* Health check endpoint
* Clean project structure
* Easy to share & deploy

---

## 🛠 Tech Stack

* **Backend:** Python (Flask)
* **Database:** PostgreSQL 15
* **Containerization:** Docker, Docker Compose
* **Environment Management:** `.env`

---

## 📁 Project Structure

```
doctor-location-tracker/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
│
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Prerequisites

Make sure you have:

* Docker
* Docker Compose
* Git

Check:

```bash
docker --version
docker-compose --version
git --version
```

---

## 🧩 Setup Instructions (Step-by-Step)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/durba1997/doctor-location-tracker.git
cd doctor-location-tracker
```

---

### 2️⃣ Create Docker network

```bash
docker network create doctor_network
```

---

### 3️⃣ Run PostgreSQL container

```bash
docker run -d \
  --name eh_postgres \
  --network doctor_network \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin123 \
  -e POSTGRES_DB=ehospital \
  -p 5432:5432 \
  postgres:15
```

---

### 4️⃣ Create `.env` file

Create `backend/.env`:

```
DB_HOST=eh_postgres
DB_PORT=5432
DB_NAME=ehospital
DB_USER=admin
DB_PASSWORD=admin123
```

---

### 5️⃣ Build & run backend

```bash
docker-compose up --build -d
```

---

### 6️⃣ Verify backend is running

Open browser or Postman:

```
http://localhost:5000
http://localhost:5000/health
```

Expected response:

```json
{
  "message": "Doctor Location Tracker Backend Running"
}
```

---

## 🔍 API Endpoints

| Method | Endpoint  | Description      |
| ------ | --------- | ---------------- |
| GET    | `/`       | App status check |
| GET    | `/health` | Health check     |

---

## 🧠 How it works (Simple Explanation)

* Flask app runs inside Docker
* PostgreSQL runs in a separate Docker container
* Both containers talk via Docker network
* Backend connects using container name (`eh_postgres`)
* Ready for frontend or mobile app integration

---

## 👨‍💻 Author

**Durba Kushari**
📧 Email: [durbakushari1997@gmail.com](mailto:durbakushari1997@gmail.com)
🔗 GitHub: [https://github.com/durba1997](https://github.com/durba1997)

---

## ⭐ Future Enhancements

* JWT Authentication
* Doctor & Patient APIs
* Real-time location updates
* Frontend (React / Mobile)
* Deployment on AWS / GCP

---

