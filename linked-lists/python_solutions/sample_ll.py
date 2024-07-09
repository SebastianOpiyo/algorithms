class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        self.count = 0
        
    def set_next_node(self, next_node):
        """Set next node."""
        self.next_node = next_node
    
    def set_data(self, data):
        """Set node data."""
        self.data = data
    
    def set_counter(self):
        """Increament the counter."""
        self.count += 1 

    def decreament_counter(self):
        """Decreament the counter when node is deleted."""
        self.count -= 1
    
    def get_nextnode(self):
        """Return the next node in the list."""
        return self.next_node
    
    def get_data(self):
        """Get node data."""
        return self.data
    
    def get_node_count(self):
        """Get the number of nodes."""
        return self.count
    
    def __str__(self) -> str:
        return str(self.data)


# This nodes are not linked
node_1 = Node("mango")
node_2 = Node("Orange")
# print(node_1, node_2)

# To link them
node_1.next_node = node_2
print(node_2.next_node)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def is_empty(self):
        '''Checks if the LL is empty'''
        return self.head is None

    def add(self, node):
        '''Add Node to the LinkedList'''
        self.add(Node(node))
        if LinkedList.is_empty:
            self.head = node
            self.tail = node.nex



