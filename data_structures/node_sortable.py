from data_structures.node import Node
from data_structures.sortable import Sortable


class SortableNode(Node):
    def __init__(self, data):
        super().__init__(data)
        if not issubclass(type(data), Sortable):
            raise Exception("Invalid Input- node must be sortable")
        self.sortable_index = data.get_sort_value()