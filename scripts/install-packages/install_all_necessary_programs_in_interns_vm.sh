#!/bin/bash
set -euo pipefail

# ---------- Shared Logging & Utility Functions ----------

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

check_root() {
  if [[ "$EUID" -ne 0 ]]; then
    log "❌ Please run this script as root (sudo)."
    exit 1
  fi
}

get_user_home() {
  if [[ -n "${SUDO_USER:-}" ]]; then
    USER_HOME="$(eval echo "~$SUDO_USER")"
  else
    USER_HOME="$HOME"
  fi
  DESKTOP_FILE="$USER_HOME/.local/share/applications/android-studio.desktop"
}

cleanup() {
  [[ -n "${TMP_DIR:-}" && -d "$TMP_DIR" ]] && rm -rf "$TMP_DIR"
}
trap cleanup EXIT

android_studio_installed() {
  [[ -x "$INSTALL_DIR/bin/studio.sh" ]]
}

create_launcher() {
  log "Creating/updating desktop launcher at: $DESKTOP_FILE"

  if [[ -f "$DESKTOP_FILE" ]]; then
    rm -f "$DESKTOP_FILE"
  fi

  mkdir -p "$(dirname "$DESKTOP_FILE")"
  cat > "$DESKTOP_FILE" <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Android Studio
Icon=$ICON_PATH
Exec=$INSTALL_DIR/bin/studio.sh %f
Comment=Android IDE by Google
Categories=Development;IDE;
Terminal=false
StartupNotify=true
EOF

  log "Desktop launcher written."
  log "Refreshing application menu..."
  update-desktop-database "$(dirname "$DESKTOP_FILE")" &> /dev/null || true
}

install_android_studio() {
  log "Fetching https://developer.android.com/studio ..."
  DOWNLOAD_PAGE_HTML="$TMP_DIR/page.html"
  curl -fsSL "https://developer.android.com/studio" -o "$DOWNLOAD_PAGE_HTML"

  log "Extracting the latest stable Linux tarball URL..."
  DOWNLOAD_URL=$(
    grep -Eo 'href="https://redirector\.gvt1\.com/edgedl/android/studio/ide-zips/[0-9]+(\.[0-9]+)*/android-studio-[0-9]+(\.[0-9]+)*-linux\.tar\.gz"' \
      "$DOWNLOAD_PAGE_HTML" \
    | head -n 1 \
    | sed -E 's/^href="([^"]+)".*/\1/'
  )

  if [[ -z "$DOWNLOAD_URL" ]]; then
    log "❌ ERROR: Could not find a stable Linux tarball URL."
    log "Here's a snippet of the fetched HTML (first 40 lines) for debugging:"
    head -n 40 "$DOWNLOAD_PAGE_HTML" | sed 's/$/\\n/'
    exit 1
  fi

  log "Latest stable download URL detected: $DOWNLOAD_URL"

  BASENAME="${DOWNLOAD_URL##*/}"
  TMP_TARBALL="$TMP_DIR/$BASENAME"

  log "Downloading Android Studio tarball: $BASENAME"
  wget -q --show-progress "$DOWNLOAD_URL" -O "$TMP_TARBALL"

  log "Creating installation directory: $INSTALL_DIR"
  mkdir -p "$INSTALL_DIR"

  log "Extracting tarball into $INSTALL_DIR ..."
  tar -xzf "$TMP_TARBALL" -C "$INSTALL_DIR" --strip-components=1

  log "Creating symlink: $BIN_LINK → $INSTALL_DIR/bin/studio.sh"
  ln -sf "$INSTALL_DIR/bin/studio.sh" "$BIN_LINK"

  log "Cleaning up temporary tarball..."
  rm -f "$TMP_TARBALL"

  log "✅ Android Studio installed under $INSTALL_DIR"
}

# ---------- Main Script ----------

