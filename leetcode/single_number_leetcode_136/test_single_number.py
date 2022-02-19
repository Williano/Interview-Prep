import unittest

from single_number_leetcode_136.single_number import Solution


class TestSingleNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1 = [2, 2, 1]
        self.data_2 = [4, 1, 2, 1, 2]
        self.data_3 = [1]

    def test_single_number(self):

        self.assertEqual(self.solution.single_number(self.data_1), 1)
        self.assertEqual(self.solution.single_number(self.data_2), 4)
        self.assertEqual(self.solution.single_number(self.data_3), 1)
