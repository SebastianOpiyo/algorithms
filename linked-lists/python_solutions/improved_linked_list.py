class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.count = 0

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def increase_count(self):
        self.count += 1

    def decrease_count(self):
        self.count -= 1


class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head == None
