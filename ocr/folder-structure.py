import os

def list_folder_structure(base_dir, ignore_file_types=None, ignore_folders=None, file_limit=30, file_list_only=False, folder_list_only=False, output_file="folder_structure.txt"):
    """
    Recursively lists the folder structure, showing up to 5 files per folder and including subfolders.
    The output is saved into a text file.

    Parameters:
        base_dir (str): The root directory to start listing from.
        ignore_file_types (list): A list of file extensions to ignore (e.g., ['.py', '.txt']).
        ignore_folders (list): A list of folder names to ignore (e.g., ['__pycache__', 'node_modules']).
        file_limit (int): Maximum number of files to show per folder.
        file_list_only (bool): If True, only files will be shown, no folders.
        folder_list_only (bool): If True, only folders will be shown, no files.
        output_file (str): The path of the output text file where the structure will be saved.
    """
    if ignore_file_types is None:
        ignore_file_types = []
    if ignore_folders is None:
        ignore_folders = []

    def is_valid_file(file):
        return not any(file.endswith(ext) for ext in ignore_file_types)

    def is_valid_folder(folder):
        return folder not in ignore_folders

    def recursive_list(path, depth=0):
        # Open the file in append mode to write the output
        with open(output_file, "a") as file_out:
            # Print the folder path to file
            file_out.write('  ' * depth + f"Folder: {path}\n")

            if not folder_list_only:
                files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and is_valid_file(f)]
                # Display up to 'file_limit' files
                for i, file in enumerate(files[:file_limit]):
                    file_out.write('  ' * (depth + 1) + f"File: {file}\n")

            if not file_list_only:
                # Recurse into subdirectories, but ignore folders in the ignore list
                subfolders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f)) and is_valid_folder(f)]
                for subfolder in subfolders:
                    recursive_list(os.path.join(path, subfolder), depth + 1)

    # Start the recursive listing from the base directory and write to file
    with open(output_file, "w") as file_out:
        file_out.write(f"Folder structure of {base_dir}:\n")
    recursive_list(base_dir)

# Example usage
base_directory = "."  # Replace with the folder you want to list
ignore_types = ['.py', '.txt']  # You can specify the file types to ignore
ignore_folders = ['__pycache__', 'node_modules', 'venv', '.venv']  # Specify folders to ignore
list_folder_structure(base_directory, ignore_file_types=ignore_types, ignore_folders=ignore_folders, file_limit=30, output_file="folder_structure.txt")
