#!/bin/bash

# Script to fix Docker permissions by adding the current user to the docker group

echo "Checking if Docker is installed..."
if ! [ -x "$(command -v docker)" ]; then
    echo "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if the current user is part of the docker group
CURRENT_USER=$(whoami)
if groups "$CURRENT_USER" | grep &>/dev/null '\bdocker\b'; then
    echo "User $CURRENT_USER is already in the docker group. No changes needed."
else
    echo "Adding user $CURRENT_USER to the docker group..."
    sudo usermod -aG docker "$CURRENT_USER" || {
        echo "Error: Failed to add user to the docker group."
        exit 1
    }

    echo "User $CURRENT_USER has been added to the docker group."
    echo "Changes will take effect after you log out and log back in."
fi

# Optionally apply the group change immediately for the current session
read -p "Do you want to apply the changes without logging out? (y/n): " APPLY_NOW
if [[ "$APPLY_NOW" =~ ^[Yy]$ ]]; then
    echo "Applying changes for the current session..."
    newgrp docker || {
        echo "Error: Failed to apply changes immediately. Please log out and log back in."
        exit 1
    }
    echo "Changes applied. You can now run Docker commands without sudo."
else
    echo "Please log out and log back in for the changes to take effect."
fi

# Verify the fix
echo "Testing Docker access..."
if docker ps &>/dev/null; then
    echo "Docker is accessible without sudo. You're all set!"
else
    echo "Error: Docker is still not accessible. Please check your installation or group settings."
    exit 1
fi
