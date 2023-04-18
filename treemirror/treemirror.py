import os
import argparse
import shutil
from tqdm import tqdm

def main():
    parser = argparse.ArgumentParser(description="Mirror the directory structure of a source directory to a destination directory.")
    parser.add_argument('path', type=str, help='path to project directory')
    parser.add_argument('output_path', type=str, help='path to output directory')
    args = parser.parse_args()

    # Check if input directory exists
    if not os.path.isdir(args.path):
        print(f"Error: {args.path} is not a directory.")
        return

    # Check if output directory exists; create it if it doesn't
    if not os.path.isdir(args.output_path):
        os.makedirs(args.output_path)
    else:
        # Prompt user before overwriting files
        overwrite = input(f"{args.output_path} already exists. Overwrite files? (y/n): ")
        if overwrite.lower() != 'y':
            return

    # Process directory structure
    process_directory_structure(args.path)

    # Ask user if they want to copy the directory structure to the specified output directory
    copy_structure = input("Do you want to copy this structure to the specified output directory? (y/n): ")
    if copy_structure.lower() == 'y':
        copy_dir_structure(args.path, args.output_path)
        print(f"Directory structure copied to {args.output_path}.")

def process_directory_structure(path):
    print(f"Directory structure of {path}:")
    print_directory_structure(path, 0)

def print_directory_structure(path, indent=0):
    for file in os.listdir(path):
        print(f"{' ' * indent}- {file}")
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path):
            print_directory_structure(full_path, indent + 2)

def copy_dir_structure(src_dir, dst_dir, prompt_overwrite=True):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    files = os.listdir(src_dir)
    for item in tqdm(files, desc='Copying directory structure', unit='file'):
        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dst_dir, item)

        if os.path.isdir(src_path):
            copy_dir_structure(src_path, dst_path, prompt_overwrite)
        else:
            if os.path.exists(dst_path) and prompt_overwrite:
                overwrite = input(f"Do you want to overwrite {dst_path}? (y/n): ")
                if overwrite.lower() == "n":
                    continue
            shutil.copy2(src_path, dst_path)

if __name__ == '__main__':
    main()
