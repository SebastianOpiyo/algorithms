#!/bin/python3
# Author: Sebastian Opiyo
# Date Created: May 29, 2020
# Date Modified: May 29, 2020
# Descr: Implementing linked lists in python

# A BRIEF OVERVIEW OF LINKED LISTS.
# ---------------------------------
"""
* Linked lists is a common data structure that takes advantage of the embedded references.
* Linked lists are made up of nodes, each containing a ref to the next node in the list
* Each node contains a unit of data called the cargo
* It is considered a recursive data structure bcs it has recursive def.
* An empty linked list is represented by a  NONE
* It has a HEAD and a tail that points to NONE.
*
* WHY DO WE NEED LINKED LISTS?
* 1. They provide a way to assemble objects into a single entity i.e a collection
"""


from numpy import add


class Node:

    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)
    
    # Print Linked list
    def print_list(self, node):
        # We are printing from head to tail
        print("LIST from HEAD to TAIL")
        while node is not None:
            print(node, end="--> ")
            node = node.next
        print('None')
    
    def print_backward(self, node):
        """ Print linked list from TAIL to HEAD recursively """
        if node is None: return
        head = node
        tail = node.next
        self.print_backward(tail)
        print(head, end="-->")



"""
 We don't have linked lists yet, what we have after calling node1 - node3 is
 * cargo --> 1
   next --> None
 * cargo --> 2
   next --> None
 * cargo --> 3
   next --> None
*
* To link the nodes we have to call next and point it tot the next node
"""

# Enhancement od print_backwards with a wrapper func
def print_backward_nicely(list):
    # Uses print_backward as a helper func
    print("[", end=" ")
    print_backward(list)
    print(" None]")


def remove_second(list):
    if list is None: return
    first = list
    second = list.next
    # Make the first node ref to the 3rd
    first.next = second.next
    # Expunge the second node
    second.next = None
    return second

def add_node_beginning(llist, new_node):
    # we need to make sure the llist is not empty
    if llist is None:
        print("Linked list is empy, new node is Head")
        return new_node
    
    new_node.next = llist
    print("New head is:", new_node)
    print(llist.print_list(new_node))
    return new_node

# Add Node at the end of the linked list
def add_node_end(llist, new_node):
    if llist is None:
        print("Linked list is empty, new node is Head")
        return new_node
    current = llist
    while current.next is not None:
        current = current.next
        print("Current node is:", current)
    current.next = new_node
    print("Added new node at the end:", new_node)
    return llist



if __name__ == "__main__":
    node1 = Node("test1")
    node2 = Node("test2")
    node3 = Node("test3")
    # Linking the nodes
    node1.next = node2
    node2.next = node3
    add_node_beginning(node1, Node("new_head"))