# 📝 Task Manager API

A RESTful API for managing tasks, built using **FastAPI** with a clean layered architecture (Router → Service → Repository → Database). This project focuses on clean code practices, proper exception handling, and scalable backend design.

---

## 🚀 Tech Stack

| Layer      | Technology     |
| ---------- | -------------- |
| Framework  | FastAPI        |
| Database   | SQLite         |
| ORM        | SQLAlchemy     |
| Validation | Pydantic       |
| Server     | Uvicorn        |
| Logging    | Python Logging |

---

## 📁 Project Structure

```
Task_Manager_API/
├── src/
│   ├── core/
│   │   └── logger.py               # Logging configuration
│   ├── database/
│   │   ├── __init__.py
│   │   ├── base.py                 # SQLAlchemy Base
│   │   └── engine.py               # DB engine & session
│   ├── models/
│   │   └── task_model.py           # ORM model
│   ├── repository/
│   │   └── task_repo.py            # Data access layer
│   ├── routers/
│   │   └── task_routes.py          # API routes
│   ├── schema/
│   │   └── task_schema.py          # Pydantic schemas
│   ├── services/
│   │   └── task_service.py         # Business logic
│   └── utils/
│       └── task_logger.py          # Custom logging utils
├── main.py                         # Entry point
├── config.py                       # App configuration
├── requirements.txt
├── .env
└── .gitignore
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AmoghShukla/Task_Manager_API.git
cd Task_Manager_API
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv venv

# Windows
venv\\Scripts\\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=sqlite:///./tasks.db
```

---

### 5. Run the Server

```bash
uvicorn main:app --reload
```

The API will be live at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 📖 API Documentation

| UI         | URL                                                        |
| ---------- | ---------------------------------------------------------- |
| Swagger UI | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)   |
| ReDoc      | [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) |

---

## 🔌 API Endpoints

### Base

| Method | Endpoint | Description  |
| ------ | -------- | ------------ |
| `GET`  | `/`      | Health check |

### Tasks

| Method   | Endpoint      | Description    |
| -------- | ------------- | -------------- |
| `GET`    | `/tasks`      | Get all tasks  |
| `GET`    | `/tasks/{id}` | Get task by ID |
| `POST`   | `/tasks`      | Create task    |
| `PUT`    | `/tasks/{id}` | Update task    |
| `DELETE` | `/tasks/{id}` | Delete task    |

---

## 📦 Dependencies

```
fastapi
uvicorn
sqlalchemy
pydantic
python-dotenv
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "Add feature"`
4. Push: `git push origin feature/your-feature`
5. Open PR

---

## 📄 License

MIT License
