"""
    Leetcode No: 2
    Title: Add Two Numbers
    Description:
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains
    a single digit. Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except
    the number 0 itself..

    Example 1:

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.


    Example 2:

    Input: l1 = [0], l2 = [0]
    Output: [0]

    Example 3:

    IInput: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
"""


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        """
        Big 0:

        Time Complexity: O(max(m, n))
        Space Complexity: O(n)
        """

        dummy = ListNode(0)
        current_node = dummy

        carry_over = 0

        # Continue the loop if any of the list or carry over has value
        while l1 or l2 or carry_over:

            # Check to make sure each has a number
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add two numbers and the carry over
            sum_of_vals = val1 + val2 + carry_over

            carry_over = sum_of_vals // 10

            val = sum_of_vals % 10

            current_node.next = ListNode(val)

            current_node = current_node.next

            # Move to the next values in the list after each iteration if it has
            # a value
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the dummy next because the current node pointe will point to
        # end of the list and the dummy will be zero
        return dummy.next
