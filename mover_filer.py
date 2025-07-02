import os
import shutil
# just changing the shutil.copy2 to shutil.move 
# this deleted the files after copying 

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
                shutil.move(src_file, dest_file)  # this is just the changed part of the code 
                print(f"Moved: {src_file} → {dest_file}")

source_dirs = [
    r"E:\New folder\#Yuru Camp △ Pictures, Images on pixiv, Japan",
    r"E:\New folder\#2Yuru Camp △ Pictures, Comics on pixiv, Japan",
    r"E:\New folder\girl, Yuru Camp △, Rin Shima ゆるキャン△アニメ２期＆劇場版おめでとう！！ - pixiv",
    r"E:\New folder\#Yuru Camp △ - OmegaΩTest's illustrations - pixiv",
    r"E:\New folder\#1Yuru Camp △ Pictures, Comics on pixiv, Japan",
    r"E:\New folder\#Yuru Camp △ Pictures, Comics on pixiv, Japan"
]

destination_dir = r"E:\New folder\#Yuru Camp △ Pictures, Comics on pixiv, Japan"
merge_folders(source_dirs, destination_dir)
