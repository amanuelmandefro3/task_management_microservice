# Task Management Microservices

## Overview

The **Task Management Microservices** project is a scalable and secure application built using Django and Django REST Framework (DRF). It consists of three primary services:

1. **User Service**: Manages user registration, OTP verification, and JWT token issuance.
2. **Task Service**: Handles task creation, assignment, and management.
3. **Notification Service**: (Optional) Sends notifications based on events.

All services communicate through RabbitMQ and use PostgreSQL for data storage. Docker Compose orchestrates the containerized services for easy deployment.

## Architecture

![Architecture Diagram](architecture-diagram.png)

- **User Service**: Centralized authentication issuing JWT tokens.
- **Task Service**: Task operations secured with JWT.
- **Notification Service**: Listens to events and sends notifications.
- **RabbitMQ**: Facilitates inter-service communication.
- **PostgreSQL**: Dedicated databases for each service.
- **Docker Compose**: Manages service containers.

## Technologies

- **Backend**: Django, Django REST Framework, drf-simplejwt, drf-yasg
- **Messaging**: RabbitMQ
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/downloads)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/task-management-microservices.git
   cd task-management-microservices
   ```

2. **Configure Environment Variables**

   Ensure the `SECRET_KEY` and other necessary environment variables are set in the `docker-compose.yml` file.

3. **Build and Start Services**

   ```bash
   docker-compose up --build
   ```

## Services

### 1. User Service

- **URL**: `http://localhost:8001/`
- **Endpoints**:
  - `POST /api/users/register/`: Register a new user.
  - `POST /api/users/verify_otp/`: Verify OTP.
  - `POST /api/users/resend_otp/`: Resend OTP.
  - `GET /api/users/profile/`: Get user profile.
  - `GET /api/users/list_users/`: List all users (protected).

### 2. Task Service

- **URL**: `http://localhost:8002/`
- **Endpoints**:
  - `GET /api/tasks/`: List all tasks.
  - `POST /api/tasks/`: Create a new task.
  - `POST /api/tasks/{id}/assign/`: Assign a task to a user.

### 3. Notification Service (Optional)

- **URL**: `http://localhost:8003/`
- **Endpoints**:
  - `GET /api/logs/`: Retrieve notification logs (protected).

## API Documentation

Each service provides Swagger UI for interactive API exploration.

- **User Service**: `http://localhost:8001/swagger/`
- **Task Service**: `http://localhost:8002/swagger/`
- **Notification Service**: `http://localhost:8003/swagger/`

### Authentication

1. **Register and Verify User** via User Service.
2. **Obtain JWT Token** from `POST /api/token/`.
3. **Authorize in Swagger** using the obtained Bearer token.

## Usage

### 1. Register a User

```bash
curl -X POST http://localhost:8001/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"amr","email":"amr@example.com","password":"password123"}'
```

### 2. Verify OTP

```bash
curl -X POST http://localhost:8001/api/users/verify_otp/ \
  -H "Content-Type: application/json" \
  -d '{"email":"amr@example.com","otp_code":"123456"}'
```

### 3. Obtain JWT Token

```bash
curl -X POST http://localhost:8001/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"amr","password":"password123"}'
```

### 4. Access Task Service Endpoints

Use the obtained JWT token in the `Authorization` header as `Bearer <token>`.

#### List All Tasks

```bash
curl -X GET http://localhost:8002/api/tasks/ \
  -H "Authorization: Bearer <access_token>"
```

#### Assign a Task

```bash
curl -X POST http://localhost:8002/api/tasks/1/assign/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"user_id":2}'
```

## Troubleshooting

- **401 Unauthorized on Task Service Swagger**:
  - Ensure Swagger URLs are publicly accessible by setting `permission_classes` to `AllowAny` in `urls.py`.
  - Verify all services share the same `SECRET_KEY`.
  - Check JWT token validity and claims.

- **Service Communication Issues**:
  - Ensure RabbitMQ is running and accessible.
  - Verify Docker containers are up and properly networked.

- **Token Issues**:
  - Ensure tokens include necessary claims (`user_id`, `username`, `email`).
  - Refresh tokens if expired.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
