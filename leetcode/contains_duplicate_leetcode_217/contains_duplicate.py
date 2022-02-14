"""
    Leetcode No: 217
    Title: Contains Duplicates
    Description:
    Given an integer array nums, return true if any value appears at least
    twice in the array, and return false if every element is distinct.

    Example 1:

    Input: nums = [1,2,3,1]
    Output: true
    Example 2:

    Input: nums = [1,2,3,4]
    Output: false
    Example 3:

    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true
"""

from typing import List


class ContainsDuplicate:
    def contains_duplicate_brute_force(self, nums: List[int]) -> bool:

        for i_element in range(len(nums)):
            for j_element in range(i_element + 1, len(nums)):
                if nums[i_element] == nums[j_element]:
                    return True

        return False

    def contains_duplicate(self, nums: List[int]) -> bool:

        element_frequency = {}

        for num in nums:
            if num in element_frequency:
                return True

            element_frequency[num] = 1

        return False
