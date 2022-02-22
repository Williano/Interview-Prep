import unittest

from plus_one_leetcode_66.plus_one import Solution


class TestValidPalindrome(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1 = [1, 2, 3]
        self.data_2 = [4, 3, 2, 1]
        self.data_3 = [9]

    def test_valid_palindrome(self):

        self.assertEqual(self.solution.plus_one(self.data_1), [1, 2, 4])
        self.assertEqual(self.solution.plus_one(self.data_2), [4, 3, 2, 2])
        self.assertEqual(self.solution.plus_one(self.data_3), [1, 0])
