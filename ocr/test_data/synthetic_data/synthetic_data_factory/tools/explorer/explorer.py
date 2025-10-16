# synthetic_data_factory/tools/explorer.py
from pathlib import Path
from typing import List

class DirectoryExplorer:
    """
    Provides methods to list immediate subdirectories and files,
    excluding specified names.
    """
    def __init__(self, root: Path, exclude: List[str] = None) -> None:
        self.root = root.resolve()
        self.exclude = set(exclude or ['__pycache__', 'tools'])

    def list_subdirs(self, path: Path = None) -> List[Path]:
        target = path or self.root
        return [p for p in target.iterdir() if p.is_dir() and p.name not in self.exclude]

    def list_files(self, path: Path) -> List[Path]:
        return [p for p in path.iterdir() if p.is_file()]
