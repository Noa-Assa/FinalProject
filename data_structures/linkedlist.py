class LinkedList:
    def __init__(self):
        self.head = None
        self.list_size = 0

    def __str__(self):
        current_node = self.head
        list_as_string = ''
        while current_node is not None:
            list_as_string += current_node.data.__str__() + '  '
            current_node = current_node.next
        return list_as_string

    def delete_node(self, node):
        if self.head is None:
            return
        current_node = self.head
        if current_node.data == node:
            self.head = current_node.next
            current_node.data = None
            current_node.next = None
            self.list_size -= 1
            return
        while current_node.next.data != node:
            current_node = current_node.next
            if current_node is None:
                return
        temp = current_node.next.next
        current_node.next.data = None
        current_node.next = None
        current_node.next = temp
        self.list_size -= 1

    def count(self):
        return self.list_size


