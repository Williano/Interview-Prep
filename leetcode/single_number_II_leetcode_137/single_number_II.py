"""
    Leetcode No: 137
    Title: Single Number II
    Description:
   Given an integer array nums where every element appears three times except
   for one, which appears exactly once. Find the single element and return it.
   You must implement a solution with a linear runtime complexity and use only
   constant extra space.

    Example 1:
    Input: nums = [2,2,3,2]
    Output: 3

    Example 2:

    Input: nums = [0,1,0,1,0,1,99]
    Output: 99

"""
from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return nums

        if len(nums) < 2:
            return nums[0]

        for num in nums:
            num_count = nums.count(num)

            if num_count < 2:
                return num
