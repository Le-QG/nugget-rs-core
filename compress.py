import os
import zipfile

def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

src_folder = 'src'
zip_file = 'pack.zip'

# Get the absolute paths
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
src_folder_path = os.path.join(script_directory, src_folder)
zip_file_path = os.path.join(script_directory, zip_file)

# Zip the folder
zip_folder(src_folder_path, zip_file_path)

print(f'Successfully created {zip_file_path}')
