from linkedList import SortedLinkedList


class SortedStack:
    def __init__(self):
        self.stack = SortedLinkedList()

    def push(self, data):
        self.stack.add_in_order(data)

    def is_empty(self):
        return self.stack.head is None

    def pop(self):
        if self.is_empty():
            return None
        top_element = self.stack.head
        self.stack.head = top_element.next
        return top_element.data

    def top(self):
        if self.is_empty():
            return None
        return self.stack.head.data

    def size(self):
        return self.stack.count()

    def __str__(self):
        return self.stack.__str__()