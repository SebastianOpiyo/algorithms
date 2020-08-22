#!/bin/python3
# Author: Sebastian Opiyo
# Date Created: Aug 22, 2020
# Date Modified: Aug 22, 2020
# Descr: Implementing BST
# Acknowledgement: runestone.academy

# Since will need to create and work with an empty binary tree,
# will have two classes.

class TreeNode(object):
    """This is the root of the Binary Search Tree.
        - Serves to provide helper functions that make work done in the BST class
        - It also keeps track of the parent as an attribute of each node.
    """

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    # BST Helper methods
    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
        else:
            if self.is_left_child():
                self.parent.left_child = self.right_child
            else:
                self.parent.right_child = self.right_child
            self.right_child.parent = self.parent

    def find_successor(self):
        successor = None
        if self.has_right_child():
            successor = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self
        return successor

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def replace_node_data(self, key, value, l_child, r_child):
        self.key = key
        self.payload = value
        self.left_child = l_child
        self.right_child = r_child
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self




    # def insert(self, node_value):
    #     if self._node == node_value:
    #         return False
    #     elif node_value < self._node:
    #         if self._left:
    #             return self._left.insert(node_value)
    #         else:
    #             self._left = TreeNode(node_value)
    #             return True
    #     else:
    #         if self._right:
    #             return self._right.insert(node_value)
    #         else:
    #             self._right = TreeNode(node_value)
    #             return True
    #
    # def find(self, node_value):
    #     if self._node == node_value:
    #         return True
    #     elif node_value < self._node and self._left:
    #         return self._left.find(node_value)
    #     elif node_value > self._node and self._right:
    #         return self._right.find(node_value)
    #     return False
    #
    # def preorder(self, order_list: list):
    #     order_list.append(self._node)
    #     if self._left:
    #         self._left.preorder(order_list)
    #     if self._right:
    #         self._right.preorder(order_list)
    #     return order_list
    #
    # def postorder(self, order_list: list):
    #     if self._left:
    #         self._left.postorder(order_list)
    #     if self._right:
    #         self._right.postorder(order_list)
    #     order_list.append(self._node)
    #     return order_list
    #
    # def inorder(self, order_list: list):
    #     if self._left:
    #         self._left.inorder(order_list)
    #     order_list.append(self._node)
    #     if self._right:
    #         self._right.inorder(order_list)
    #     return order_list


class BST(object):
    """This a Binary Search Tree that has reference to the TreeNode.
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
