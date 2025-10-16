# synthetic_data_factory/tools/validators.py
from pathlib import Path

class DirectoryValidator:
    """Validates that a path exists and is a directory."""
    def __init__(self, path: Path) -> None:
        if not path.exists() or not path.is_dir():
            raise ValueError(f"Not a directory: {path}")
        self.path = path.resolve()
