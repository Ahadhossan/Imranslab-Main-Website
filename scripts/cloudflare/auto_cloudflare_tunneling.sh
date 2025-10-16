#!/usr/bin/env bash
set -euo pipefail

###############################################################################
# This script installs cloudflared (if needed), prompts for a subdomain
# and a local port, creates a Cloudflare Tunnel named after that subdomain,
# routes DNS, writes config.yml, writes a systemd service, and starts/enables it.
#
# Usage:
#   sudo ./install_cloudflared_tunnel.sh
#
# You will be asked only for:
#   1) Cloudflare login (handled by `cloudflared tunnel login`)
#   2) Subdomain name
#   3) Local port (defaults to 80)
###############################################################################

# Ensure we’re running as root
if [[ $EUID -ne 0 ]]; then
  echo "Error: This script must be run as root (e.g. via sudo)."
  exit 1
fi

# 1) Install cloudflared (if not already present)
if ! command -v cloudflared &>/dev/null; then
  echo "Installing cloudflared..."
  mkdir -p --mode=0755 /usr/share/keyrings
  curl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg \
    | tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null

  echo "deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] \
https://pkg.cloudflare.com/cloudflared any main" \
    | tee /etc/apt/sources.list.d/cloudflared.list

  apt-get update
  apt-get install -y cloudflared
else
  echo "cloudflared is already installed; skipping installation."
fi

# 2) Log in to Cloudflare (opens browser for you to complete)
echo
echo "===================="
echo " Step 1: cloudflared login "
echo "===================="
echo "Please follow the instructions in your browser to authenticate."
cloudflared tunnel login

# 3) Prompt for the subdomain (used as the tunnel name)
echo
read -rp "Enter the subdomain name you want to tunnel (e.g. 'sr-cleaning'): " sub_domain
sub_domain="${sub_domain// /}"  # strip any accidental spaces

if [[ -z "$sub_domain" ]]; then
  echo "Error: Subdomain cannot be empty."
  exit 1
fi

# 4) Prompt for the local port (default to 80 if empty)
read -rp "Enter the local port your service is listening on (default: 80): " local_port
local_port="${local_port// /}"  # strip spaces
if [[ -z "$local_port" ]]; then
  local_port=80
fi

# Optional: Validate that local_port is a positive integer
if ! [[ "$local_port" =~ ^[0-9]+$ ]]; then
  echo "Error: Port must be a positive integer."
  exit 1
fi

echo
echo "========================================"
echo " Subdomain: $sub_domain"
echo " Local port: $local_port"
echo "========================================"

# 5) Create the tunnel and capture its UUID
echo
echo "========================================"
echo " Step 2: Creating a Cloudflare Tunnel"
echo " Tunnel name: $sub_domain"
echo "========================================"
create_output="$(cloudflared tunnel create "$sub_domain")"

# Extract the tunnel ID from the "Created tunnel ..." line
tunnel_id="$(printf '%s\n' "$create_output" | awk '/Created tunnel/ {print $NF}')"

if [[ -z "$tunnel_id" ]]; then
  echo "Error: Failed to parse tunnel ID from cloudflared output."
  echo "Here is the full output for debugging:"
  echo "-------------------------------------"
  echo "$create_output"
  echo "-------------------------------------"
  exit 1
fi

echo "Tunnel '$sub_domain' created with ID: $tunnel_id"

# 6) Route DNS: create a CNAME/record so that subdomain.imranslab.org → this tunnel
echo
echo "=================================================="
echo " Step 3: Adding DNS record for $sub_domain.imranslab.org"
echo "=================================================="
cloudflared tunnel route dns "$sub_domain" "${sub_domain}.imranslab.org"

# 7) Write /etc/cloudflared/config.yml
echo
echo "========================================"
echo " Step 4: Writing /etc/cloudflared/config.yml"
echo "========================================"
mkdir -p /etc/cloudflared

cat > /etc/cloudflared/config.yml <<EOF
# --------------------------------------------------------------------------
# Cloudflared config for tunnel '$sub_domain'
# --------------------------------------------------------------------------
tunnel: $tunnel_id
credentials-file: "/root/.cloudflared/$tunnel_id.json"

ingress:
  - hostname: "${sub_domain}.imranslab.org"
    service: http://localhost:${local_port}
  - service: http_status:404
EOF

echo "/etc/cloudflared/config.yml created."

# 8) Write the systemd service unit at /etc/systemd/system/cloudflared.service
echo
echo "================================================"
echo " Step 5: Creating systemd unit file: cloudflared"
echo "================================================"
cat > /etc/systemd/system/cloudflared.service <<EOF
[Unit]
Description=Cloudflare Tunnel for $sub_domain
After=network.target

[Service]
# If cloudflared is installed in a different location, adjust the path below.
ExecStart=/usr/local/bin/cloudflared tunnel run $sub_domain
Restart=on-failure
User=root
Group=root
# Exporting CF_TUNNEL_ID is optional; some setups may use it
Environment=CF_TUNNEL_ID=$tunnel_id

[Install]
WantedBy=multi-user.target
EOF

echo "/etc/systemd/system/cloudflared.service created."

# 9) Reload systemd, start & enable the service
echo
echo "======================================="
echo " Step 6: Reloading systemd and starting"
echo "======================================"
systemctl daemon-reload
systemctl enable --now cloudflared

echo
echo "========================================"
echo " All done! "
echo " Tunnel name : $sub_domain"
echo " Tunnel ID   : $tunnel_id"
echo " Hostname    : ${sub_domain}.imranslab.org"
echo " Forwarding  : http://localhost:${local_port}"
echo
echo "To check the service status: sudo systemctl status cloudflared"
echo "Logs can be viewed with: journalctl -u cloudflared --follow"
echo "========================================"
