import unittest

from reverse_words_in_a_string_leetcode_151.reverse_words_in_a_string import Solution


class TestReverseWordsInAString(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1 = "the sky is blue"
        self.data_2 = "  hello world  "
        self.data_3 = "a good   example"

    def test_reverse_words_in_a_string(self):

        self.assertEqual(self.solution.reverse_words(self.data_1), "blue is sky the")
        self.assertEqual(self.solution.reverse_words(self.data_2), "world hello")
        self.assertEqual(self.solution.reverse_words(self.data_3), "example good a")
