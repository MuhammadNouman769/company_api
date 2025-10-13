🏢 Company API

A Django REST Framework (DRF) project to manage company data, employees, and organizational details.
This project demonstrates CRUD operations and relational database management using Django.

🚀 Features

✅ Company and Employee Management
✅ RESTful API built with Django REST Framework
✅ SQLite3 Database (default, easily switchable to PostgreSQL)
✅ Interactive API Documentation with Swagger & ReDoc
✅ Admin Panel for easy data management

🛠️ Tech Stack
Component	Technology
Backend	Django, Django REST Framework
Database	SQLite3 (default), PostgreSQL (optional)
Language	Python 3.12+
Documentation	Swagger / ReDoc
📂 Project Structure
companyapi/
│
├── .venv/                  # Python virtual environment
├── .vscode/                # VS Code settings
│
├── apps/                   # Django apps
│   ├── company_api/        # Company management app
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   └── employees_api/      # Employee management app
│       ├── migrations/
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── urls.py
│       └── views.py
│
├── core/                   # Core project configuration
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

⚙️ Installation & Setup
1️⃣ Clone the repository:
git clone https://github.com/yourusername/companyapi.git
cd companyapi

2️⃣ Create & activate a virtual environment:
python -m venv .venv
source .venv/bin/activate     # For Linux/Mac
.venv\Scripts\activate        # For Windows

3️⃣ Install dependencies:
pip install -r requirements.txt

4️⃣ Run migrations:
python manage.py migrate

5️⃣ Start the development server:
python manage.py runserver

📖 API Documentation

Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc: http://127.0.0.1:8000/redoc/

👤 Author

Muhammad Nouman
🧠 Backend Developer (Python | Django | DRF)
🌐 GitHub
 | LinkedIn
 | Portfolio
