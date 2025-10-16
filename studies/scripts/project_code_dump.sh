#!/bin/bash

# Get the parent directory path (one level up from the script's location)
PARENT_DIR=$(dirname "$PWD")

# Get the parent directory name
PARENT_DIR_NAME=$(basename "$PARENT_DIR")

# Define the name of the text file (using the parent directory name)
TEXT_FILE_NAME="${PARENT_DIR_NAME}_code_dump.txt"

# Define the path to the Downloads folder
DOWNLOADS_FOLDER="$HOME/Downloads"

# Full path to the text file
TEXT_FILE_PATH="$DOWNLOADS_FOLDER/$TEXT_FILE_NAME"

# Check if a text file with the same name already exists in the Downloads folder
if [ -f "$TEXT_FILE_PATH" ]; then
  echo "Deleting existing text file: $TEXT_FILE_PATH"
  rm -f "$TEXT_FILE_PATH" || { echo "Failed to delete existing text file"; exit 1; }
fi

# Move to the parent directory
cd "$PARENT_DIR" || { echo "Failed to change directory to $PARENT_DIR"; exit 1; }

# Create the text file and write the directory structure and file contents
{
  # Generate a directory tree (excluding unnecessary files and directories)
  echo "===== DIRECTORY TREE ====="
  tree -a -I '.git|node_modules|venv|.venv|.idea|.pytest_cache|dist|build|__pycache__|.cache|.DS_Store' .

  # Add a separator
  echo -e "\n\n===== FILE CONTENTS ====="

  # Find non-empty files smaller than 0.5 MB (500 KB) and include their contents
  # Exclude unnecessary files and directories
  find . -type f -size +0 -size -500k \
    ! -path "*/.git/*" \
    ! -path "*/node_modules/*" \
    ! -path "*/venv/*" \
    ! -path "*/.venv/*" \
    ! -path "*/.idea/*" \
    ! -path "*/.pytest_cache/*" \
    ! -path "*/dist/*" \
    ! -path "*/build/*" \
    ! -path "*/__pycache__/*" \
    ! -path "*/.cache/*" \
    ! -path "*/.DS_Store" \
    -print | while read -r file; do
      # Print the file path as a header
      echo -e "\n===== FILE: $file ====="
      # Indent the file contents by 4 spaces
      sed 's/^/    /' "$file"
    done
} > "$TEXT_FILE_PATH"

# Notify the user that the text file has been created
echo "Text file '$TEXT_FILE_NAME' created successfully and saved to '$DOWNLOADS_FOLDER'."

# Copy the content of the text file to the clipboard (if possible)
if command -v xclip &> /dev/null; then
  # Linux: Use xclip
  xclip -selection clipboard < "$TEXT_FILE_PATH"
  echo "Content copied to clipboard using xclip."
elif command -v pbcopy &> /dev/null; then
  # macOS: Use pbcopy
  pbcopy < "$TEXT_FILE_PATH"
  echo "Content copied to clipboard using pbcopy."
else
  # Fallback: Display the content in the terminal
  echo "Clipboard tool not found. Displaying content below:"
  echo "-----------------------------------------------"
  cat "$TEXT_FILE_PATH"
  echo "-----------------------------------------------"
  echo "You can manually copy the content from above."
fi