import os
import shutil

def get_unique_filename(dest_folder, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(dest_folder, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    return new_filename

def merge_folders(source_folders, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for folder in source_folders:
        for root, _, files in os.walk(folder):
            for file in files:
                src_file = os.path.join(root, file)
                unique_name = get_unique_filename(destination_folder, file)
                dest_file = os.path.join(destination_folder, unique_name)
                shutil.copy2(src_file, dest_file)
                print(f"Copied: {src_file} → {dest_file}")

# === Usage Example ===
source_dirs = [
    r"C:\Path\To\Folder1",
    r"C:\Path\To\Folder2",
    r"C:\Path\To\Folder3"
]
destination_dir = r"C:\Path\To\MergedFolder"

merge_folders(source_dirs, destination_dir)
