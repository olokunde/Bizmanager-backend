# Bizmanager Backend

Bizmanager Backend is a Django-based backend application designed to manage users, products, orders, and administrative operations.  
This project is being built as a hands-on backend development project, focusing on writing clean, scalable, and practical Django code.

---

## Project Overview

The goal of this project is to simulate a real-world business management backend system.  
It includes structured apps, database models, admin configurations, and is being expanded gradually to include APIs, authentication, and role-based access control.

This repository reflects **real learning through building**, not just tutorials.

---

## Current Features

- Custom Django project structure
- Modular apps:
  - **Users** – user management logic
  - **Products** – product creation and management
  - **Orders** – order handling and status tracking
  - **Reports** – placeholder for reporting logic
- Django Admin customization:
  - Product management
  - Order status filtering
  - User administration
- Database integration (SQLite for development)
- Clean project structure following Django best practices

---

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (development)
- **Admin Interface:** Django Admin
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

backend/
├── config/ # Project settings and URLs
├── users/ # User management app
├── products/ # Product management app
├── orders/ # Order management app
├── reports/ # Reports (work in progress)
├── manage.py
└── db.sqlite3

---

## Setup Instructions (Local)

1. Clone the repository:
   ```bash
   git clone https://github.com/olokunde/Bizmanager-backend.git


2. Navigate into the project:

   cd Bizmanager-backend/backend


3. Create and activate virtual environment:

   python -m venv venv
   venv\Scripts\activate


4. Install dependencies:

   pip install django


5. Run migrations:

   python manage.py migrate


6. Start the development server:

   python manage.py runserver


7. Access Django Admin:

   http://127.0.0.1:8000/admin/

---

## Roadmap (What I’m Building Next)

-  Django REST Framework (DRF) APIs

-  JWT authentication

-  User registration and login endpoints

-  Role-based permissions (Admin vs User)

-  Order lifecycle APIs

-  API documentation (Swagger)

-  Deployment (Render / Railway)

---

## Screenshots

Screenshots will be added as features are completed (Admin dashboard, API testing, and documentation views).

---

## Author
Olaoluwa Olokunde
Backend Developer (Python & Django)
GitHub: https://github.com/olokunde
