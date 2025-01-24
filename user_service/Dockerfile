# Abeni
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Start the consumer in the background, then runserver
CMD ["sh", "-c", "python manage.py migrate && (python manage.py start_consumer &) && python manage.py runserver 0.0.0.0:8000"]
