# 🚗 Car Rental Portal

Modern full-stack web application for a car rental company.

The project is an information system designed to automate car rental processes, including vehicle management, customer
bookings, authentication, and administration.

The application is developed using modern software engineering approaches with a focus on scalability, maintainability,
clean architecture, testing, and deployment.

---

## 🛠 Tech Stack

### Backend

![Python](https://img.shields.io/badge/Python-3.12.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/Django_REST_Framework-API-ff1709?style=for-the-badge&logo=django&logoColor=white)

---

### Frontend

![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/React-18%2B-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-Latest-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.x-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)

---

### Database

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-Latest-DC382D?style=for-the-badge&logo=redis&logoColor=white)

---

### DevOps

![Docker](https://img.shields.io/badge/Docker-Latest-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

---

### Testing & Quality

![Pytest](https://img.shields.io/badge/Pytest-9.1.1-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Black](https://img.shields.io/badge/Black-26.5.1-black?style=for-the-badge)
![Ruff](https://img.shields.io/badge/Ruff-0.16.0-D7FF64?style=for-the-badge&logo=ruff&logoColor=black)

![isort](https://img.shields.io/badge/isort-8.0.1-ef8336?style=for-the-badge)
![mypy](https://img.shields.io/badge/mypy-2.3.0-2A6DB0?style=for-the-badge)
![Pyright](https://img.shields.io/badge/Pyright-1.1.411-1679A7?style=for-the-badge)




---

# 📌 Project Overview

## Purpose

The main goal of the project is to create a complete online car rental platform that allows customers to search, view,
and reserve vehicles, while administrators can manage the entire rental workflow.

The system combines:

- modern frontend development;
- scalable backend architecture;
- relational database design;
- REST API communication;
- authentication and authorization;
- automated testing;
- containerization and deployment.

---

# ✨ Main Features

## Customer Features

- User registration and authentication
- User profile management
- Browse available vehicles
- Search and filtering system
- Detailed car information page
- Booking creation
- Booking history
- Reviews and ratings
- Responsive interface
- Dark / Light theme
- Multilingual interface

Supported languages:

- English
- Ukrainian
- Russian

---

## Administrator Features

- User management
- Vehicle management
- Add / update / delete cars
- Manage rental bookings
- Change booking statuses
- Monitor system information

---

# 🏗️ System Architecture

The application follows a layered architecture approach.

General architecture:

```

React Frontend
|
|
REST API
|
|
Django Backend
|
|
Django ORM
|
|
PostgreSQL Database

```

---

# 🛠 Technology Stack

## Backend

- Python 3.12
- Django
- Django REST Framework
- Django ORM
- PostgreSQL
- JWT Authentication
- Redis
- Celery (planned)

---

## Frontend

- TypeScript
- React
- Vite
- React Router
- Tailwind CSS
- React Hook Form
- Zod
- Zustand / Redux Toolkit

---

## Database

Primary database:

- PostgreSQL

ORM:

- Django ORM

Database concepts:

- relational data modeling
- normalization
- migrations
- indexing
- transactions
- query optimization

---

## DevOps

- Linux Ubuntu
- Docker
- Docker Compose
- Nginx
- GitHub Actions
- CI/CD
- Environment configuration

---

## Testing

Backend:

- Pytest
- Django Testing Framework
- Unit Testing
- Integration Testing
- API Testing

Frontend:

- Component Testing
- UI Testing

---

# 📂 Project Structure

```

car-rental-portal/

│
├── backend/
│   └── Django backend application
│
├── frontend/
│   └── React TypeScript application
│
├── docs/
│   └── Project documentation
│
├── docker/
│   └── Docker configuration
│
├── postman/
│   └── API collections
│
├── .github/
│   └── GitHub Actions workflows
│
├── docker-compose.yml
│
├── .env.example
│
├── pyproject.toml
│
├── README.md
│
└── LICENSE

```

---

# ⚙️ Backend Structure

```

backend/

├── apps/
│
├── config/
│
├── api/
│
├── services/
│
├── permissions/
│
├── tests/
│
└── manage.py

```

Responsibilities:

### Models

Database entities and relationships.

### API Layer

Handles HTTP requests and responses.

### Services

Contains business logic.

### Permissions

Authentication and authorization rules.

### Tests

Ensures system reliability.

---

# ⚛️ Frontend Structure

```

frontend/

├── src/
│
├── components/
│
├── pages/
│
├── hooks/
│
├── services/
│
├── store/
│
├── types/
│
└── utils/

````

Principles:

- reusable components;
- clean UI architecture;
- separation of logic and presentation;
- responsive design.

---

# 🚀 Installation and Setup

## Requirements

Before installation:

- Python 3.12+
- Node.js
- PostgreSQL
- Docker (recommended)
- Git

---

# Backend Setup

Go to backend folder:

```bash
cd backend
````

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment.

Windows:

```bash
.venv\Scripts\activate
```

Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create environment file:

```bash
.env
```

Run migrations:

```bash
python manage.py migrate
```

Start backend:

```bash
python manage.py runserver
```

Backend will run:

```
http://localhost:8000
```

---

# Frontend Setup

Go to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start application:

```bash
npm run dev
```

Frontend will run:

```
http://localhost:5173
```

---

# 🐳 Docker Setup

Build and start containers:

```bash
docker compose up --build
```

Docker services:

```
Backend
Frontend
PostgreSQL
Redis
Nginx
```

---

# 🔐 Environment Variables

Example configuration:

```
.env.example
```

Contains:

* Django secret key
* Database configuration
* JWT settings
* Redis configuration
* Frontend API URL

Sensitive information is stored only inside `.env`.

---

# 🧪 Code Quality Tools

The project uses:

## Black

Automatic Python formatting.

## Ruff

Code quality checking and linting.

## isort

Import sorting.

## mypy

Static type checking.

## Pyright

Additional type analysis.

Configuration:

```
pyproject.toml
```

---

# 🌿 Git Workflow

The project follows Git Flow principles.

Branches:

```
main
 |
develop
 |
feature/*
```

## main

Stable production-ready version.

## develop

Main development branch.

## feature

Temporary branches for individual tasks.

Examples:

```
feature/project-setup

feature/authentication

feature/car-management

feature/frontend-ui
```

---

# 📖 API Documentation

The backend provides API documentation using:

* OpenAPI
* Swagger UI

Available after backend launch:

```
http://localhost:8000/api/docs/
```

---

# 🎨 Design Concept

The application uses a modern minimal design.

Main principles:

* dark theme by default;
* optional light theme;
* smooth animations;
* responsive layout;
* clean interface;
* accessibility.

Color palette:

* dark gray;
* white;
* muted olive green accent colors.

---

# 📈 Future Improvements

Possible future features:

* Online payment integration
* Mobile application
* Advanced analytics
* AI-based recommendations
* Cloud deployment
* Microservice architecture
* Monitoring system

---

# 👩‍💻 Author

Software Engineering Student

This project is developed as:

* university qualification project;
* portfolio project;
* example of full-stack application development.

