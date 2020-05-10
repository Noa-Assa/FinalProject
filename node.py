from sortable import Sortable


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Decide to use Exception to make it clear one cannot make an object part of this class
# without being a part of Sortable abstract class
class SortableNode(Node):
    def __init__(self, data):
        super().__init__(data)
        if not issubclass(type(data), Sortable):
            raise Exception("Invalid Input- node must be sortable")
        self.sortable_index = data.get_sort_value()


class WeightedNode(Node):
    def __init__(self, data, weight):
        super().__init__(data)
        self.weight = weight

