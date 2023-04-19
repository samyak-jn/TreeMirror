import os
import argparse
from treemirror.treemirror import process_directory_structure,copy_dir_structure

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


if __name__ == '__main__':
    main()
