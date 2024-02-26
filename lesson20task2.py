import unittest
from unittest.mock import patch
import io
import json
import os

class TestTelephoneDirectory(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"First_name": "John", "Last_name": "Doe", "Full_name": "John Doe", "Number": "+1234567890", "city": "New York"},
            {"First_name": "Jane", "Last_name": "Doe", "Full_name": "Jane Doe", "Number": "+1987654321", "city": "Los Angeles"}
        ]
        with open("telephone_test.json", "w") as file:
            json.dump(self.data, file)

    def tearDown(self):
        os.remove("telephone_test.json")

    @patch("builtins.input", side_effect=["1", "John"])
    def test_search_by_first_name(self, mock_input):
        expected_output = "Ось данні про особу що ви просили: \n{'First_name': 'John', 'Last_name': 'Doe', 'Full_name': 'John Doe', 'Number': '+1234567890', 'city': 'New York'}\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            with open("telephone_test.json", "r") as file:
                data = json.load(file)
                for i in data:
                    if i["First_name"] == "John":
                        print("Ось данні про особу що ви просили: ")
                        print(i)
        self.assertEqual(fake_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()