main() {
  check_root
  get_user_home

  INSTALL_DIR="/opt/android-studio"
  BIN_LINK="/usr/local/bin/android-studio"
  ICON_PATH="$INSTALL_DIR/bin/studio.png"

  log "----------------------------------------"
  log " Installing or Updating: Android Studio "
  log "----------------------------------------"

  # Create a temporary directory for downloads and parsing
  TMP_DIR="$(mktemp -d)"

  # 1) Ensure required 32-bit libraries for Android Studio on 64-bit Linux
  log "Checking 32-bit dependencies..."

  # Enable i386 architecture if not already
  if ! dpkg --print-foreign-architectures | grep -q i386; then
    log "Enabling i386 architecture..."
    dpkg --add-architecture i386
    apt-get update -y
  fi

  # Install libraries; skip if already installed
  REQUIRED_PKGS=(
    libc6:i386
    libncurses5:i386
    libstdc++6:i386
    lib32z1
    libbz2-1.0:i386
  )

  for pkg in "${REQUIRED_PKGS[@]}"; do
    if dpkg -l | grep -q "^ii  $pkg "; then
      log "✅ Dependency already installed: $pkg"
    else
      log "Installing dependency: $pkg"
      apt-get install -y "$pkg"
    fi
  done

  # 2) Install or update Android Studio
  if android_studio_installed; then
    log "Android Studio already installed at $INSTALL_DIR."
    create_launcher
    log "✅ Desktop launcher updated. To reinstall, remove $INSTALL_DIR and re-run."
  else
    log "Android Studio not found. Proceeding with fresh install."
    install_android_studio
    create_launcher
  fi

  log "🎉 Done. Launch Android Studio via 'android-studio' or from your application menu."
}

main "$@"




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



INSTALL_DIR="/opt/idea-community"
BIN_LINK="/usr/local/bin/idea"
ICON_PATH="$INSTALL_DIR/bin/idea.png"
DESKTOP_FILE=""
USER_HOME=""

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

get_user_home() {
  if [[ -n "$SUDO_USER" ]]; then
    USER_HOME=$(eval echo ~$SUDO_USER)
  else
    USER_HOME="$HOME"
  fi
  DESKTOP_FILE="$USER_HOME/.local/share/applications/idea-community.desktop"
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
Name=IntelliJ IDEA Community Edition
Icon=$ICON_PATH
Exec=$INSTALL_DIR/bin/idea.sh %f
Comment=Java IDE by JetBrains
Categories=Development;IDE;
Terminal=false
StartupNotify=true
EOF
  log "Desktop launcher created at $DESKTOP_FILE"

  # Refresh the application menu (ensure the new launcher is registered)
  log "Refreshing application menu..."
  update-desktop-database "$USER_HOME/.local/share/applications/"
}

install_idea() {
  log "Fetching the latest IntelliJ IDEA Community Edition download URL..."

  local json_data download_url idea_tarball tmp_tarball

  # Fetch the latest release URL from JetBrains
  json_data=$(wget -qO- "https://data.services.jetbrains.com/products/releases?code=IIU&latest=true&type=release")
  
  # Extract the download URL for the Linux version
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
  get_user_home

  log "Checking if IntelliJ IDEA Community Edition is already installed..."

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

  log "Installation complete! You can run IntelliJ IDEA via the 'idea' command or through your application menu."
}

main "$@"


INSTALL_DIR="/opt/tailscale"
BIN_LINK="/usr/local/bin/tailscale"
DESKTOP_FILE=""
USER_HOME=""
ICON_PATH="/opt/tailscale/tailscale.png"

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
  DESKTOP_FILE="$USER_HOME/.local/share/applications/tailscale.desktop"
}

# Check if the launcher already exists and is valid
launcher_exists_and_valid() {
  [[ -f "$DESKTOP_FILE" ]] || return 1
  grep -q "^Exec=$INSTALL_DIR/tailscale %f" "$DESKTOP_FILE" || return 1
  grep -q "^Icon=$ICON_PATH" "$DESKTOP_FILE" || return 1
  return 0
}

# Check if Tailscale is already installed
tailscale_installed() {
  [[ -d "$INSTALL_DIR" && -x "$INSTALL_DIR/tailscale" ]]
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
Name=Tailscale
Icon=$ICON_PATH
Exec=$INSTALL_DIR/tailscale %f
Comment=Zero-config VPN solution
Categories=Network;VPN;
Terminal=false
StartupNotify=true
EOF

  log "Desktop launcher created/updated at $DESKTOP_FILE"

  # Refresh the application menu
  log "Refreshing application menu..."
  update-desktop-database "$USER_HOME/.local/share/applications/"
}

