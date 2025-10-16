# Use official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV VENV_PATH /app/.venv

# Set work directory
WORKDIR /app

# Copy necessary files
COPY requirements.txt apt-requirements.txt ./

# Install system dependencies
RUN apt-get update && \
    xargs -a apt-requirements.txt apt-get install -y && \
    rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
RUN python -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project files
COPY . /app

# Ensure scripts are executable
RUN chmod +x scripts/run_all_tests.sh

# Define entrypoint to run tests
ENTRYPOINT ["bash", "scripts/run_all_tests.sh"]
