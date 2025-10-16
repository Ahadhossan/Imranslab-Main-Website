#!/bin/bash
set -euo pipefail

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

uninstall_vscode() {
  if ! command -v code >/dev/null 2>&1; then
    log "VSCode is not installed."
    exit 0
  fi

  log "Removing Visual Studio Code package..."
  sudo apt-get remove --purge -y code

  log "Removing Microsoft VSCode repository file..."
  sudo rm -f /etc/apt/sources.list.d/vscode.list

  log "Removing Microsoft GPG key for VSCode..."
  sudo rm -f /usr/share/keyrings/microsoft.gpg

  log "Running autoremove to clean dependencies..."
  sudo apt-get autoremove -y

  log "Updating apt cache..."
  sudo apt-get update -y

  log "VSCode uninstalled successfully!"
}

uninstall_vscode