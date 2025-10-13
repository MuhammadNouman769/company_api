# 🏢 Company API

A Django REST API to manage company data, employees, and organizational details.  
This project is built using **Django REST Framework (DRF)** and demonstrates CRUD operations with relational data.

---

## 🚀 Features
- Company and Employee Management  
- RESTful API with Django REST Framework  
- SQLite3 Database (default, can be changed to PostgreSQL)  
- Swagger & ReDoc API Documentation  
- Admin Panel for managing data easily  

---

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework  
- **Database:** SQLite3  
- **Language:** Python 3.12+  
- **Documentation:** Swagger / Redoc  

---

## 📂 Project Structure


companyapi/
│
├── .venv/                  # Python virtual environment
├── .vscode/                # VS Code settings
├── apps/                   # Django apps
│   ├── company_api/        # Company app
│   │   ├── migrations/     # Migration files
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   └── employees_api/      # Employee app
│       ├── migrations/
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── urls.py
│       └── views.py
│
├── core/                   # Project core (settings, urls, wsgi/asgi)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── db.sqlite3              # Default SQLite database
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
