import unittest
import os

from lesson21task1 import FileContextManager

class TestFileContextManager(unittest.TestCase):
    def setUp(self):
        self.filename = "test_file.txt"
        self.file_content = "Hello, World!"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_file_writing(self):
        with FileContextManager(self.filename, 'w') as f:
            f.write(self.file_content)

        with open(self.filename, 'r') as f:
            content = f.read()
            self.assertEqual(content, self.file_content)

    def test_file_appending(self):
        existing_content = "Existing content."
        with open(self.filename, 'w') as f:
            f.write(existing_content)

        additional_content = "\nAdditional content."
        with FileContextManager(self.filename, 'a') as f:
            f.write(additional_content)

        with open(self.filename, 'r') as f:
            content = f.read()
            expected_content = existing_content + additional_content
            self.assertEqual(content, expected_content)

    def test_file_reading(self):
        with open(self.filename, 'w') as f:
            f.write(self.file_content)

        with FileContextManager(self.filename, 'r') as f:
            content = f.read()
            self.assertEqual(content, self.file_content)


if __name__ == '__main__':
    unittest.main()