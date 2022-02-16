"""
    Leetcode No: 206
    Title: Reverse Linked List
    Description:
    Given the head of a singly linked list, reverse the list, and
    return the reversed list.

    Example 1:

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Example 2:

    Input: head = [1,2]
    Output: [2,1]

    Example 3:

    Input: head = []
    Output: []

"""


class Solution:
    def reverse_linked_list(self, head):

        previous_node = None
        current_node = head

        while current_node:
            current_node_next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = current_node_next

        return previous_node
