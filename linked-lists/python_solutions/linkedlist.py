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


class Node:

    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


node1 = Node("test1")
node2 = Node("test2")
node3 = Node("test3")

# print("The nodes below aren't linked at all.")
# print(node1)
# print(node2)
# print(node3)

"""
 We don't have linked lists yet, what we have after calling node1 - node3 is
 * cargo --> 1
   next --> None
 * cargo --> 2
   next --> None
 * cargo --> 3
   next --> None
*
* To link the nodes we have to call next.
"""
node1.next = node2
node2.next = node3


# print()
# print("Lets call a linked list here >>>>node1.next")
# print(node1.next)
# print(node2.next)
# print(node3.next)
# node3 refs to None, hence at the end of the linked list

def print_list(node):
    # We are printing from head to tail
    print("LIST from HEAD to TAIL")
    while node is not None:
        print(node, end="--> ")
        node = node.next
    print('None')


print("Print from HEAD to TAIL")


# print_list(node1)

def print_backward(node):
    # We are printing from tail to head in reverse
    if node is None: return
    head = node
    tail = node.next
    print_backward(tail)
    print(head, end="-->")


# print("Print from TAIL to HEAD")
# print_backward(node1)
# print()

# Enhancement od print_backwards with a wrapper func
def print_backward_nicely(list):
    # Uses print_backward as a helper func
    print("[", end=" ")
    print_backward(list)
    print(" None]")


print_backward_nicely(node1)


def remove_second(list):
    if list is None: return
    first = list
    second = list.next
    # Make the first node ref to the 3rd
    first.next = second.next
    # Expunge the second node
    second.next = None
    return second

# TODO: Add node to the beginning. 
# TODO: Refine the algorithm

# print_list(node1)
# remove = remove_second(node1)
# print_list(remove)
# print_list(node1)
