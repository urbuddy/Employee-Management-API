# Employee Management API

## Overview
The Employee Management API is a RESTful service built with Django REST Framework to manage employee data in a company. This API allows you to create, retrieve, update, and delete employee records while following RESTful principles. The API also includes JWT-based authentication to secure endpoints, ensuring only authenticated users have access to employee data.

## Features
CRUD Operations: Create, read, update, and delete employee records.
Token-Based Authentication: Secures endpoints with JWT authentication.
Filtering: Filter employees by department or role.
Pagination: Limits results per page to 10 employees with pagination support.
Validation: Ensures unique and valid email addresses and required fields.
Error Handling: Provides meaningful HTTP status codes and messages.

# Requirements
Python 3.7+
Django 4.0+
Django REST Framework 3.13+
djangorestframework-simplejwt for JWT authentication
Installation
Clone the repository:

```bash
  git clone https://github.com/your-username/employee-management-api.git
  cd employee-management-api
```

Create a virtual environment:
```bash
  python3 -m venv venv
  source venv/bin/activate
```

Install dependencies:
```bash
  pip install -r requirements.txt
```

Apply migrations:
```bash
python manage.py migrate
```

Create a superuser (for accessing the Django Admin and generating JWT tokens):
```bash
python manage.py createsuperuser
```

Start the development server:
```bash
python manage.py runserver
```

## API Endpoints
### Authentication
Get JWT Token: POST /api/token/
Request:
json
```bash
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

Response:
json
```bash
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

Employee Endpoints
Note: All employee endpoints require JWT authentication with the Authorization header:

makefile
Copy code
Authorization: Bearer <your_access_token>
Create an Employee: POST /api/employees/

Request:
json
```bash
{
  "name": "John Doe",
  "email": "john@example.com",
  "department": "Engineering",
  "role": "Developer"
}
```
Response: 201 Created
List All Employees: GET /api/employees/

Supports filtering by department and role and pagination with page parameter.
Response: 200 OK
Retrieve a Single Employee: GET /api/employees/{id}/

Response: 200 OK or 404 Not Found if the employee does not exist.
Update an Employee:

Full Update (PUT): PUT /api/employees/{id}/
Partial Update (PATCH): PATCH /api/employees/{id}/
Response: 200 OK or 404 Not Found if the employee does not exist.
Delete an Employee: DELETE /api/employees/{id}/

Response: 204 No Content or 404 Not Found if the employee does not exist.
Running Tests
To run tests, use the following command:

```bash
python manage.py test
```

Example Usage with cURL
Get JWT Token:

```bash
curl -X POST http://localhost:8000/api/token/ -d '{"username": "yourusername", "password": "yourpassword"}' -H "Content-Type: application/json"
```

Create an Employee:

```bash
curl -X POST http://localhost:8000/api/employees/ -d '{"name": "Jane Doe", "email": "jane@example.com", "department": "HR", "role": "Manager"}' -H "Authorization: Bearer <your_access_token>" -H "Content-Type: application/json"
```

List All Employees:

```bash
curl -X GET "http://localhost:8000/api/employees/?department=HR" -H "Authorization: Bearer <your_access_token>"
```

## Project Structure
```bash
├── employees/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py           # Employee model definition
│   ├── serializers.py      # Employee serializer with validation
│   ├── urls.py             # URL routing for employee API
│   ├── views.py            # Employee views (CRUD operations)
│   └── tests.py            # Unit tests for the API
├── company_api/
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Root URL configuration
│   └── wsgi.py
├── manage.py
└── requirements.txt
```
