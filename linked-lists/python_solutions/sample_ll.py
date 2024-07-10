class Node:
    def __init__(self, new_data=None, next_node=None):
        self.data = new_data
        self.next_node = next_node
        #self.counter = 0

    # define getter and setter
    def set_data(self, new_data):
        self.data = new_data
    
    def set_next_node(self, next_node):
        self.next_node = next_node
    
    def get_data(self):
        return self.data
    
    def get_next_node(self):
        return self.next_node
    
    def __str__(self):
        return str(self.data)

# test
# Creating
node_1 = Node("Orange")
node_2 = Node("Mangoes")
node_3 = Node("Bananas")
node_4 = Node("Lemon")
# print(node_1, node_2, node_3, node_4)

# Linking nodes
node_1.set_next_node(node_2)
node_2.set_next_node(node_3)
node_3.set_next_node(node_4)


def print_linked_list(node:Node):
    while node is not None:
        print(node.get_data(), end="-->")
        node = node.get_next_node()
    print(None)        

print_linked_list(node=node_1)


class LinkedList:
    pass