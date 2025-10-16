# synthetic_data_factory/tools/scanners.py
from typing import List, Dict, Protocol
from ..explorer.explorer import DirectoryExplorer # importing from current directory

class Scanner(Protocol):
    """
    Protocol for scanner classes that collect information from a directory.
    """
    def scan(self) -> object:
        ...

class TopLevelScanner:
    """Scans for immediate subdirectory names under root."""
    def __init__(self, explorer: DirectoryExplorer) -> None:
        self.explorer = explorer

    def scan(self) -> List[str]:
        return [d.name for d in self.explorer.list_subdirs()]

class SubfolderMappingScanner:
    """Scans each top-level folder for its immediate subfolders."""
    def __init__(self, explorer: DirectoryExplorer) -> None:
        self.explorer = explorer

    def scan(self) -> Dict[str, List[str]]:
        result: Dict[str, List[str]] = {}
        for top in self.explorer.list_subdirs():
            names = [sub.name for sub in self.explorer.list_subdirs(top)]
            result[top.name] = sorted(names)
        return result

class NestedSubfolderScanner:
    """Scans two levels deep: top-level → subfolders → their subfolders."""
    def __init__(self, explorer: DirectoryExplorer) -> None:
        self.explorer = explorer

    def scan(self) -> Dict[str, Dict[str, List[str]]]:
        result: Dict[str, Dict[str, List[str]]] = {}
        for top in self.explorer.list_subdirs():
            sub_map: Dict[str, List[str]] = {}
            for sub in self.explorer.list_subdirs(top):
                names = [lvl.name for lvl in self.explorer.list_subdirs(sub)]
                sub_map[sub.name] = sorted(names)
            result[top.name] = sub_map
        return result

class FileListingScanner:
    """Scans for files inside each subfolder, excluding '__init__.py'."""
    def __init__(self, explorer: DirectoryExplorer) -> None:
        self.explorer = explorer

    def scan(self) -> Dict[str, Dict[str, List[str]]]:
        result: Dict[str, Dict[str, List[str]]] = {}
        for top in self.explorer.list_subdirs():
            file_map: Dict[str, List[str]] = {}
            for sub in self.explorer.list_subdirs(top):
                files = [f.name for f in self.explorer.list_files(sub) if f.name != '__init__.py']
                file_map[sub.name] = sorted(files)
            result[top.name] = file_map
        return result

