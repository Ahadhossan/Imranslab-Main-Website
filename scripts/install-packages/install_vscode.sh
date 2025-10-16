#!/bin/bash
set -euo pipefail

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

install_vscode_noninteractive() {
  if command -v code >/dev/null 2>&1; then
    log "VSCode is already installed."
    exit 0
  fi

  log "Adding Microsoft GPG key..."
  wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
  sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/
  rm microsoft.gpg

  log "Adding Microsoft VSCode repository..."
  echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list

  log "Updating apt cache..."
  sudo apt-get update -y

  log "Installing VSCode..."
  # Use DEBIAN_FRONTEND=noninteractive to suppress prompts
  DEBIAN_FRONTEND=noninteractive sudo apt-get install -y code

  log "VSCode installed successfully!"
}

install_vscode_noninteractive
