import unittest

from meeting_rooms_leetcode_252.meeting_rooms import Solution


class TestMeetingRooms(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.data_1 = [[0, 30], [5, 10], [15, 20]]
        self.data_2 = [[7, 10], [2, 4]]

    def test_meeting_rooms(self):

        self.assertEqual(self.solution.can_attend_meetings(self.data_1), False)
        self.assertEqual(self.solution.can_attend_meetings(self.data_2), True)
