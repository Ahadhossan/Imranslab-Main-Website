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