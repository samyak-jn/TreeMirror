# TreeMirror
TreeMirror is a Python program that creates a mirrored copy of a directory structure, allowing users to easily duplicate and transfer directory trees.

## Requirements

To run TreeMirror, you will need to have Python 3.x installed on your machine. You can check if you have Python installed by running the following command in your terminal:

``
python --version
``

## Installation

To install TreeMirror, you can simply clone this repository to your local machine:

``
git clone https://github.com/samyak-jn/treemirror.git
``

Once cloned, you can navigate to the `treemirror` directory and install the program's dependencies using the following command:

``
pip install -r requirements.txt
``

## Usage

To use TreeMirror, you can run the program using the following command:

``
python treemirror/treemirror.py <input_directory> <output_directory>
``

- `<input_directory>`: the path to the directory structure to be copied.
- `<output_directory>`: the path to the directory where the copy will be created.

Replace `<input_directory>` with the path to the directory whose structure you want to mirror, and `<output_directory>` with the path to the directory where you want to create the mirrored copy.

If the `<output_directory>` already exists, the program will ask if you want to overwrite its contents.

When the program is run, it will first display a CLI interface to visualize the directory structure of the input directory. The interface will show each directory as a node, with the parent directories above the child directories. Each node will be indented to indicate its level in the directory hierarchy.

After displaying the directory structure, the program will prompt the user to confirm if they want to overwrite the files in the output directory. If the user confirms, the program will create a copy of the input directory structure in the output directory. If the output directory already exists, the program will ask the user if they want to overwrite the files in the directory.

## Testing

To run the unit tests for TreeMirror, navigate to the `test` directory and run the following command:

``
python -m unittest
``

## License

TreeMirror is licensed under the MIT License. See the `LICENSE` file for more information.
