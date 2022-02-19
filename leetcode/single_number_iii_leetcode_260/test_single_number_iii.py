import unittest

from single_number_iii_leetcode_260.single_number_iii import Solution


class TestSingleNumberIII(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1 = [1, 2, 1, 3, 2, 5]
        self.data_2 = [-1, 0]
        self.data_3 = [0, 1]

    def test_single_number(self):

        self.assertEqual(self.solution.single_number(self.data_1), [3, 5])
        self.assertEqual(self.solution.single_number(self.data_2), [-1, 0])
        self.assertEqual(self.solution.single_number(self.data_3), [1, 0])
