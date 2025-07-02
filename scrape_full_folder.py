import os
import shutil
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}

def move_images(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, _, files in os.walk(source_folder):
        for file in files:
            if os.path.splitext(file)[1].lower() in IMAGE_EXTENSIONS:
                src_path = os.path.join(root, file)
                dest_path = os.path.join(destination_folder, file)

                #dupe names
                counter = 1
                base, ext = os.path.splitext(file)
                while os.path.exists(dest_path):
                    dest_path = os.path.join(destination_folder, f"{base}_{counter}{ext}")
                    counter += 1
                # final moving
                shutil.move(src_path, dest_path)
                print(f"Moved: {src_path} → {dest_path}")

source_dir = r"F:\files\DCIM"
destination_dir = r"F:\files\DCIM"

move_images(source_dir, destination_dir)
