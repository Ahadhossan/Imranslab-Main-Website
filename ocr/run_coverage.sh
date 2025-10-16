#!/usr/bin/env bash
set -euo pipefail

LOG_DIR="/app/logs/test-runs"
COV_HTML_DIR="${LOG_DIR}/htmlcov"
COV_XML_FILE="${LOG_DIR}/coverage.xml"

TS=$(date +"%Y%m%d_%H%M%S")

# Prepare dirs
mkdir -p "${COV_HTML_DIR}" /app/outputs

echo "=== Run Environment ==="
python -V
pip list

# Run tests with coverage
pytest tests/ \
  --cov=preprocessing_image \
  --cov=ocr_processing \
  --cov=test_data \
  --cov=performance \
  --cov-report=term \
  --cov-report=html:"${COV_HTML_DIR}" \
  --cov-report=xml:"${COV_XML_FILE}" \
  --junitxml="${LOG_DIR}/junit_${TS}.xml" \
  -n auto
