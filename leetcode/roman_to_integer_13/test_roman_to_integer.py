import unittest

from roman_to_integer_13.roman_to_integer import Solution


class TestValidPalindrome(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1 = "III"
        self.data_2 = "LVIII"
        self.data_3 = "MCMXCIV"

    def test_valid_palindrome(self):

        self.assertEqual(self.solution.roman_to_int(self.data_1), 3)
        self.assertEqual(self.solution.roman_to_int(self.data_2), 58)
        self.assertEqual(self.solution.roman_to_int(self.data_3), 1994)
