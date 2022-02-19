import unittest

from valid_palindrome_125.valid_palindrome import Solution


class TestValidPalindrome(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1 = "A man, a plan, a canal: Panama"
        self.data_2 = "race a car"
        self.data_3 = " "

    def test_valid_palindrome(self):

        self.assertEqual(self.solution.is_palindrome(self.data_1), True)
        self.assertEqual(self.solution.is_palindrome(self.data_2), False)
        self.assertEqual(self.solution.is_palindrome(self.data_3), False)
