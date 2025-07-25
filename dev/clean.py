import os
import shutil


def clean_cache_files():
    print("< Cleaning.... >")
    for root, dirs, files in os.walk(".", topdown=False):
        for file in files:
            if file.endswith(".pyc") or file.endswith(".blend1"):
                path = os.path.join(root, file)
                print(f"Del File : {path}")
                os.remove(path)
        for directory in dirs:
            if directory == "__pycache__":
                path = os.path.join(root, directory)
                print(f"Del Dir  : {path}")
                shutil.rmtree(path)
clean_cache_files()

