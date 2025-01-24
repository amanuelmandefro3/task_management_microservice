# Abeni

services:
  # User Service
  user-service:
    build: ./user_service
    container_name: user_service
    command: sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    volumes:
      - ./user_service:/app
    ports:
      - "8001:8000"
    environment:
      DATABASE_NAME: user_db
      DATABASE_USER: postgres
      DATABASE_PASSWORD: 12345678
      DATABASE_HOST: postgres-user
      DATABASE_PORT: 5432
      RABBITMQ_HOST: rabbitmq
      RABBITMQ_PORT: 5672
      EMAIL_BACKEND: "django.core.mail.backends.smtp.EmailBackend"
      EMAIL_HOST: "smtp.gmail.com"
      EMAIL_HOST_USER: "amanuelmandefrow@gmail.com"
      EMAIL_HOST_PASSWORD: "nrhcholmnxdhjocc"
      EMAIL_PORT: "2525"
      EMAIL_USE_TLS: "True"
      DEFAULT_FROM_EMAIL: "amanuelmandefrow@gmail.com"
      SECRET_KEY: "mysharedsecretkey123" 
    depends_on:
      - rabbitmq
      - postgres-user

  # Task Service
  task-service:
    build: ./task_service
    container_name: task_service
    command: sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    volumes:
      - ./task_service:/app
    ports:
      - "8002:8000"
    environment:
      DATABASE_NAME: task_db
      DATABASE_USER: postgres
      DATABASE_PASSWORD: 12345678
      DATABASE_HOST: postgres-task
      DATABASE_PORT: 5432
      RABBITMQ_HOST: rabbitmq
      RABBITMQ_PORT: 5672
      SECRET_KEY: "mysharedsecretkey123"
    depends_on:
      - rabbitmq
      - postgres-task

  # Notification Service
  notification-service:
    build: ./notification_service
    container_name: notification_service
    command: sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    volumes:
      - ./notification_service:/app
    ports:
      - "8003:8000"
    environment:
      DATABASE_NAME: notification_db
      DATABASE_USER: postgres
      DATABASE_PASSWORD: 12345678
      DATABASE_HOST: postgres-notification
      DATABASE_PORT: 5432
      RABBITMQ_HOST: rabbitmq
      RABBITMQ_PORT: 5672
    depends_on:
      - rabbitmq
      - postgres-notification

  # RabbitMQ
  rabbitmq:
    image: "rabbitmq:3-management"
    ports:
      - "5672:5672"
      - "15672:15672"

  # PostgreSQL for User Service
  postgres-user:
    image: postgres:13
    environment:
      POSTGRES_DB: user_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: 12345678
    ports:
      - "5435:5432"

  # PostgreSQL for Task Service
  postgres-task:
    image: postgres:13
    environment:
      POSTGRES_DB: task_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: 12345678
    ports:
      - "5436:5432"

  # PostgreSQL for Notification Service
  postgres-notification:
    image: postgres:13
    environment:
      POSTGRES_DB: notification_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: 12345678
    ports:
      - "5437:5432"
