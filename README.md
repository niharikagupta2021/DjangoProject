# Django Login System

## Description

This Django project implements a robust login system with features for user signup, login, and profile management. It includes functionalities such as user registration, user data retrieval, updating user details, and deleting user accounts. The project utilizes Django’s built-in features for model creation, views implementation, URL routing, and template rendering to achieve seamless user interaction and data management.

Additionally, the project has been thoroughly tested using Postman to ensure the reliability and functionality of all CRUD (Create, Read, Update, Delete) operations.

## Features

- User signup with unique email validation  
- User login with email and password authentication  
- Profile management with ability to view, update, and delete user information  
- CRUD operations accessible via Django views and testable through Postman API requests  
- Admin interface for managing users (superuser setup included)  

## Project Structure

- **Django Project Name:** `LoginSystem`  
- **Django App Name:** `Loginify`  
- Virtual environment used: `DjangoAssignment`  

## Setup Instructions

### 1. Create and activate virtual environment

```bash
python -m venv DjangoAssignment
# Windows
DjangoAssignment\Scripts\activate
# macOS/Linux
source DjangoAssignment/bin/activate

steps:
1. pip install django

2. django-admin startproject LoginSystem
cd LoginSystem
python manage.py startapp Loginify

3. Create the Django project and app
bash
Copy
Edit
django-admin startproject LoginSystem
cd LoginSystem
python manage.py startapp Loginify

4. Run migrations and create superuser
bash
Copy
Edit
python manage.py migrate
python manage.py createsuperuser

5.Run the development server
python manage.py runserver

CRUD Operations Endpoints
Operation	HTTP Method	Endpoint	Description
Get all users	GET	/users/	Retrieve details of all users
Get user by email	GET	/user/<email>/	Retrieve user details by email
Update user details	PUT	/user/update/<email>/	Update user details by email
Delete user	DELETE	/user/delete/<email>/	Delete user by email

Use Postman to test these API endpoints.

Additional Notes
Passwords are stored as plain text in this project for simplicity. In production, always hash passwords securely.

The project uses Django’s ORM for database management and supports SQLite by default.

Basic HTML templates are used for signup, login, and success pages.

References:
Django Documentation
Postman API Testing Tool
