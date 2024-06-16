# Use an official Python runtime as a parent image
FROM python:3.10 as backend-builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory for the backend
WORKDIR /app/backend

# Install system dependencies for backend
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev

# Copy the backend requirements file and install Python dependencies
COPY Backend/requirements.txt /app/backend/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the backend source code
COPY Backend/ /app/backend/

# ---------------------
# Frontend Build Stage
# ---------------------
FROM node:14 as frontend-builder

# Set the working directory for the frontend
WORKDIR /app/frontend

# Copy frontend files and install dependencies
COPY Frontend/package.json Frontend/package-lock.json /app/frontend/
RUN npm install

# Copy the frontend source code
COPY Frontend/ /app/frontend/

# Build the frontend
RUN npm run build

# ---------------------
# Final Stage
# ---------------------
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Collect static files
RUN python /app/backend/manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
