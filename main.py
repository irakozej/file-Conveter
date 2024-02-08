import os
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    folder_name = os.path.basename(folder_path)
    date_today = datetime.today().strftime('%Y_%m_%d')
    compressed_filename = f"{folder_name}_{date_today}.{compress_type}"

    try:
        if compress_type == 'zip':
            with zipfile.ZipFile(compressed_filename, 'w') as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))
        elif compress_type == 'tar':
            with tarfile.open(compressed_filename, 'w') as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        elif compress_type == 'tgz':
            with tarfile.open(compressed_filename, 'w:gz') as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        else:
            print("Invalid compression type. Please choose either 'zip', 'tar', or 'tgz'.")
            return

        print(f"Compression successful! File saved as: {compressed_filename}")
    except Exception as e:
        print(f"Compression failed. Error: {str(e)}")

def main():
    folder_path = input("Enter the path of the folder to compress: ")
    
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return
    
    print("Available compressed file types:")
    print("1. Zip (.zip)")
    print("2. Tar (.tar)")
    print("3. Tar Gzip (.tgz)")

    choice = input("Enter the number corresponding to your preferred compression type: ")

    if choice == '1':
        compress_type = 'zip'
    elif choice == '2':
        compress_type = 'tar'
    elif choice == '3':
        compress_type = 'tgz'
    else:
        print("Invalid choice.")
        return

    compress_folder(folder_path, compress_type)

if __name__ == "__main__":
    main()
