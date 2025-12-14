# Social Media API

A Django REST Framework–based Social Media API with token authentication and custom user profiles.

## Features
- Custom user model
- Token-based authentication
- User registration & login
- User profile management
- Followers system (Many-to-Many)

## Setup
```bash
pip install django djangorestframework djangorestframework-authtoken pillow
python manage.py migrate
python manage.py runserver
