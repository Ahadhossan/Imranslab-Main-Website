#!/bin/bash

set -euo pipefail

# ===== DEFAULT IP and PORT =====
DEFAULT_IP="192.168.2.127"
DEFAULT_PORT="3142"

# ===== PROMPT FOR INPUT =====
# read -p "Enter proxy IP [$DEFAULT_IP]: " ip
ip="${ip:-$DEFAULT_IP}"

# read -p "Enter proxy Port [$DEFAULT_PORT]: " port
port="${port:-$DEFAULT_PORT}"

# ===== FILE TO MODIFY =====
sources_list_path="/etc/apt/sources.list"

# ===== BACKUP FIRST =====
cp "$sources_list_path" "${sources_list_path}.bak"
echo "✅ Backup created at ${sources_list_path}.bak"

# ===== REMOVE OLD IP:PORT IF ANY =====
sed -i 's|http://[0-9]\{1,3\}\(\.[0-9]\{1,3\}\)\{3\}:[0-9]\{1,\}/|http://|g' "$sources_list_path"

# ===== ADD NEW IP:PORT =====
sed -i "s|http://|http://$ip:$port/|g" "$sources_list_path"

# ===== CONFIRMATION =====
echo "✅ Proxy IP:PORT http://$ip:$port/ injected into sources.list"
echo "====== Updated sources.list preview ======"
grep '^deb ' "$sources_list_path" | head -n 10
echo "=========================================="

# ===== RUN UPDATE =====
echo "⏳ Running: sudo apt update"
sudo apt update
