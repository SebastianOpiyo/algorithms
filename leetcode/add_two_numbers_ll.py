# Topic: LL, recursion
# Difficulty: medium


'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Define the Node
from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    """Class to create a linked list and add nodes to it"""
    
    def __init__(self, mylist):
        self.head = None
        self.tail = None
        self.mylist = mylist
        self.create_linked_list_from_list()

    
    def create_linked_list_from_list(self):
        """Create a linked list from a list of ints"""
        # Create a ll
        for item in reversed(self.mylist):
            self.append_node(item)
    
    def append_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        # traverse to the end of the list and add  new node
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    
    def print_list(self):
        current_node = self.head

        while current_node:
            print(f'{current_node.data} -> ', end='')
            current_node = current_node.next
        print('None')


class Solution:
    def addTwoNumbers(self, l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
        pass
pass



# Test cases
l1 = LinkedList([2,4,3])
l2 = LinkedList([5,6,4])

l1.print_list()
l2.print_list()
# print(l1.head.data)