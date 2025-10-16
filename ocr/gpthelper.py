import os
from pathlib import Path

class GPTHelper:
    def __init__(self,
                 root_dir: str,
                 output_file: str = "gpt_dump.txt",
                 allowed_extensions=None,
                 disallowed_extensions=None,
                 disallowed_folders=None,
                 disallowed_filenames=None,
                 max_file_size_kb: int = 512):
        self.root_dir = Path(root_dir).resolve()
        self.output_file = Path(output_file).resolve()
        self.allowed_extensions = set(allowed_extensions or [])
        self.disallowed_extensions = set(disallowed_extensions or [])
        self.disallowed_folders = set(disallowed_folders or [])
        self.disallowed_filenames = set(disallowed_filenames or [])
        self.max_file_size_kb = max_file_size_kb

    def is_allowed(self, file_path: Path) -> bool:
        if file_path.suffix and self.allowed_extensions and file_path.suffix not in self.allowed_extensions:
            return False
        if file_path.suffix in self.disallowed_extensions:
            return False
        if file_path.name in self.disallowed_filenames:
            return False
        if any(part in self.disallowed_folders for part in file_path.parts):
            return False
        if file_path.stat().st_size > self.max_file_size_kb * 1024:
            return False
        return True

    def get_folder_tree(self) -> str:
        tree_lines = []

        for root, dirs, files in os.walk(self.root_dir):
            # Filter disallowed folders
            dirs[:] = [d for d in dirs if d not in self.disallowed_folders]

            level = root.replace(str(self.root_dir), '').count(os.sep)
            indent = '│   ' * level + '├── '
            tree_lines.append(f"{indent}{os.path.basename(root)}/")

            for f in sorted(files):
                path = Path(root) / f
                if self.is_allowed(path):
                    file_indent = '│   ' * (level + 1) + '└── '
                    tree_lines.append(f"{file_indent}{f}")

        return "\n".join(tree_lines)

    def get_file_dump(self) -> str:
        dump_lines = []
        for root, _, files in os.walk(self.root_dir):
            for f in sorted(files):
                file_path = Path(root) / f
                if self.is_allowed(file_path):
                    rel_path = file_path.relative_to(self.root_dir)
                    dump_lines.append(f"\n\n### FILE: {rel_path}\n")
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                            content = file.read().strip()
                            dump_lines.append(content if content else "[EMPTY FILE]")
                    except Exception as e:
                        dump_lines.append(f"[ERROR READING FILE: {e}]")
        return "\n".join(dump_lines)

    def generate_output(self):
        with open(self.output_file, 'w', encoding='utf-8') as out_file:
            out_file.write("===== 📁 FOLDER STRUCTURE =====\n")
            out_file.write(self.get_folder_tree())
            out_file.write("\n\n===== 📄 FILE CONTENT DUMP =====\n")
            out_file.write(self.get_file_dump())

        print(f"\n✅ GPT helper dump created: {self.output_file}")

# ------------------------ USAGE ------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="GPT Helper: Dump folder tree and file contents.")
    parser.add_argument("root_dir", help="Root directory to scan")
    parser.add_argument("--output", default="gpt_dump.txt", help="Output text file")
    parser.add_argument("--allowed", nargs='*', default=[".py", ".sh", ".txt", ".yml", ".yaml", ".md"],
                        help="Allowed file extensions")
    parser.add_argument("--disallowed_ext", nargs='*', default=[".log", ".zip"],
                        help="Disallowed file extensions")
    parser.add_argument("--disallowed_folders", nargs='*', default=["__pycache__", ".git", "venv", "node_modules"],
                        help="Folder names to skip")
    parser.add_argument("--disallowed_files", nargs='*', default=["secrets.py", ".DS_Store"],
                        help="Exact file names to skip")
    parser.add_argument("--max_kb", type=int, default=512, help="Maximum file size (KB) to include")

    args = parser.parse_args()

    helper = GPTHelper(
        root_dir=args.root_dir,
        output_file=args.output,
        allowed_extensions=set(args.allowed),
        disallowed_extensions=set(args.disallowed_ext),
        disallowed_folders=set(args.disallowed_folders),
        disallowed_filenames=set(args.disallowed_files),
        max_file_size_kb=args.max_kb
    )
    helper.generate_output()
