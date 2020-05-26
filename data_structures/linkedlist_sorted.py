from data_structures.linkedlist import LinkedList
from data_structures.node_sortable import SortableNode


class SortedLinkedList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)

    def add_in_order(self, data):
        new_node = SortableNode(data)
        self.list_size += 1
        if (self.head is None) or (self.head.sortable_index <= new_node.sortable_index):
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            if new_node.sortable_index > current_node.next.sortable_index:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        current_node.next = new_node