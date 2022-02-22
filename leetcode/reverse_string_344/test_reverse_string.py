import unittest

from reverse_string_344.reverse_string import Solution


class TestReverseString(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1 = ["h", "e", "l", "l", "o"]
        self.data_2 = ["H", "a", "n", "n", "a", "h"]

    def test_valid_palindrome(self):

        self.assertEqual(
            self.solution.reverse_string(self.data_1), ["o", "l", "l", "e", "h"]
        )
        self.assertEqual(
            self.solution.reverse_string_v1(self.data_1), ["o", "l", "l", "e", "h"]
        )
        self.assertEqual(
            self.solution.reverse_string(self.data_2), ["h", "a", "n", "n", "a", "H"]
        )
        self.assertEqual(
            self.solution.reverse_string_v1(self.data_2), ["h", "a", "n", "n", "a", "H"]
        )
