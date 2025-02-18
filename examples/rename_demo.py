import os

from dotenv import load_dotenv

from src.file import rename_file, retrieve_files

if __name__ == "__main__":
    load_dotenv()
    PATH = os.getenv("FOLDER_PATH")
    EXT = os.getenv("EXTENSIONS")
    NAME = os.getenv("NAME_FORMAT")

    files = retrieve_files(PATH, EXT)
    for file in files:
        file_name = os.path.basename(file)
        is_success = rename_file(file, NAME, EXT)
        if not is_success:
            print(f"[WARNING] {file_name} failed to rename!")
        else:
            print(f"[INFO] {file_name} success to rename!")
