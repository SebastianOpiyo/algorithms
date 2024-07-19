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


def print_linked_list(node:Node):
    while node is not None:
        print(node.get_data(), end="-->")
        node = node.get_next_node()       

# print_linked_list(node=node_1)


class UnorderedLinkedList:
    
    def __init__(self) -> None:
        self.head = None
        # self._tail = None
    
    def is_empty(self):
        return self.head is None
    
    def add(self, data):
        '''Add Node to the LinkedList'''
        temp = Node(data)
        temp.set_next_node(self.head)
        self.head = temp
        
    def get_list_size(self):
        '''Get the number of nodes in the linked list'''
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next_node()
        return count
    
    
    def search_item(self, item):
        found = False
        current = self.head
        
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next_node()
            return found
    
    def remove_item(self, item):
        pass



# Test
my_list = UnorderedLinkedList()
# print(my_list.is_empty())
my_list.add("Orange")
my_list.add("Mango")
# print(my_list.is_empty())
# print(my_list.get_list_size())
print(my_list.search_item("Mango"))
