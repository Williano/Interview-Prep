"""
    Leetcode No: 1
    Title: Two Sum
    Description:
    Given an array of integers nums and an integer target, return indices of
    the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may
    not use the same element twice.
    You can return the answer in any order.

    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


    Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]
"""

from typing import List


class TwoSum:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        While we are iterating and inserting elements into the hash table,
        we also look back to check if current element's difference already
        exists in the hash table. If it exists, we have found a solution and
        return the indices immediately.

        Time complexity: O(n). We traverse the list containing nn elements
        only once. Each lookup in the table costs only O(1)O(1) time.

        Space complexity: O(n). The extra space required depends on the
        number of items stored in the hash table,
        which stores at most n elements.
        """

        diff_from_target_and_index = {}  # diff: index

        for element_index, element in enumerate(nums):
            diff_from_target = target - element

            if diff_from_target in diff_from_target_and_index:
                return [diff_from_target_and_index[diff_from_target], element_index]

            diff_from_target_and_index[element] = element_index

        return []

    def two_sum_brute_force(self, nums: List[int], target: int) -> List[int]:
        """
        The brute force approach is simple. Loop through each element x and
        find if there is another value that equals to target - x.

        Time complexity: O(n^2). For each element, we try to find its
        complement by looping through the rest of the array which takes O(n)
        time. Therefore, the time complexity is O(n^2).

        Space complexity: O(1). The space required does not depend on the
        size of the input array, so only constant space is used.

        """

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

        return []


def main():

    two_sum_test = TwoSum()

    test_cases = [
        [[2, 7, 11, 15], 9],
        [[3, 2, 4], 6],
        [[3, 3], 6],
    ]

    for test_case in test_cases:
        print(two_sum_test.two_sum(nums=test_case[0], target=test_case[1]))


if __name__ == "__main__":
    main()
