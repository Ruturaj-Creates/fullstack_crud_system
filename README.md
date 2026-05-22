# Full Stack FastAPI CRUD Application

A full-stack CRUD application built using FastAPI, PostgreSQL, SQLAlchemy, and React.js.

---

# Tech Stack

## Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

## Frontend
- React.js
- CSS

---

# Features

- Create data
- Read data
- Update data
- Delete data
- REST API integration
- PostgreSQL database connectivity
- Full-stack architecture

---

# Project Structure

```text
backend/
 ├── main.py
 ├── database.py
 ├── db_models.py
 ├── models.py
 └── requirements.txt

frontend/
 ├── src/
 ├── public/
 └── package.json
```

---

# Backend Setup

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\\Scripts\\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Backend Server

```bash
uvicorn backend.main:app --reload
```

---

# Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

# API Documentation

FastAPI automatically provides Swagger UI documentation.

Visit:

```text
http://127.0.0.1:8000/docs
```

---

# Future Improvements

- JWT Authentication
- Docker Support
- Environment Variables
- Better UI Design
- Deployment
- Role-Based Access
- Pagination & Search

---

# Author

Developed by Ruturaj Desai