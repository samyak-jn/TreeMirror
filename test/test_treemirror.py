import unittest
import os
import subprocess
import shutil
import tempfile


class TestTreeMirror(unittest.TestCase):
    
    def test_valid_input(self):
        # Get the absolute path of the project directory inside the test directory
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'project'))

        # Create temporary output directory
        with tempfile.TemporaryDirectory() as temp_output:
            treemirror_script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'treemirror', 'treemirror.py'))

            # Run treemirror program with valid input and output directories
            subprocess.run(['python', treemirror_script, project_dir, temp_output], check=True)

            # Check if output directory has the same directory structure as the input directory
            expected_dir = project_dir
            for root, dirs, files in os.walk(expected_dir):
                for d in dirs:
                    expected_path = os.path.abspath(os.path.join(root, d))
                    actual_path = os.path.abspath(os.path.join(temp_output, expected_path[len(expected_dir)+1:]))
                    print(f"expected_path: {expected_path}")
                    print(f"actual_path: {actual_path}")
                    self.assertTrue(os.path.isdir(actual_path))
                for f in files:
                    expected_path = os.path.abspath(os.path.join(root, f))
                    actual_path = os.path.abspath(os.path.join(temp_output, expected_path[len(expected_dir)+1:]))
                    print(f"expected_path: {expected_path}")
                    print(f"actual_path: {actual_path}")
                    self.assertTrue(os.path.isfile(actual_path))

        # Print the contents of the output directory
        print("Contents of output directory:")
        for root, dirs, files in os.walk(temp_output):
            for d in dirs:
                print(os.path.join(root, d))
            for f in files:
                print(os.path.join(root, f))

    def test_invalid_input(self):
        # Get the paths of the invalid input directory and the treemirror.py script relative to the test script
        input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'invalid_path'))
        treemirror_script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'treemirror', 'treemirror.py'))
        
        # Run treemirror program with invalid input directory
        output = subprocess.run(['python', treemirror_script, input_dir, 'output/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Check if error message is printed to stdout or stderr
        self.assertIn(b'Error:', output.stdout + output.stderr)


    def test_cancel_overwrite(self):
        # Create temporary output directory with existing file
        temp_output = 'temp_output'
        os.makedirs(temp_output, exist_ok=True)
        with open(os.path.join(temp_output, 'test.txt'), 'w') as f:
            f.write('test')

        # Get the paths of the input directory and the treemirror.py script relative to the test script
        input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'project'))
        treemirror_script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'treemirror', 'treemirror.py'))
        
        # Run treemirror program with input and output directories that would overwrite the file
        proc = subprocess.Popen(['python', treemirror_script, input_dir, temp_output], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # Respond to overwrite prompt with 'n' to cancel
        proc.communicate(b'n\n')

        # Check if the file in the output directory was not overwritten
        with open(os.path.join(temp_output, 'test.txt'), 'r') as f:
            self.assertEqual(f.read(), 'test')

        # Remove temporary output directory
        shutil.rmtree(temp_output)


if __name__ == '__main__':
    unittest.main()
