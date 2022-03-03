"""
    Leetcode No: 252
    Title: Meeting Rooms
    Description:
    Given an array of meeting time intervals where intervals[i] = [starti, endi],
    determine if a person could attend all meetings.

    Example 1:

    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: false


    Example 2:

    Input: intervals = [[7,10],[2,4]]
    Output: true

"""


from typing import List


class Solution:
    def can_attend_meetings(self, intervals: List[List[int]]) -> bool:

        """
        Big 0:

        Time Complexity: O(nlogn) -> Sort is nlogn and we go through each element once
        Space Complexity: O(1)
        """

        # Sort the list first
        intervals.sort()

        for index, element in enumerate(intervals):

            # You want to compare the current meeting's end time with the next
            # meeting's end time so you have to check if we are not at the end
            # of the list by checking the current index + 1 is less than the
            # size of the list
            if index + 1 < len(intervals) and element[1] > intervals[index + 1][0]:
                return False

        return True
