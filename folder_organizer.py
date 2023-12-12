import os
import shutil
import hashlib

def file_hash(filename):
    """ Generate MD5 hash of a file """
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def delete_duplicates(directory):
    """ Delete duplicate files in a given directory """
    hashes = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            filehash = file_hash(filepath)
            if filehash in hashes:
                os.remove(filepath)
                print(f"Duplicate file {filename} deleted.")
            else:
                hashes[filehash] = filename

def sort_files_by_type(directory):
    """
    Sort files in the given directory into subfolders based on file extensions.
    If a NotADirectoryError occurs, delete the file.

    Args:
    directory (str): Path to the directory where files are to be sorted.
    """
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_extension = filename.split('.')[-1].lower()
            folder_name = os.path.join(directory, file_extension)

            try:
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                shutil.move(filepath, os.path.join(folder_name, filename))
                print(f"Moved {filename} to {folder_name}/")
            except NotADirectoryError:
                os.remove(filepath)
                print(f"Not a directory. Deleted file: {filename}")

# Define the paths to your Desktop, Downloads, and Documents folders
desktop_folder = "/Users/jude/Desktop"
downloads_folder = "/Users/jude/Downloads"
documents_folder = "/Users/jude/Documents"

# Process each folder
for folder in [desktop_folder, downloads_folder, documents_folder]:
    delete_duplicates(folder)
    sort_files_by_type(folder)
    print(f"Processed files in {folder}")

