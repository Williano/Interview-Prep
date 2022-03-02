import unittest


from find_all_duplicates_in_an_array_leetcode_442.find_all_duplicates_in_an_array import (
    Solution,
)


class TestFindAllDisappearedNumbers(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1 = [4, 3, 2, 7, 8, 2, 3, 1]
        self.data_2 = [1, 1, 2]
        self.data_3 = [1]

    def test_find_all_numbers_disappeared_in_an_array(self):

        self.assertEqual(self.solution.find_duplicates(self.data_1), [2, 3])
        self.assertEqual(self.solution.find_duplicates(self.data_2), [1])
        self.assertEqual(self.solution.find_duplicates(self.data_1), [])
