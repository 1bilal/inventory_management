# Inventory Management System

An inventory management system built with Django (backend) and React (frontend). This system provides basic CRUD operations for managing products, suppliers, and categories, with JWT-based authentication for secure access.

## Features

- **Inventory Tracking**: Manage product details, stock levels, suppliers, and categories.
- **JWT Authentication**: Secure login system using JSON Web Tokens for session management.
- **Admin Control**: Manage user access and data through Django's admin interface.
- **RESTful API**: Exposes a REST API for frontend interaction.
- **React Frontend**: User-friendly interface for managing inventory data.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [API Endpoints](#api-endpoints)
- [Admin Interface](#admin-interface)
- [Project Structure](#project-structure)

## Requirements

- Python 3.7+
- Node.js 14+
- Django 3.x or 4.x
- React 17+

## Installation

Clone the repository and follow the steps below to set up the project:

```bash
git clone https://github.com/username/inventory-management-system.git
cd inventory-management-system
```

### Backend Setup

1. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. **Install Backend Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**:

   ```bash
   python manage.py migrate
   ```

4. **Create a Superuser**:

   ```bash
   python manage.py createsuperuser
   ```

5. **Start the Backend Server**:

   ```bash
   python manage.py runserver
   ```


### Frontend Setup

1. **Navigate to the Frontend Directory**:

   ```bash
   cd inventory-frontend
   ```

2. **Install Frontend Dependencies**:

   ```bash
   npm install
   ```

3. **Start the Frontend Server**:

   ```bash
   npm start
   ```

The frontend should now be accessible at `http://localhost:3000` and the backend API at `http://localhost:8000`.


### Usage

After setting up both the backend and frontend, you can start using the application. For managing users and accessing secure endpoints, use the admin interface and JWT-based login.

#### JWT Authentication

- Obtain tokens by logging in via the `/api/login/` endpoint.
- Include the `access` token in the `Authorization` header as `Bearer <access_token>` for secure endpoints.

#### API Endpoints

| Endpoint                  | Method | Description                       |
|---------------------------|--------|-----------------------------------|
| `/api/login/`             | POST   | Login to obtain JWT tokens        |
| `/api/products/`          | GET    | Retrieve a list of products       |
| `/api/products/<id>/`     | GET    | Retrieve, update or delete a product |
| `/api/categories/`        | GET    | Retrieve a list of categories     |
| `/api/suppliers/`         | GET    | Retrieve a list of suppliers      |

#### Admin Interface

Access the Django admin interface at `http://localhost:8000/admin`. Use the superuser credentials created earlier to log in and manage products, categories, suppliers, and users.


### Project Structure

```
inventory-management-system/
├── backend/                  # Django backend
│   ├── inventory/            # Main inventory app
│   ├── settings.py           # Django settings
│   └── urls.py               # URL routing
├── inventory-frontend/       # React frontend
│   ├── src/
│   │   ├── components/       # Reusable components
│   │   ├── pages/            # Main pages (Login, Dashboard)
│   ├── App.js                # Main React app
│   └── package.json          # Frontend dependencies
├── README.md                 # Project documentation
└── requirements.txt          # Backend dependencies
```

### License

This project is licensed under the MIT License.
