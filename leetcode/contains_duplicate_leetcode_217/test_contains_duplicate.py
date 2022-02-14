import unittest

from contains_duplicate_leetcode_217.contains_duplicate import ContainsDuplicate


class TestContainsDuplicate(unittest.TestCase):
    def setUp(self) -> None:
        self.test = ContainsDuplicate()
        self.data_set_1 = [1, 2, 3, 1]
        self.data_set_2 = [1, 2, 3, 4]
        self.data_set_3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.data_set_4 = []

    def test_brute_force(self):

        self.assertEqual(
            self.test.contains_duplicate_brute_force(self.data_set_1), True
        )

        self.assertEqual(
            self.test.contains_duplicate_brute_force(self.data_set_2), False
        )

        self.assertEqual(
            self.test.contains_duplicate_brute_force(self.data_set_3), True
        )

        self.assertEqual(
            self.test.contains_duplicate_brute_force(self.data_set_4), False
        )

    def test_hash_map(self):

        self.assertEqual(self.test.contains_duplicate(self.data_set_1), True)

        self.assertEqual(self.test.contains_duplicate(self.data_set_2), False)

        self.assertEqual(self.test.contains_duplicate(self.data_set_3), True)

        self.assertEqual(self.test.contains_duplicate(self.data_set_4), False)
