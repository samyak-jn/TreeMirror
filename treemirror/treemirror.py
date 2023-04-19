import os
import shutil

from tqdm import tqdm


def process_dir_struct(path):
    print(f"Directory structure of {path}:")
    print_dir_struct(path, 0)


def print_dir_struct(path, indent=0):
    for file in os.listdir(path):
        print(f"{' ' * indent}- {file}")
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path):
            print_dir_struct(full_path, indent + 2)


def copy_dir_struct(src_dir, dst_dir, prompt_overwrite=True):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    files = os.listdir(src_dir)
    for item in tqdm(files, desc="Copying directory structure", unit="file"):
        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dst_dir, item)

        if os.path.isdir(src_path):
            copy_dir_struct(src_path, dst_path, prompt_overwrite)
        else:
            if os.path.exists(dst_path) and prompt_overwrite:
                overwrite = input(f"Do you want to overwrite {dst_path}? (y/n): ")
                if overwrite.lower() == "n":
                    continue
            shutil.copy2(src_path, dst_path)
