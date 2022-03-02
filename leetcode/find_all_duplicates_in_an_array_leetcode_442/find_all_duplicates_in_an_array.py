"""
    Leetcode No: 442
    Title: Find All Duplicates In An Array
    Description:
    Given an integer array nums of length n where all the integers of nums are
    in the range [1, n] and each integer appears once or twice, return an
    array of all the integers that appears twice.
    You must write an algorithm that runs in O(n) time and uses only constant extra space.

    Example 1:

    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [2,3]


    Example 2:

    Input: nums = [1,1,2]
    Output: [1]


    Example 3:

    Input: nums = [1]
    Output: []
"""


from typing import List


class Solution:
    def find_duplicates(self, nums: List[int]) -> List[int]:

        hash_table = {}

        new_list = []

        for num in nums:

            if num not in hash_table:
                hash_table[num] = 1
            else:
                new_list.append(num)

        return new_list
