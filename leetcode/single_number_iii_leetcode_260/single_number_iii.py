"""
    Leetcode No: 260
    Title: Single Number III
    Description:
    Given an integer array nums, in which exactly two elements appear only once
    and all the other elements appear exactly twice. Find the two elements
    that appear only once. You can return the answer in any order.
    You must write an algorithm that runs in linear runtime complexity and
    uses only constant extra space.

    Example 1:

    Input: nums = [1,2,1,3,2,5]
    Output: [3,5]
    Explanation:  [5, 3] is also a valid answer.

    Example 2:

    Input: nums = [-1,0]
    Output: [-1,0]

    Example 3:

    Input: nums = [0,1]
    Output: [1,0]

"""
from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> List[int]:

        if len(nums) < 2:
            return

        elements = []

        for num in nums:

            num_count = nums.count(num)

            if num_count < 2:
                elements.append(num)

        return elements
