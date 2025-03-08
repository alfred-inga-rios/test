import unittest
from src.whale_converter import WhaleConverter

class TestWhaleConverter(unittest.TestCase):
    def setUp(self):
        self.converter = WhaleConverter()

    def test_empty_string(self):
        self.assertEqual(self.converter.convert(""), "")

    def test_no_vowels(self):
        self.assertEqual(self.converter.convert("xyz"), "xyz")

    def test_only_vowels(self):
        self.assertEqual(self.converter.convert("aeiou"), "")

    def test_mixed_string(self):
        self.assertEqual(self.converter.convert("hello world"), "hll wrld")

    def test_upper_case_vowels(self):
        self.assertEqual(self.converter.convert("HellO WOrld"), "hll wrld")

if __name__ == '__main__':
    unittest.main()
