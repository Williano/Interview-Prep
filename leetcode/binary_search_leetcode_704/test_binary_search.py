import unittest

from binary_search_leetcode_704.binary_search import Solution


class TestSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1 = [-1, 0, 3, 5, 9, 12]
        self.data_2 = [-1, 0, 3, 5, 9, 12]

    def test_search(self):

        self.assertEqual(self.solution.search(self.data_1), 9)
        self.assertEqual(self.solution.search(self.data_2), 2)
