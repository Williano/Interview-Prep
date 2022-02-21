"""
    Leetcode No: 704
    Title: Binary Search
    Description:
    Given an array of integers nums which is sorted in ascending order,
    and an integer target, write a function to search target in nums.
    If target exists, then return its index. Otherwise, return -1.
    You must write an algorithm with O(log n) runtime complexity.


    Example 1:

    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

    Example 2:

    Input: nums = [1]
    Output: 1

    Example 3:

    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left_of_nums: int = 0
        right_of_nums: int = len(nums) - 1

        while left_of_nums <= right_of_nums:

            middle_index: int = (left_of_nums + right_of_nums) // 2

            if nums[middle_index] == target:
                return middle_index

            if nums[middle_index] > target:
                right_of_nums = middle_index - 1

            else:
                left_of_nums = middle_index + 1

        return -1
