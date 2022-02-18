import unittest

from merge_two_sorted_lists_leetcode_21.merge_two_sorted_lists import Solution


class TestMergeTwoSortedLists(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1a, self.data_1b = [1, 2, 4], [1, 3, 4]
        self.data_2a, self.data_2b = [], []
        self.data_3a, self.data_3b = [], [0]

    def test_merge_two_sorted_lists(self) -> None:

        self.assertEqual(
            self.solution.merge_two_lists(self.data_1a, self.data_1b),
            [1, 1, 2, 3, 4, 4],
        )

        self.assertEqual(self.solution.merge_two_lists(self.data_2a, self.data_2b), [])

        self.assertEqual(self.solution.merge_two_lists(self.data_3a, self.data_3b), [0])
