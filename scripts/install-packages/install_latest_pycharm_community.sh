#!/bin/bash

set -euo pipefail

INSTALL_DIR="/opt/pycharm-community"
BIN_LINK="/usr/local/bin/pycharm"
USER_HOME=""
DESKTOP_FILE=""
ICON_PATH="$INSTALL_DIR/bin/pycharm.png"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

# Determine the current user's home directory
get_user_home() {
  if [[ -n "$SUDO_USER" ]]; then
    USER_HOME=$(eval echo ~$SUDO_USER)
  else
    USER_HOME="$HOME"
  fi
  DESKTOP_FILE="$USER_HOME/.local/share/applications/pycharm-community.desktop"
}

# Check if the launcher already exists and is valid
launcher_exists_and_valid() {
  [[ -f "$DESKTOP_FILE" ]] || return 1
  grep -q "^Exec=$INSTALL_DIR/bin/pycharm.sh %f" "$DESKTOP_FILE" || return 1
  grep -q "^Icon=$ICON_PATH" "$DESKTOP_FILE" || return 1
  return 0
}

# Check if PyCharm is installed
pycharm_installed() {
  [[ -d "$INSTALL_DIR" && -x "$INSTALL_DIR/bin/pycharm.sh" ]]
}

# Create a new desktop launcher
create_launcher() {
  log "Creating or updating the desktop launcher at $DESKTOP_FILE"

  # Remove existing launcher if it exists
  if [[ -f "$DESKTOP_FILE" ]]; then
    log "Removing existing launcher: $DESKTOP_FILE"
    rm "$DESKTOP_FILE"
  fi

  mkdir -p "$(dirname "$DESKTOP_FILE")"
  cat > "$DESKTOP_FILE" <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=PyCharm Community Edition
Icon=$ICON_PATH
Exec=$INSTALL_DIR/bin/pycharm.sh %f
Comment=Python IDE by JetBrains
Categories=Development;IDE;
Terminal=false
StartupNotify=true
EOF

  log "Desktop launcher created/updated at $DESKTOP_FILE"

  # Refresh the application menu (ensure the new launcher is registered)
  log "Refreshing application menu..."
  update-desktop-database "$USER_HOME/.local/share/applications/"
}

# Install the latest version of PyCharm
install_pycharm() {
  log "Fetching the latest PyCharm Community Edition download URL..."

  local json_data download_url pycharm_tarball tmp_tarball

  json_data=$(wget -qO- "https://data.services.jetbrains.com/products/releases?code=PCP&latest=true&type=release")

  download_url=$(echo "$json_data" | grep -oP '"linux":{"link":"\K[^"]+')

  if [[ -z "$download_url" ]]; then
    log "Failed to fetch the latest download URL. Exiting."
    exit 1
  fi

  log "Latest download URL found: $download_url"

  pycharm_tarball="${download_url##*/}"
  tmp_tarball="/tmp/$pycharm_tarball"

  log "Downloading $pycharm_tarball ..."
  wget -q --show-progress "$download_url" -O "$tmp_tarball"

  log "Extracting to $INSTALL_DIR ..."
  sudo mkdir -p "$INSTALL_DIR"
  sudo tar -xzf "$tmp_tarball" -C "$INSTALL_DIR" --strip-components=1

  log "Creating symlink $BIN_LINK ..."
  sudo ln -sf "$INSTALL_DIR/bin/pycharm.sh" "$BIN_LINK"

  log "Cleaning up temporary files..."
  rm -f "$tmp_tarball"

  log "PyCharm Community Edition installed successfully!"
}

# Main logic
main() {
  get_user_home

  log "Checking if PyCharm Community Edition is already installed..."

  if pycharm_installed; then
    log "PyCharm Community Edition seems to be installed at $INSTALL_DIR."

    if launcher_exists_and_valid; then
      log "Launcher already exists and is valid. Skipping installation."
      exit 0
    else
      log "Launcher missing or invalid. Creating/updating launcher..."
      create_launcher
      exit 0
    fi
  else
    log "PyCharm Community Edition not found. Starting installation..."
    install_pycharm
    create_launcher
  fi

  log "Installation complete! You can run PyCharm via the 'pycharm' command or through your application menu."
}

# Run the main function
main "$@"
