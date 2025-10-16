#!/bin/bash

# https://chatgpt.com/g/g-p-67d9c917afa8819182e4bc14ae699799-devops/c/683c29c6-d1e0-800d-89c0-fbb42814c33e 

set -euo pipefail

INSTALL_DIR="/opt/idea-community"
BIN_LINK="/usr/local/bin/idea"
DESKTOP_FILE="$HOME/.local/share/applications/idea-community.desktop"
ICON_PATH="$INSTALL_DIR/bin/idea.png"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

launcher_exists_and_valid() {
  [[ -f "$DESKTOP_FILE" ]] || return 1
  grep -q "^Exec=$INSTALL_DIR/bin/idea.sh %f" "$DESKTOP_FILE" || return 1
  grep -q "^Icon=$ICON_PATH" "$DESKTOP_FILE" || return 1
  return 0
}

idea_installed() {
  [[ -d "$INSTALL_DIR" && -x "$INSTALL_DIR/bin/idea.sh" ]]
}

create_launcher() {
  mkdir -p "$(dirname "$DESKTOP_FILE")"
  cat > "$DESKTOP_FILE" <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=IntelliJ IDEA Community Edition
Icon=$ICON_PATH
Exec=$INSTALL_DIR/bin/idea.sh %f
Comment=Java IDE by JetBrains
Categories=Development;IDE;
Terminal=false
StartupNotify=true
EOF
  log "Desktop launcher created/updated at $DESKTOP_FILE"
}

install_idea() {
  log "Fetching latest IntelliJ IDEA Community Edition download URL..."

  local json_data download_url idea_tarball tmp_tarball

  json_data=$(wget -qO- "https://data.services.jetbrains.com/products/releases?code=IIU&latest=true&type=release")

  # Extract Linux link for IntelliJ IDEA Community Edition (product code IIU)
  download_url=$(echo "$json_data" | grep -oP '"linux":{"link":"\K[^"]+')

  if [[ -z "$download_url" ]]; then
    log "Failed to fetch the latest download URL. Exiting."
    exit 1
  fi

  log "Latest download URL found: $download_url"

  idea_tarball="${download_url##*/}"
  tmp_tarball="/tmp/$idea_tarball"

  log "Downloading $idea_tarball ..."
  wget -q --show-progress "$download_url" -O "$tmp_tarball"

  log "Extracting to $INSTALL_DIR ..."
  sudo mkdir -p "$INSTALL_DIR"
  sudo tar -xzf "$tmp_tarball" -C "$INSTALL_DIR" --strip-components=1

  log "Creating symlink $BIN_LINK ..."
  sudo ln -sf "$INSTALL_DIR/bin/idea.sh" "$BIN_LINK"

  log "Cleaning up temporary files..."
  rm -f "$tmp_tarball"

  log "IntelliJ IDEA Community Edition installed successfully!"
}

main() {
  if idea_installed; then
    log "IntelliJ IDEA Community Edition seems to be installed at $INSTALL_DIR."

    if launcher_exists_and_valid; then
      log "Launcher already exists and is valid. Skipping installation."
      exit 0
    else
      log "Launcher missing or invalid. Creating/updating launcher..."
      create_launcher
      exit 0
    fi
  else
    log "IntelliJ IDEA Community Edition not found. Starting installation..."
    install_idea
    create_launcher
  fi

  log "Installation complete! Run IntelliJ IDEA via 'idea' command or your application menu."
}

main "$@"
