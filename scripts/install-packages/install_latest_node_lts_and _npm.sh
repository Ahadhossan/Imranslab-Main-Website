
#!/bin/bash

set -euo pipefail

USER_HOME=""
CURRENT_VERSION=""
LATEST_VERSION=""
INSTALL_DIR="/usr/local/lib/nodejs"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

# Detect current user's home directory
get_user_home() {
  if [[ -n "$SUDO_USER" ]]; then
    USER_HOME=$(eval echo ~$SUDO_USER)
  else
    USER_HOME="$HOME"
  fi
}

# Fetch the latest LTS version of Node.js
get_latest_lts_version() {
  LATEST_VERSION=$(curl -fsSL https://nodejs.org/dist/index.json | jq -r 'map(select(.LTS == true)) | .[0].version')
}

# Check installed Node.js version
check_installed_version() {
  if command -v node &>/dev/null; then
    CURRENT_VERSION=$(node -v)
    log "Currently installed version: $CURRENT_VERSION"
  else
    CURRENT_VERSION=""
  fi
}

# Uninstall the current Node.js version
uninstall_current_version() {
  if [[ -n "$CURRENT_VERSION" ]]; then
    log "Uninstalling current Node.js version..."
    sudo apt-get remove --purge -y nodejs
    sudo apt-get autoremove -y
    log "Current Node.js version uninstalled."
  else
    log "No Node.js version detected, skipping uninstallation."
  fi
}

# Install the latest LTS version of Node.js
install_latest_lts_version() {
  log "Adding NodeSource repository for LTS version..."

  # Add the NodeSource repository for the latest LTS version
  curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -

  log "Installing Node.js LTS version..."
  sudo apt-get install -y nodejs

  log "Node.js LTS version $LATEST_VERSION installed successfully!"
}

# Main logic
main() {
  get_user_home

  log "Checking if Node.js is already installed..."

  # Fetch the latest LTS version
  sudo apt install jq
  get_latest_lts_version

  check_installed_version

  # Compare the installed version with the latest LTS version
  if [[ "$CURRENT_VERSION" == "$LATEST_VERSION" ]]; then
    log "Installed version ($CURRENT_VERSION) is the latest LTS version. Skipping installation."
  else
    log "Installed version ($CURRENT_VERSION) is not the latest LTS version ($LATEST_VERSION). Uninstalling old version and installing the latest LTS..."
    uninstall_current_version
    install_latest_lts_version
  fi

  log "Installation complete! You can verify by running 'node -v' and 'npm -v'."
}

main "$@"
