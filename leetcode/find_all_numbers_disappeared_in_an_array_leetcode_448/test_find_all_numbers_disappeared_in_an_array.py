import unittest


from find_all_numbers_disappeared_in_an_array_leetcode_448.find_all_numbers_disappeared_in_an_array import (
    Solution,
)


class TestFindAllDisappearedNumbers(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1 = [4, 3, 2, 7, 8, 2, 3, 1]
        self.data_2 = [1, 1]
        self.data_3 = []

    def test_find_all_numbers_disappeared_in_an_array(self):

        self.assertEqual(self.solution.find_disappeared_numbers(self.data_1), [5, 6])
        self.assertEqual(self.solution.find_disappeared_numbers(self.data_2), [2])
        self.assertEqual(self.solution.find_disappeared_numbers(self.data_1), [])