# Install the latest version of Tailscale
install_tailscale() {
  log "Fetching the latest Tailscale installation script..."

  # Download and install Tailscale using their official package
  curl -fsSL https://tailscale.com/install.sh | sh

  log "Tailscale installed successfully!"
}

# Main logic
main() {
  get_user_home

  log "Checking if Tailscale is already installed..."

  if tailscale_installed; then
    log "Tailscale seems to be installed at $INSTALL_DIR."

    if launcher_exists_and_valid; then
      log "Launcher already exists and is valid. Skipping installation."
      exit 0
    else
      log "Launcher missing or invalid. Creating/updating launcher..."
      create_launcher
      exit 0
    fi
  else
    log "Tailscale not found. Starting installation..."
    install_tailscale
    create_launcher
  fi

  log "Installation complete! You can run Tailscale via the 'tailscale' command or through your application menu."
}

main "$@"


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




# ======================================
# Uninstall Firefox from Ubuntu Script
# ======================================
#
# This script removes Firefox if it is installed via Snap or APT,
# purges configuration files, and performs cleanup.
#
# Usage:
#   sudo ./uninstall_firefox.sh

# ---------- Logging & Utility Functions ----------

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

check_root() {
  if [[ "$EUID" -ne 0 ]]; then
    log "❌ Please run this script as root (sudo)."
    exit 1
  fi
}

# ---------- Uninstallation Logic ----------

remove_snap_firefox() {
  if snap list | grep -q "^firefox "; then
    log "Removing Firefox Snap..."
    snap remove firefox
    log "✅ Firefox Snap removed."
  else
    log "➖ Firefox Snap not found."
  fi
}

remove_apt_firefox() {
  # Check if any firefox package is installed via APT
  if dpkg -l | grep -q "^ii.*firefox"; then
    log "Removing Firefox APT package(s)..."
    apt-get update -y
    apt-get remove --purge -y firefox firefox-* || true
    apt-get autoremove -y
    log "✅ Firefox APT packages removed."
  else
    log "➖ Firefox APT package not found."
  fi
}

purge_user_configs() {
  log "Purging user configuration files..."
  # Remove global configuration directory
  rm -rf /etc/firefox
  # Remove system-wide cache and profiles
  rm -rf /usr/lib/firefox
  rm -rf /usr/lib/firefox-esr
  rm -rf /usr/lib/firefox-*/ 
  # Remove per-user profiles and caches
  if [[ -n "${SUDO_USER:-}" ]]; then
    TARGET_USER="$SUDO_USER"
  else
    TARGET_USER="$(logname 2>/dev/null || echo "$USER")"
  fi

  # Delete configuration and cache directories in each home
  for home in /home/*; do
    if [[ -d "$home/.mozilla/firefox" ]]; then
      log "Deleting $home/.mozilla/firefox"
      rm -rf "$home/.mozilla/firefox"
    fi
    if [[ -d "$home/.cache/mozilla/firefox" ]]; then
      log "Deleting $home/.cache/mozilla/firefox"
      rm -rf "$home/.cache/mozilla/firefox"
    fi
    if [[ -d "$home/.local/share/applications" ]]; then
      # Remove any firefox.desktop entries
      find "$home/.local/share/applications" -maxdepth 1 -type f -iname "firefox*.desktop" -exec rm -f {} \;
    fi
  done

  # Also remove for root
  if [[ -d "/root/.mozilla/firefox" ]]; then
    log "Deleting /root/.mozilla/firefox"
    rm -rf /root/.mozilla/firefox
  fi
  if [[ -d "/root/.cache/mozilla/firefox" ]]; then
    log "Deleting /root/.cache/mozilla/firefox"
    rm -rf /root/.cache/mozilla/firefox
  fi

  log "✅ User configuration cleanup complete."
}

# ---------- Main Execution ----------

main() {
  check_root

  log "-----------------------------------------"
  log " Uninstalling Firefox from Ubuntu "
  log "-----------------------------------------"

  remove_snap_firefox
  remove_apt_firefox
  purge_user_configs

  log "🎉 Done. Firefox has been uninstalled, and related files have been removed."
}

main "$@"
