# synthetic_data_factory/tools/collector.py
# !/usr/bin/env python3
"""
Collector endpoint for scanning synthetic_data_factory structure.
Provides a single function 'collect_metadata' that returns all scan results.
"""
import sys
from pathlib import Path
from typing import Dict

# Ensure synthetic_data_factory is on sys.path so 'tools' package can be imported
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.validators import DirectoryValidator
from tools.explorer import DirectoryExplorer
from tools.scanners import (
    TopLevelScanner,
    SubfolderMappingScanner,
    NestedSubfolderScanner,
    FileListingScanner,
)
from tools.manager import ScanManager


def collect_metadata(base_dir: Path = None) -> Dict[str, object]:
    """
    Scans the synthetic_data_factory directory structure and returns results.

    :param base_dir: Path to the synthetic_data_factory folder. If None, uses default.
    :return: dict mapping scanner names to scan results.
    """
    base = Path(base_dir) if base_dir else Path(__file__).parent.parent
    DirectoryValidator(base)

    explorer = DirectoryExplorer(base, exclude=['__pycache__', 'tools'])
    scanners = [
        TopLevelScanner(explorer),
        SubfolderMappingScanner(explorer),
        NestedSubfolderScanner(explorer),
        FileListingScanner(explorer),
    ]
    manager = ScanManager(scanners)
    return manager.run_scans()


if __name__ == "__main__":
    import pprint

    results = collect_metadata()
    pprint.pprint(results)
