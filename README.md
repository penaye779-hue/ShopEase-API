ShopEase API
Overview

ShopEase API is a backend service for managing products, categories, and users in an e-commerce platform. It provides secure endpoints for user registration, authentication, and CRUD operations for products and categories.

This project is built as part of the BE Capstone Part 5 for the 2026 program.

Features

User registration and JWT authentication

Create, list, update, and delete products

Create, list, update, and delete categories

RESTful API endpoints

PostgreSQL database support

Fully deployed on Render

Tech Stack

Python 3.14

Django 6.0.1

Django REST Framework 3.16

PostgreSQL

Render for deployment

Installation

Clone the repository:

git clone https://github.com/penaye779-hue/ShopEase-API.git
cd ShopEase-API

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

Install dependencies:

pip install -r requirements.txt

Configure environment variables in a .env file:

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_postgresql_url

Run migrations:

python manage.py migrate

Start the server locally:

python manage.py runserver
API Endpoints

Home: /

{ "status": "ShopEase API is running", "version": "1.0" }

User Registration: POST /api/users/register/

JWT Token: POST /api/token/

JWT Refresh: POST /api/token/refresh/

Products: /api/products/

Categories: /api/categories/

All POST/PUT requests require authentication via JWT access token.

Testing API

Use Postman, Insomnia, or curl to test endpoints. Example:

curl -X GET https://shopease-api-rkb1.onrender.com/api/products/ \
  -H "Authorization: Bearer <your_access_token>"
Deployment

Deployed live at: https://shopease-api-rkb1.onrender.com

Hosted on Render with PostgreSQL database.

Notes

Admin interface available at /admin/

Default admin credentials can be set via Django createsuperuser command.

All migrations and database changes are tracked and maintained.