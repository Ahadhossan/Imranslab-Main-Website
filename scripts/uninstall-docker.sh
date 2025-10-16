#!/bin/bash

echo "Starting Docker uninstallation process..."

# Stop Docker services
echo "Stopping Docker services..."
sudo systemctl stop docker
sudo systemctl stop docker.socket

# Uninstall Docker packages
echo "Removing Docker packages..."
sudo apt-get purge -y docker-engine docker docker.io containerd runc

# Remove Docker directories
echo "Removing Docker directories..."
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd

# Remove Docker-related configuration files
echo "Removing Docker configuration files..."
sudo rm -rf /etc/docker
sudo rm -rf /etc/systemd/system/docker.service
sudo rm -rf /etc/systemd/system/docker.socket
sudo rm -rf /usr/lib/systemd/system/docker.service
sudo rm -rf /usr/lib/systemd/system/docker.socket

# Clean up dependencies
echo "Cleaning up dependencies..."
sudo apt-get autoremove -y
sudo apt-get autoclean

# Verify Docker is uninstalled
echo "Verifying Docker removal..."
if ! command -v docker &> /dev/null; then
    echo "Docker has been successfully uninstalled."
else
    echo "Docker uninstallation failed. Please check manually."
fi
