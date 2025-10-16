#!/bin/bash

# Download the installer
curl -sSL https://ollama.ai/install.sh -o ollama_installer.sh

# Make it executable
chmod +x ollama_installer.sh

# Run the installer
./ollama_installer.sh

# Print completion message with URL
echo "Ollama installation complete! For more information, visit https://ollama.ai"
