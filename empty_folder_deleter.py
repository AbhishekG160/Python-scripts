import os

def delete_empty_folders(folder_path):
    # Traverse dir tree in bottom-up
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                if not os.listdir(dir_path):  # Check if folder empty
                    os.rmdir(dir_path)
                    print(f"Deleted empty folder: {dir_path}")
            except Exception as e:
                print(f"Error deleting {dir_path}: {e}")

target_folder = r"F:\files"

delete_empty_folders(target_folder)
