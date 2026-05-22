# Django Serialization Project

This project is a Django-based API with DRF (Django Rest Framework) and drf-spectacular for OpenAPI schema and documentation.

## Features
- Django 5.2+
- Django Rest Framework (DRF)
- OpenAPI/Swagger docs via drf-spectacular
- Example app: `apps.api`

## Quick Start

1. **Clone the repository**
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
7. **Access the API docs:**
   - Swagger UI: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
   - Redoc: [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Project Structure
```
manage.py
requirements.txt
apps/
    api/
        models.py
        serializers.py
        views.py
        ...
core/
    settings.py
    urls.py
    ...
```



## Repository
Project repository: [https://github.com/MuhammadNouman769/serializers-learningg](https://github.com/MuhammadNouman769/serializers-learningg)

## How to Clone
Clone this repository to your system using:

```bash
git clone https://github.com/MuhammadNouman769/serializers-learningg.git
```

## License
This project is for educational/demo purposes.
