"""
    Leetcode No: 136
    Title: Single Number
    Description:
    Given a non-empty array of integers nums, every element appears twice
    except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and
    use only constant extra space.

    Example 1:
    Input: nums = [2,2,1]
    Output: 1

    Example 2:

    Input: nums = [4,1,2,1,2]
    Output: 4

    Example 3:

    Input: nums = [1]
    Output: 1
"""
from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return nums[0]

        for num in nums:
            num_count = nums.count(num)

            if num_count < 2:
                return num
