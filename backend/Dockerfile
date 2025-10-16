# syntax=docker/dockerfile:1.5
# Base Python image
FROM python:3.12-slim
# why below line? https://pythonspeed.com/articles/base-image-python-docker-images/
# Install dependencies for apt-requirements (if needed)
COPY apt-requirements.txt /tmp/apt-requirements.txt
RUN apt-get update && \
    xargs -a /tmp/apt-requirements.txt apt-get install -y && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy Python dependencies
COPY requirements.txt /app/requirements.txt
# why --no-cache-dir? https://pythonspeed.com/articles/docker-cache-pip-downloads/
#
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code into the container
COPY . /app

# Expose Gunicorn port
EXPOSE 8000

# Run Gunicorn as the application server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
