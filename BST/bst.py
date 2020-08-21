class Node(object):
    def __init__(self, node_value):
        self._node = node_value
        self._left = None
        self._right = None

    def insert(self, node_value):
        if self._node == node_value:
            return False
        elif node_value < self._node:
            if self._left:
                return self._left.insert(node_value)
            else:
                self._left = Node(node_value)
                return True
        else:
            if self._right:
                return self._right.insert(node_value)
            else:
                self._right = Node(node_value)
                return True

    def find(self, node_value):
        if self._node == node_value:
            return True
        elif node_value < self._node and self._left:
            return self._left.find(node_value)
        elif node_value > self._node and self._right:
            return self._right.find(node_value)
        return False

    def preorder(self, order_list: list):
        order_list.append(self._node)
        if self._left:
            self._left.preorder(order_list)
        if self._right:
            self._right.preorder(order_list)
        return order_list

    def postorder(self, order_list: list):
        if self._left:
            self._left.postorder(order_list)
        if self._right:
            self._right.postorder(order_list)
        order_list.append(self._node)
        return order_list

    def inorder(self, order_list: list):
        if self._left:
            self._left.inorder(order_list)
        order_list.append(self._node)
        if self._right:
            self._right.inorder(order_list)
        return order_list

class BST(object):
    