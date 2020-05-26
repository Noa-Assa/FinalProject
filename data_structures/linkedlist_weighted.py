from data_structures.linkedlist import LinkedList
from data_structures.node_weighted import WeightedNode


class WeightedLinkedList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)

    def add_new_head(self, data, weight):
        new_node = WeightedNode(data, weight)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        current_node = self.head
        list_as_string = ''
        while current_node is not None:
            list_as_string += current_node.data.__str__() + '(' + str(current_node.weight) + ')  '
            current_node = current_node.next
        return list_as_string
