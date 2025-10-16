#!/bin/bash

# Get the script's directory (assumes this script is inside 'scripts/')
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Ensure the script runs from the project root
cd "$PROJECT_ROOT" || { echo "Failed to switch to project root: $PROJECT_ROOT"; exit 1; }

# Set up test reports directory
REPORT_DIR="$PROJECT_ROOT/scripts/test_reports"

# Remove old reports to keep the folder clean
rm -rf "$REPORT_DIR"/*

# Ensure the report directory exists
mkdir -p "$REPORT_DIR"

# Generate a structured filename for easy comparison
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
REPORT_NAME="test_report_$TIMESTAMP"
LOG_FILE="$REPORT_DIR/${REPORT_NAME}.log"
HTML_REPORT="$REPORT_DIR/${REPORT_NAME}.html"

# Activate virtual environment if exists
if [ -d "$PROJECT_ROOT/.venv" ]; then
    source "$PROJECT_ROOT/.venv/bin/activate"
    echo "✅ Activated virtual environment"
else
    echo "⚠️ Warning: Virtual environment not found. Ensure dependencies are installed globally."
fi

# Debugging: Show current directory and virtual environment
echo "📂 Current Directory: $(pwd)"
echo "🐍 Python Path: $(which python)"
echo "📝 Running Tests in: instructor/tests, jira_integration/tests, university/tests"

# Run pytest for all test directories explicitly with verbose output
pytest "$PROJECT_ROOT/instructor/tests" \
       "$PROJECT_ROOT/jira_integration/tests" \
       "$PROJECT_ROOT/university/tests" \
       --html="$HTML_REPORT" --self-contained-html | tee "$LOG_FILE"

# Display report location
echo "✅ Pytest report generated at: $HTML_REPORT"
echo "📝 Log file stored at: $LOG_FILE"

# Execute additional script after tests complete
POST_TEST_SCRIPT="$SCRIPT_DIR/project_code_dump.sh"

if [ -f "$POST_TEST_SCRIPT" ]; then
    echo "🔄 Executing post-test actions..."
    bash "$POST_TEST_SCRIPT"
else
    echo "⚠️ No post-test script found at $POST_TEST_SCRIPT"
fi

# Deactivate virtual environment if activated
if [[ "$VIRTUAL_ENV" != "" ]]; then
    deactivate
    echo "🚪 Deactivated virtual environment"
fi
