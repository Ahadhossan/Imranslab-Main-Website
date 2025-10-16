#!/usr/bin/env bash
set -euo pipefail

# Configure logging paths
LOG_DIR="/app/logs/test-runs"
TS=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="${LOG_DIR}/test_run_${TS}.log"

# Initialize directories
mkdir -p "${LOG_DIR}"
# Verify environment
echo "=== Environment Verification ===" | tee -a "${LOG_FILE}"
{
    python -c "import cv2; print(f'OpenCV version: {cv2.__version__}')"
    pip list
    pip check
} | tee -a "${LOG_FILE}"

# Ensure we’re only running tests from preprocess/tests/
echo -e "\n=== Starting test run at $(date) ===" | tee -a "${LOG_FILE}"

# Run pytest only on tests from preprocess/tests
pytest tests/ \
    --maxfail=100 \
    --disable-warnings \
    --tb=short \
    --no-cov \
    --junitxml="${LOG_DIR}/junit_${TS}.xml" \
    -n auto \
    -rs \
    2>&1 | tee -a "${LOG_FILE}"

# Finalize logs
EXIT_CODE=${PIPESTATUS[0]}
echo -e "\n=== Test run completed with exit code: ${EXIT_CODE} ===" | tee -a "${LOG_FILE}"
cp -r /app/logs/htmlcov "${LOG_DIR}/htmlcov_${TS}" 2>/dev/null || true
exit ${EXIT_CODE}
