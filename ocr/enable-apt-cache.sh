#!/bin/bash

set -euo pipefail

DEFAULT_IP="192.168.2.127"
DEFAULT_PORT="3142"

ip="${ip:-$DEFAULT_IP}"
port="${port:-$DEFAULT_PORT}"

sources_list_path="/etc/apt/sources.list"

if [[ ! -f "$sources_list_path" ]]; then
  echo "⚠️ $sources_list_path not found. Skipping apt proxy injection."
  exit 0
fi

cp "$sources_list_path" "${sources_list_path}.bak"
echo "✅ Backup created at ${sources_list_path}.bak"

sed -i 's|http://[0-9]\{1,3\}\(\.[0-9]\{1,3\}\)\{3\}:[0-9]\{1,\}/|http://|g' "$sources_list_path"
sed -i "s|http://|http://$ip:$port/|g" "$sources_list_path"

echo "✅ Proxy IP:PORT http://$ip:$port/ injected into sources.list"
echo "====== Updated sources.list preview ======"
grep '^deb ' "$sources_list_path" | head -n 10
echo "=========================================="

echo "⏳ Running: apt update"
apt update
