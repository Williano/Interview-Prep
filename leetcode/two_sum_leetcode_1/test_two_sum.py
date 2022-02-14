import unittest

from two_sum_leetcode_1.two_sum import TwoSum


class TestTwoSum(unittest.TestCase):
    def setUp(self) -> None:
        self.test_two_sum = TwoSum()

    def test_cases(self):
        self.assertEqual(
            self.test_two_sum.two_sum(nums=[2, 7, 11, 15], target=9), [1, 0]
        )

        self.assertEqual(self.test_two_sum.two_sum(nums=[3, 2, 4], target=6), [2, 1])

        self.assertEqual(self.test_two_sum.two_sum(nums=[3, 3], target=6), [1, 0])

        self.assertEqual(self.test_two_sum.two_sum(nums=[3, 2, 4], target=15), [])

        self.assertEqual(self.test_two_sum.two_sum(nums=[], target=15), [])


# How to run test
# python -m unittest  two_sum_leetcode_1/test_two_sum.py
