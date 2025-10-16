# synthetic_data_factory/tools/manager.py
from typing import Protocol, List, Dict
from tools.scanners import Scanner

class ScanManager:
    """Orchestrates multiple Scanner implementations."""
    def __init__(self, scanners: List[Scanner]) -> None:
        self.scanners = scanners

    def run_scans(self) -> Dict[str, object]:
        """Executes each scanner and returns a mapping of scanner class name to its result."""
        return {
            type(scanner).__name__: scanner.scan()
            for scanner in self.scanners
        }
