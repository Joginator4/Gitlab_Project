import os
import unittest
import xmlrunner
class TestCurrentFolder(unittest.TestCase):
    
    def test_files_in_current_folder(self):
        # Get the list of files in the current folder
        files = os.listdir('.')
        # Check if the list is not empty
        self.assertGreater(len(files), 0, "Unit test completed successfully !")

if __name__ == '__main__':
    print("Running tests...", "\n")
       
    unittest.main()