import unittest

from valid_anagram_leetcode_242.valid_anagram import Solution


class TestValidAnagram(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1a, self.data_1b = "anagram", "nagaram"
        self.data_2a, self.data_2b = "rat", "car"

    def test_valid_anagram(self):

        self.assertEqual(self.solution.is_anagram(self.data_1a, self.data_1b), True)
        self.assertEqual(self.solution.is_anagram(self.data_2a, self.data_2b), False)
