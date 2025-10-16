#!/bin/bash
# ===========================
# 🚀 GPT Helper Script (Stable Version) 🚀
# ===========================
# Fixed find command syntax + proper glob handling
# Last updated: 2023-10-15

set -euo pipefail

# ======= CONFIGURATION =======
DEBUG=1
DUMP_FILE="gpt_dump.txt"
MAX_SIZE=$((1024*1024))  # 1MB
ALLOWED_EXTENSIONS=("sh" "py" "yml" "yaml")
ALLOWED_FILENAMES=("Dockerfile" "docker-compose.yml")
IGNORE_FOLDERS=(".venv" "venv" "node_modules" "test_env")  # Folders to ignore
# ============================

debug() {
    [ "$DEBUG" -eq 1 ] && echo "DEBUG: $*" >&2
}

echo -e "\n📝 Gathering project structure for GPT..."
echo "----------------------------------------"

# Initialize environment
mkdir -p logs
: > "$DUMP_FILE" || { echo "❌ Cannot write to $DUMP_FILE"; exit 1; }
export LC_ALL=C.UTF-8

add_section() {
    echo -e "\n### $1 ###\n" >> "$DUMP_FILE"
}

build_find_conditions() {
    set -f  # Disable globbing
    local conditions=()

    # Add file extensions
    for ext in "${ALLOWED_EXTENSIONS[@]}"; do
        conditions+=("-iname")
        conditions+=("*.${ext}")
        conditions+=("-o")
    done

    # Add specific filenames
    for fname in "${ALLOWED_FILENAMES[@]}"; do
        conditions+=("-name")
        conditions+=("${fname}")
        conditions+=("-o")
    done

    # Remove trailing -o
    if [ ${#conditions[@]} -gt 0 ]; then
        unset 'conditions[${#conditions[@]}-1]'
    fi

    echo "${conditions[@]}"
    set +f  # Re-enable globbing
}

# Generate find conditions
set -f
FIND_CONDITIONS=($(build_find_conditions))
set +f
debug "FIND_CONDITIONS: ${FIND_CONDITIONS[*]}"

# Build find ignore conditions for specified folders
IGNORE_CONDITIONS=()
for folder in "${IGNORE_FOLDERS[@]}"; do
    IGNORE_CONDITIONS+=("-not" -path "./$folder/*")
done

#############################
# === ROOT FILES SECTION ===
#############################
add_section "ROOT FILES (Allowed Types)"
(
    set -f
    find . -maxdepth 1 -type f \( "${FIND_CONDITIONS[@]}" \) "${IGNORE_CONDITIONS[@]}" \
        -not -path "./logs/*" 2>/dev/null
) | sed 's|^\./||' | awk '{print "  📄 " $0}' >> "$DUMP_FILE"

#################################
# === INPUT FOLDER STRUCTURE ===
#################################
add_section "INPUT FOLDER STRUCTURE"
find input -type d -not -path '*/.*' "${IGNORE_CONDITIONS[@]}" 2>/dev/null | awk '{print "📂 " $0}' >> "$DUMP_FILE"

##################################
# === OUTPUT FOLDER STRUCTURE ===
##################################
add_section "OUTPUT FOLDER STRUCTURE"
find outputs -type d -not -path '*/.*' "${IGNORE_CONDITIONS[@]}" 2>/dev/null | awk '{print "📂 " $0}' >> "$DUMP_FILE"

##################################
# === CONTENT DUMP SECTION ===
##################################
add_section "ALLOWED FILE CONTENTS"
CONTENT_FILES=$(
    set -f
    find . -type f \( "${FIND_CONDITIONS[@]}" \) "${IGNORE_CONDITIONS[@]}" \
        -not -path "*/.*" \
        -not -path "./outputs/*" \
        -not -path "./logs/*" \
        -not -path "./logs/gpt_dump.txt" \
        -not \( -path "./input/*" \( -iname "*.jpg" -o -iname "*.jpeg" \) \) 2>/dev/null
)

debug "Found $(echo "$CONTENT_FILES" | wc -l) files for content dumping"

echo "$CONTENT_FILES" | sort | while read -r file; do
    debug "Processing: $file"
    echo -e "\n### FILE: $file ###\n" >> "$DUMP_FILE"

    if [ -f "$file" ]; then
        head -n 1000 "$file" | iconv -c -t UTF-8//IGNORE >> "$DUMP_FILE" 2>/dev/null
    else
        debug "WARNING: Missing file - $file"
    fi

    echo -e "\n--------------------------------" >> "$DUMP_FILE"

    # Check and enforce size limit
    current_size=$(stat -c%s "$DUMP_FILE" 2>/dev/null || stat -f%z "$DUMP_FILE")
    if [ "$current_size" -ge "$MAX_SIZE" ]; then
        debug "Reached size limit - truncating file"
        truncate -s "$MAX_SIZE" "$DUMP_FILE"
        break
    fi
done

#############################
# === FINAL OUTPUT ===
#############################
if [ -s "$DUMP_FILE" ]; then
    echo -e "\n📋 Export complete! Total size: $(du -h "$DUMP_FILE" | cut -f1)"
    echo "ℹ️ View with: cat $DUMP_FILE"
else
    echo "❌ No valid content collected!"
    exit 1
fi

debug "Script completed successfully"
echo "✅ GPT Helper Script Completed!"
