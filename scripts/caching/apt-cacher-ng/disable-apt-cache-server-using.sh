#!/bin/bash

# Define the file path to sources.list
sources_list_path="/etc/apt/sources.list"

# Backup the original sources.list file
cp $sources_list_path "${sources_list_path}.bak"
echo "Backup of sources.list created at ${sources_list_path}.bak"

# Remove only the IP:Port part of the lines
sed -i 's|http://[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}:[0-9]\{1,\}/|http://|' $sources_list_path

# Confirm the changes
echo "IP:port part has been removed from sources.list."
cat $sources_list_path

# Update package lists
echo "Updating package list..."
sudo apt update
