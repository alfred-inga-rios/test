import unittest
from app.main import main

class TestMain(unittest.TestCase):
    
    def test_main_function(self):
        # Assuming the main function returns a value, replace 'expected_value' with the actual expected output
        expected_value = "Hello, World!"  # Example expected output
        result = main()
        self.assertEqual(result, expected_value)

if __name__ == '__main__':
    unittest.main()