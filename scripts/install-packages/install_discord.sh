#!/bin/bash

set -euo pipefail

INSTALL_DIR="/opt/discord"
BIN_LINK="/usr/local/bin/discord"
DESKTOP_FILE=""
USER_HOME=""
ICON_PATH="$INSTALL_DIR/discord.png"

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
  DESKTOP_FILE="$USER_HOME/.local/share/applications/discord.desktop"
}

# Check if the launcher already exists and is valid
launcher_exists_and_valid() {
  [[ -f "$DESKTOP_FILE" ]] || return 1
  grep -q "^Exec=$INSTALL_DIR/Discord %f" "$DESKTOP_FILE" || return 1
  grep -q "^Icon=$ICON_PATH" "$DESKTOP_FILE" || return 1
  return 0
}

# Check if Discord is already installed
discord_installed() {
  [[ -d "$INSTALL_DIR" && -x "$INSTALL_DIR/Discord" ]]
}

# Create or update the desktop launcher
create_launcher() {
  log "Creating or updating desktop launcher at $DESKTOP_FILE"

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
Name=Discord
Icon=$ICON_PATH
Exec=$INSTALL_DIR/Discord %f
Comment=Voice, video and text chat for gamers
Categories=Games;Social;Network;
Terminal=false
StartupNotify=true
EOF

  log "Desktop launcher created/updated at $DESKTOP_FILE"

  # Refresh the application menu
  log "Refreshing application menu..."
  update-desktop-database "$USER_HOME/.local/share/applications/"
}

# Install the latest version of Discord
install_discord() {
  log "Fetching the latest Discord download URL..."

  local download_url discord_tarball tmp_tarball

  # Get the latest Discord version download URL from the official website
  download_url="https://discord.com/api/download?platform=linux&format=tar.gz"

  log "Latest download URL found: $download_url"

  discord_tarball="discord.tar.gz"
  tmp_tarball="/tmp/$discord_tarball"

  log "Downloading $discord_tarball ..."
  wget -q --show-progress "$download_url" -O "$tmp_tarball"

  log "Extracting to $INSTALL_DIR ..."
  sudo mkdir -p "$INSTALL_DIR"
  sudo tar -xzf "$tmp_tarball" -C "$INSTALL_DIR" --strip-components=1

  log "Creating symlink $BIN_LINK ..."
  sudo ln -sf "$INSTALL_DIR/Discord" "$BIN_LINK"

  log "Cleaning up temporary files..."
  rm -f "$tmp_tarball"

  log "Discord installed successfully!"
}

# Main logic
main() {
  get_user_home

  log "Checking if Discord is already installed..."

  if discord_installed; then
    log "Discord seems to be installed at $INSTALL_DIR."

    if launcher_exists_and_valid; then
      log "Launcher already exists and is valid. Skipping installation."
      exit 0
    else
      log "Launcher missing or invalid. Creating/updating launcher..."
      create_launcher
      exit 0
    fi
  else
    log "Discord not found. Starting installation..."
    install_discord
    create_launcher
  fi

  log "Installation complete! You can run Discord via the 'discord' command or through your application menu."
}

main "$@"
