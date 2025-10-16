#!/bin/bash

REPORT_DIR="/app/scripts/test_reports"
FINAL_REPORT="$REPORT_DIR/combined_test_report.html"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

# Backup old reports
echo "📝 Backing up old reports..."
mkdir -p "$REPORT_DIR/old_reports"
mv "$REPORT_DIR"/*.html "$REPORT_DIR/old_reports/" 2>/dev/null

# Merge reports using pytest-html extras
echo "🔄 Merging reports..."
echo "<html><head><title>Combined Test Report</title></head><body>" > "$FINAL_REPORT"
for report in "$REPORT_DIR"/*.html; do
  echo "<h2>Report: $(basename "$report")</h2>" >> "$FINAL_REPORT"
  cat "$report" | sed '1,4d' >> "$FINAL_REPORT"  # Skip HTML headers to prevent conflicts
done
echo "</body></html>" >> "$FINAL_REPORT"

# Move old reports to archive
mv "$REPORT_DIR/old_reports" "$REPORT_DIR/old_reports_$TIMESTAMP"
echo "✅ Final combined report saved at: $FINAL_REPORT"
