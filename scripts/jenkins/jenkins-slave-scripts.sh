#!/bin/bash

set -e

echo "🔧 Updating package list..."
sudo apt update


echo "📦 Installing core dependencies..."
sudo apt install -y \
    git \
    curl \
    openssh-server \
    vim \
    ca-certificates \
    gnupg \
    lsb-release \
    software-properties-common \
    openjdk-21-jdk

echo "🛡️ Setting up Docker repository..."
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

echo "📦 Installing Docker Engine and Compose Plugin..."
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

echo "👤 Adding current user to docker group..."
sudo usermod -aG docker $USER

echo "☕ Installing Java 17..."
sudo apt install -y openjdk-17-jdk

echo "🚀 Enabling and starting SSH server..."
sudo systemctl enable ssh
sudo systemctl start ssh

# Headless session Docker group fix
exec sg docker newgrp `id -gn` || true

echo "✅ Setup completed successfully!"
echo "🐳 Docker group reloaded for current session."

sudo snap install docker -y && sudo apt install docker-compose -y