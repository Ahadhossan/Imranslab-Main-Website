#!/bin/bash
set -ex

CONSOLE_LOG="logs/test-runs/console_output.txt"
SKIPPED_OUT="ci/skipped_tests/skipped_tests.txt"

# Ensure directories exist with proper permissions
mkdir -p $(dirname "${SKIPPED_OUT}") $(dirname "${CONSOLE_LOG}")
chmod -R 777 logs ci

echo "=== Environment Verification ==="
echo "Workspace contents:"
ls -l
echo "Log directory contents:"
ls -l logs

echo "=== Checking Console Output ==="
if [ ! -f "${CONSOLE_LOG}" ]; then
    echo "❌ ERROR: Missing console log at ${CONSOLE_LOG}"
    echo "Directory contents:"
    ls -R logs || true
    exit 1
fi

echo "=== Extracting Skipped Tests ==="
awk '
    /=========================== short test summary info ============================/ {flag=1}
    flag {print}
    /==== .* passed, .* skipped, .* warnings in .* ====/ {if(flag){exit}}
' "${CONSOLE_LOG}" > "${SKIPPED_OUT}"

echo "=== Extraction Results ==="
if [ -s "${SKIPPED_OUT}" ]; then
    echo "📋 Found skipped tests:"
    cat "${SKIPPED_OUT}"
else
    echo "✅ No skipped tests detected"
    echo "No skipped tests found at $(date)" > "${SKIPPED_OUT}"
fi