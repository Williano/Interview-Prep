"""
    Leetcode No: 53
    Title: Maximum Subarray
    Description:
    Given an integer array nums, find the contiguous subarray
    (containing at least one number) which has the largest sum and return its sum.
    A subarray is a contiguous part of an array.


    Example 1:

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

    Example 2:

    Input: nums = [1]
    Output: 1

    Example 3:

    Input: nums = [5,4,-1,7,8]
    Output: 23
"""

from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:

        max_sub_arr: int = nums[0]

        current_sum: int = 0

        for num in nums:

            if current_sum < 0:
                current_sum = 0

            current_sum += num

            max_sub_arr = max(max_sub_arr, current_sum)

        return max_sub_arr
