import unittest

from missing_number_leetcode_268.missing_number import Solution


class TestMissingNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.test = Solution()
        self.data_1 = [3, 0, 1]
        self.data_2 = [0, 1]
        self.data_3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]

    def test_missing_number(self) -> None:

        self.assertEqual(self.test.missing_number(self.data_1), 2)
        self.assertEqual(self.test.missing_number(self.data_2), 2)
        self.assertEqual(self.test.missing_number(self.data_3), 8)
