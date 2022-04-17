import unittest
from generate_string_from_palindrome.generate_string_from_palindrome import Solution


class TestGeneratePalindrome(unittest.TestCase):
    def setUp(self) -> None:
        self.test = Solution()
        self.data_1 = "AAAACACBA"
        self.data_2 = "RARARARARA"
        self.data_3 = "A"

    def test_generate_palindrome(self):

        self.assertEqual(self.test.generate_palindrome(self.data_1), "AAACBCAAA")
        self.assertEqual(self.test.generate_palindrome(self.data_2), None)
        self.assertEqual(self.test.generate_palindrome(self.data_3), "A")
