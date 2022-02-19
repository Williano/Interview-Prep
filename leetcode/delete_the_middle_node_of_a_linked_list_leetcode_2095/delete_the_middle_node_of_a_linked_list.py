"""
    Leetcode No: 2095
    Title: Delete The Middle Node of A Linked List
    Description:
    You are given the head of a linked list. Delete the middle node,
    and return the head of the modified linked list.
    The middle node of a linked list of size n is the ⌊n / 2⌋th node
    from the start using 0-based indexing, where ⌊x⌋ denotes the largest
    integer less than or equal to x.
    For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2,
    respectively.

    Example 1:

    Input: head = [1,3,4,7,1,2,6]
    Output: [1,3,4,1,2,6]
    Explanation:
    The above figure represents the given linked list. The indices of the
    nodes are written below.
    Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
    We return the new list after removing this node.


    Example 2:

    Input: head = [1,2,3,4]
    Output: [1,2,4]
    Explanation:
    The above figure represents the given linked list.
    For n = 4, node 2 with value 3 is the middle node, which is marked in red.

    Example 3:

    Input: head = [2,1]
    Output: [2]
    Explanation:
    The above figure represents the given linked list.
    For n = 2, node 1 with value 1 is the middle node, which is marked in red.
    Node 0 with value 2 is the only node remaining after removing node 1.
"""


class Solution:
    def get_length_of_list(self, head) -> int:

        # Get the length of the list
        counter = 0
        current_node = head

        while current_node:
            counter += 1
            current_node = current_node.next

        return counter

    def delete_middle(self, head):

        if head is None:
            return head

        # Calculate the index of the middle number
        middle_number_index = self.get_length_of_list(head) // 2

        # Check if the middle number is equal to the first element
        if middle_number_index == 0:
            head = head.next

        # Remove the middle number
        counter = 0
        current_node = head

        while current_node:
            if counter == (middle_number_index - 1):
                current_node.next = current_node.next.next
                return head

            current_node = current_node.next
            counter += 1

        return head
