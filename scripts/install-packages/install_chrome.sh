#!/bin/bash
set -euo pipefail

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

install_chrome() {
  log "Checking if Google Chrome is already installed..."

  if command -v google-chrome >/dev/null 2>&1; then
    log "Google Chrome is already installed."
    exit 0
  fi

  log "Downloading latest Google Chrome .deb package..."

  TMP_DEB="/tmp/google-chrome-stable_current_amd64.deb"
  wget -q --show-progress https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O "$TMP_DEB"

  log "Installing Google Chrome package..."
  sudo apt-get update -y
  sudo apt-get install -y "$TMP_DEB" || {
    log "Fixing dependencies if installation failed..."
    sudo apt-get install -f -y
  }

  log "Cleaning up..."
  rm -f "$TMP_DEB"

  log "Google Chrome installation complete!"
}

install_chrome
