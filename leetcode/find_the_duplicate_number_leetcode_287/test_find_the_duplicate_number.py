import unittest

from find_the_duplicate_number_leetcode_287.find_the_duplicate_number import Solution


class TestFindTheDuplicateNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1 = [1, 3, 4, 2, 2]
        self.data_2 = [3, 1, 3, 4, 2]

    def test_find_the_duplicate_number(self):

        self.assertEqual(self.solution.find_duplicate(self.data_1), 2)
        self.assertEqual(self.solution.find_duplicate(self.data_2), 3)
