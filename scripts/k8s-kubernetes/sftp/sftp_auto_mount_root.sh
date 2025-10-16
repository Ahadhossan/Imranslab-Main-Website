#!/bin/bash

set -e

# --------------------------- CONFIG --------------------------- #
REMOTE_IP="192.168.2.206"
REMOTE_USER="sftpuser"
REMOTE_PATH="/srv/sftp_storage/upload"
LOCAL_SUBFOLDER="sftp_storage"
LOG_FILE="/var/log/sftp-auto-setup.log"
SYSTEMD_PATH="/etc/systemd/system"
# ------------------------------------------------------------- #

log() {
    echo -e "[`date '+%Y-%m-%d %H:%M:%S'`] $1" | tee -a "$LOG_FILE"
}

# Step 0: Check sshfs installed or not
if ! command -v sshfs &> /dev/null
then
    log "🚀 sshfs not found... Installing sshfs..."
    apt update
    apt install -y sshfs
else
    log "🔍 sshfs already installed."
fi

# Step 0.5: Check and create mount.fuse.sshfs symlink if missing
if [ ! -f "/sbin/mount.fuse.sshfs" ]; then
    log "🔗 Creating symlink for mount.fuse.sshfs..."
    ln -s $(which sshfs) /sbin/mount.fuse.sshfs
else
    log "🔗 mount.fuse.sshfs already exists."
fi


echo "🔧 Starting SFTP Auto Mount Setup..."
sleep 1

# Step 1: Detect username & home
USERNAME=${SUDO_USER:-$(whoami)}
USER_HOME=$(eval echo ~$USERNAME)
MOUNT_PATH="${USER_HOME}/${LOCAL_SUBFOLDER}"
if [[ "$USER_HOME" == "/root" ]]; then
    UNIT_NAME="root-${LOCAL_SUBFOLDER}.mount"
else
    UNIT_NAME="home-${USERNAME}-${LOCAL_SUBFOLDER}.mount"
fi
UNIT_FILE="${SYSTEMD_PATH}/${UNIT_NAME}"

log "👤 Detected user: $USERNAME"
log "📁 Home directory: $USER_HOME"
log "📌 Mount path: $MOUNT_PATH"
log "⚙️ Unit file: $UNIT_FILE"

# Step 2: Generate SSH key if not present
if [ ! -f "$USER_HOME/.ssh/id_rsa" ]; then
    log "🔐 Generating SSH key..."
    ssh-keygen -t rsa -b 4096 -f "$USER_HOME/.ssh/id_rsa" -N ""
else
    log "🔑 SSH key already exists."
fi

# Step 3: Copy SSH key to server
log "🚀 Copying SSH key to $REMOTE_USER@$REMOTE_IP..."
ssh-copy-id -i "$USER_HOME/.ssh/id_rsa.pub" "$REMOTE_USER@$REMOTE_IP"

# Step 4: Create mount folder
if [ ! -d "$MOUNT_PATH" ]; then
    mkdir -p "$MOUNT_PATH"
    log "📂 Created mount point: $MOUNT_PATH"
else
    log "📂 Mount point already exists."
fi

# Step 5: Generate systemd mount unit
log "🛠️ Creating systemd mount unit..."
cat <<EOF | tee "$UNIT_FILE" > /dev/null
[Unit]
Description=Mount SFTP Storage for $USERNAME
After=network-online.target
Wants=network-online.target

[Mount]
What=${REMOTE_USER}@${REMOTE_IP}:${REMOTE_PATH}
Where=${MOUNT_PATH}
Type=fuse.sshfs
Options=_netdev,allow_other,IdentityFile=${USER_HOME}/.ssh/id_rsa,idmap=user,StrictHostKeyChecking=no
TimeoutSec=30

[Install]
WantedBy=multi-user.target
EOF

# Step 6: Reload and enable mount unit
log "🔁 Reloading systemd daemon..."
systemctl daemon-reload

log "📌 Enabling and starting mount unit..."
systemctl enable "$UNIT_NAME"
systemctl start "$UNIT_NAME"

# Step 7: Confirm status
sleep 1
echo
systemctl status "$UNIT_NAME" --no-pager
echo

# Step 8: Final check
if mountpoint -q "$MOUNT_PATH"; then
    log "✅ Mount successful at $MOUNT_PATH"
else
    log "❌ Mount failed. Please check systemctl status $UNIT_NAME"
fi

log "🎉 SFTP auto mount setup complete."
