import unittest

from single_number_II_leetcode_137.single_number_II import Solution


class TestSingleNumberII(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1 = [2, 2, 3, 2]
        self.data_2 = [0, 1, 0, 1, 0, 1, 99]

    def test_single_number_ii(self):

        self.assertEqual(self.solution.single_number(self.data_1), 3)
        self.assertEqual(self.solution.single_number(self.data_2), 99)
