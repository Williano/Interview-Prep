import unittest

from maximum_subarrary_leetcode_53.maximum_subarrary import Solution


class TestMaximumSubArray(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.data_2 = [1]
        self.data_3 = [5, 4, -1, 7, 8]

    def test_maximum_sub_array(self):

        self.assertEqual(self.solution.max_sub_array(self.data_1), 6)
        self.assertEqual(self.solution.max_sub_array(self.data_2), 1)
        self.assertEqual(self.solution.max_sub_array(self.data_3), 23)
