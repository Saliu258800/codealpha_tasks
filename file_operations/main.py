import os
import shutil 

def get_files(path):
    return os.listdir(path)

def main():
    src = input("Enter the directory of your .jpg files: ")
    dest = input("Enter the directory to your destination folder: ")

    os.makedirs(dest, exist_ok=True)

    try:
        for file in get_files(src):
            if file.lower().endswith(".jpg"):
                src_file = os.path.join(src, file)
                dest_file = os.path.join(dest, file)
                shutil.move(src_file, dest_file)
                print(f"{file} successfully moved to {dest}")
    except Exception as e:
        print(f"{e}: unexpected error")
    
if __name__ == "__main__":
    main()