
###############################

import os
import shutil

EXTENSIONS = {
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.mp3': 'Audio',
    '.mp4': 'Videos',
    '.zip': 'Archives',
    '.py': 'Scripts',
    '.js': 'Scripts',
}

def organize_folder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            fname, ext = os.path.splitext(file)
            folder = EXTENSIONS.get(ext.lower(), 'Others')
            target = os.path.join(folder_path, folder)

            os.makedirs(target, exist_ok=True)
            shutil.move(file_path, os.path.join(target, file))
            print(f"'{file}' moved to '{folder}' folder.")

folder = input("Enter folder path to organize: ").strip()
try:
    organize_folder(folder)
except FileNotFoundError:
    print('file not found!!!')

##############################

