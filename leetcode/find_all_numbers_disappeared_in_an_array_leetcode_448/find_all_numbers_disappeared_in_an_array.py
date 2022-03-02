"""
    Leetcode No: 448
    Title: Find All Numbers Disappeared in an Array
    Description:
    Given an array nums of n integers where nums[i] is in the range [1, n],
    return an array of all the integers in the range [1, n] that do not
    appear in nums.

    Example 1:

    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [5,6]


    Example 2:

    Input: nums = [1,1]
    Output: [2]


    Example 3:

    Input: root = []
    Output: []
"""


from typing import List


class Solution:
    def find_disappeared_numbers(self, nums: List[int]) -> List[int]:
        """
        Big O:

            Time Complexity: O(n^2)
            Space Complexity: 0(n^2)
        """

        # Hash table for keeping track of the numbers in the array
        # Note that we can also use a set here since we are not
        # really concerned with the frequency of numbers.
        hash_table = {}

        # Add each of the numbers to the hash table
        for num in nums:
            hash_table[num] = 1

        # Response array that would contain the missing numbers
        result = []

        # Iterate over the numbers from 1 to N and add all those
        # that don't appear in the hash table.
        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)

        return result
