# 🏢 Company API

A **Django REST Framework (DRF)** based RESTful API to manage **companies, employees, and organizational data**.
This project demonstrates clean API design, CRUD operations, and relational data handling using Django.

---

## 📌 Project Overview

The **Company API** allows you to:

* Create and manage companies
* Add, update, and remove employees under companies
* Access data through RESTful endpoints
* Explore APIs using Swagger & ReDoc documentation

This project is ideal for:

* Learning Django REST Framework
* Understanding relational models in APIs
* Practicing real-world backend development

---

## 🚀 Features

*  Company Management (CRUD)
*  Employee Management (CRUD)
*  Relational Data (Company ↔ Employees)
*  Django Admin Panel
*  RESTful API Design
*  Swagger & ReDoc API Documentation
*  SQLite3 Database (easy to switch to PostgreSQL)

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Language:** Python 3.12+
* **Database:** SQLite3 (default)
* **API Docs:** Swagger / ReDoc
* **Tools:** Git, Virtual Environment

---

## 📂 Project Structure

```text
company_api/
│── company_api/        # Main project settings
│── companies/          # Company app
│── employees/          # Employee app
│── manage.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1 Clone the Repository

```bash
git clone https://github.com/MuhammadNouman769/company_api.git
cd company_api
```

### 2 Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3 Install Dependencies

```bash
pip install -r requirements.txt
```

### 4 Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5 Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6 Run Development Server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## 🔑 Admin Panel

Access Django Admin Panel:

```
http://127.0.0.1:8000/admin/
```

Use the superuser credentials created earlier.

---

## 📘 API Documentation

Swagger and ReDoc are enabled for easy API testing.

* **Swagger UI:**

  ```
  http://127.0.0.1:8000/swagger/
  ```

* **ReDoc:**

  ```
  http://127.0.0.1:8000/redoc/
  ```

---

## 🔌 API Endpoints (Example)

### Companies

* `GET /api/companies/` → List all companies
* `POST /api/companies/` → Create a new company
* `GET /api/companies/{id}/` → Retrieve company details
* `PUT /api/companies/{id}/` → Update company
* `DELETE /api/companies/{id}/` → Delete company

### Employees

* `GET /api/employees/` → List all employees
* `POST /api/employees/` → Create a new employee
* `GET /api/employees/{id}/` → Retrieve employee details
* `PUT /api/employees/{id}/` → Update employee
* `DELETE /api/employees/{id}/` → Delete employee

---

## 🧪 Testing APIs

You can test APIs using:

* Swagger UI
* Postman
* cURL

Example using cURL:

```bash
curl http://127.0.0.1:8000/api/companies/
```

---

## 🔄 Database Configuration

Default database is **SQLite3**.

To switch to PostgreSQL, update `DATABASES` in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'company_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Muhammad Nouman**
GitHub: [https://github.com/MuhammadNouman769](https://github.com/MuhammadNouman769)

---

⭐ If you like this project, don’t forget to **star the repository**!
