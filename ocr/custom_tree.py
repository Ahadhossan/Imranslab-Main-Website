# import os
# from pathlib import Path

# def generate_tree(
#     root_path: str,
#     exclude_dirs: list = None,
#     exclude_extensions: list = None,
#     prefix: str = ""
# ):
#     exclude_dirs = set(exclude_dirs or [])
#     exclude_extensions = set(exclude_extensions or [])

#     entries = sorted(Path(root_path).iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
#     entries = [e for e in entries if not (e.is_dir() and e.name in exclude_dirs)]

#     for i, entry in enumerate(entries):
#         connector = "└── " if i == len(entries) - 1 else "├── "
#         path_str = prefix + connector + entry.name

#         if entry.is_file():
#             if entry.suffix in exclude_extensions:
#                 continue
#             print(path_str)
#         elif entry.is_dir():
#             print(path_str)
#             new_prefix = prefix + ("    " if i == len(entries) - 1 else "│   ")
#             generate_tree(entry, exclude_dirs, exclude_extensions, new_prefix)

# # Example usage
# if __name__ == "__main__":
#     ROOT_DIR = "."  # Change to your root directory
#     EXCLUDED_DIRS = {"__pycache__", ".git", "node_modules", 'venv', '.venv', }
#     EXCLUDED_EXTENSIONS = {".log", ".pyc", ".tmp"}

#     print(f"{ROOT_DIR}")
#     generate_tree(ROOT_DIR, exclude_dirs=EXCLUDED_DIRS, exclude_extensions=EXCLUDED_EXTENSIONS)





import os
from pathlib import Path

def generate_tree(
    root_path: str,
    exclude_dirs: set = None,
    exclude_extensions: set = None,
    exclude_files: set = None,
    prefix: str = ""
):
    exclude_dirs = exclude_dirs or set()
    exclude_extensions = exclude_extensions or set()
    exclude_files = exclude_files or set()

    try:
        entries = sorted(Path(root_path).iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    except PermissionError:
        print(prefix + "└── [Permission Denied]")
        return

    entries = [e for e in entries if not (e.is_dir() and e.name in exclude_dirs)]

    for i, entry in enumerate(entries):
        if entry.is_file():
            if entry.name in exclude_files:
                continue
            if entry.suffix in exclude_extensions:
                continue

        connector = "└── " if i == len(entries) - 1 else "├── "
        path_str = prefix + connector + entry.name

        print(path_str)

        if entry.is_dir():
            new_prefix = prefix + ("    " if i == len(entries) - 1 else "│   ")
            generate_tree(entry, exclude_dirs, exclude_extensions, exclude_files, new_prefix)

# Example usage
if __name__ == "__main__":
    ROOT_DIR = "."  # Set your project root path here
    EXCLUDED_DIRS = {"__pycache__", ".git", "venv", "node_modules", 'venv', '.venv', '.pytest_cache', 'errors'}
    EXCLUDED_EXTENSIONS = {".log", ".pyc", ".tmp", ".ipynb"}
    EXCLUDED_FILES = {"secrets.txt", ".env", "debug.log", "custom_tree.py"}

    print(f"{ROOT_DIR}")
    generate_tree(
        ROOT_DIR,
        exclude_dirs=EXCLUDED_DIRS,
        exclude_extensions=EXCLUDED_EXTENSIONS,
        exclude_files=EXCLUDED_FILES
    )
