# ------------------------------------------------------------------------------- #
# IMPORTS
# ------------------------------------------------------------------------------- #

import os
import json

# ------------------------------------------------------------------------------- #
# FUNCTIONS
# ------------------------------------------------------------------------------- #

def create_directory(directory=""):
    if not os.path.exists(directory):
        try: os.makedirs(directory, exist_ok=True)
        except: pass


def find_files_in_folder(directory="", extension='.json', look_in_sub_dirs=False):
    json_files = []
    if os.path.exists(directory):
        if look_in_sub_dirs:
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.lower().endswith('.json'):
                        json_files.append(os.path.join(root, file))
        else:
            for file in os.listdir(directory):
                if file.lower().endswith(extension):
                    json_files.append(os.path.join(directory, file))
    return json_files


def load_json_to_dict(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File '{json_file_path}' not found")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{json_file_path}'")
        return None
    except Exception as e:
        print(f"An error occurred while loading '{json_file_path}': {e}")
        return None

