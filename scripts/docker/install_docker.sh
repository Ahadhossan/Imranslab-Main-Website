#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" &> /dev/null
}

# Check if Docker is already installed
if command_exists docker; then
    echo "Docker is already installed. Exiting installation script."
    docker --version
    exit 0
fi

# Update system packages
echo "Updating system packages..."
sudo apt-get update -y

# Install prerequisites
echo "Installing prerequisites..."
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common \
    gnupg

# Add Docker's official GPG key
if [ ! -f /usr/share/keyrings/docker-archive-keyring.gpg ]; then
    echo "Adding Docker's official GPG key..."
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
fi

# Set up the stable repository
if [ ! -f /etc/apt/sources.list.d/docker.list ]; then
    echo "Setting up the Docker repository..."
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
fi

# Update package index
echo "Updating package index with Docker packages..."
sudo apt-get update -y

# Install Docker Engine
echo "Installing Docker Engine..."
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Verify Docker installation
if command_exists docker; then
    echo "Docker has been successfully installed."
    docker --version
else
    echo "Docker installation failed. Please check the script output for errors."
    exit 1
fi

# Add user to the Docker group to avoid using 'sudo' for Docker commands
echo "Adding the current user to the Docker group..."
sudo usermod -aG docker "$USER"
echo "You need to log out and log back in for the group changes to take effect."

# Start and enable Docker service
echo "Starting and enabling Docker service..."
sudo systemctl start docker
sudo systemctl enable docker

# Verify Docker is running
#echo "Verifying Docker is running..."
#sudo systemctl status docker | grep Active
if ! sudo systemctl is-active --quiet docker; then
    echo "Error: Docker service is not running. Check logs with 'sudo journalctl -u docker --no-pager'."
    exit 1
fi
