#!/bin/bash

# Script to fix Docker permissions and create a PostgreSQL Docker container for a Django project.

# Configuration Variables
CONTAINER_NAME="django-postgres"
POSTGRES_USER="myuser"
POSTGRES_PASSWORD="mypassword"
POSTGRES_DB="mydatabase"
POSTGRES_PORT=5432
HOST_PORT=5432

# Step 1: Check if Docker is installed
echo "Checking if Docker is installed..."
if ! [ -x "$(command -v docker)" ]; then
    echo "Docker is not installed. Installing Docker..."
    sudo apt update && sudo apt install -y docker.io || {
        echo "Error: Failed to install Docker."
        exit 1
    }
    echo "Docker installed successfully."
    echo "Starting Docker service..."
    sudo systemctl start docker
    sudo systemctl enable docker
else
    echo "Docker is already installed."
fi

# Step 2: Fix Docker Permissions
echo "Checking Docker permissions for the current user..."
CURRENT_USER=$(whoami)
if groups "$CURRENT_USER" | grep &>/dev/null '\bdocker\b'; then
    echo "User $CURRENT_USER already has Docker permissions."
else
    echo "Adding user $CURRENT_USER to the docker group..."
    sudo usermod -aG docker "$CURRENT_USER" || {
        echo "Error: Failed to add user to the docker group."
        exit 1
    }
    echo "User $CURRENT_USER has been added to the docker group."
    echo "You need to log out and log back in for the changes to take effect."
    echo "Attempting to apply changes for this session..."
    newgrp docker || {
        echo "Error: Failed to apply group changes immediately. Please log out and log back in."
        exit 1
    }
fi

# Step 3: Test Docker Access
echo "Testing Docker access..."
if ! docker ps &>/dev/null; then
    echo "Error: Docker is still not accessible. Please ensure Docker permissions are set correctly."
    exit 1
fi
echo "Docker is accessible. Proceeding with PostgreSQL setup."

# Step 4: Create PostgreSQL Container
echo "Creating PostgreSQL container..."
if docker ps -aq -f name=$CONTAINER_NAME; then
    echo "A container with the name $CONTAINER_NAME already exists. Removing it..."
    docker stop $CONTAINER_NAME && docker rm $CONTAINER_NAME || {
        echo "Error: Failed to remove the existing container."
        exit 1
    }
fi

docker run -d \
    --name $CONTAINER_NAME \
    -e POSTGRES_USER=$POSTGRES_USER \
    -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
    -e POSTGRES_DB=$POSTGRES_DB \
    -p $HOST_PORT:$POSTGRES_PORT \
    postgres || {
        echo "Error: Failed to create the PostgreSQL container."
        exit 1
    }

# Step 5: Verify PostgreSQL Container
if docker ps -q -f name=$CONTAINER_NAME; then
    echo "PostgreSQL container $CONTAINER_NAME is running successfully."
else
    echo "Error: PostgreSQL container failed to start."
    exit 1
fi

# Step 6: Display Connection Details
echo "PostgreSQL is ready. Use the following details to connect:"
echo "---------------------------------------"
echo "Host: localhost"
echo "Port: $HOST_PORT"
echo "Database: $POSTGRES_DB"
echo "Username: $POSTGRES_USER"
echo "Password: $POSTGRES_PASSWORD"
echo "---------------------------------------"

echo "Setup complete!"
