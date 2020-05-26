from data_structures.node import Node


class WeightedNode(Node):
    def __init__(self, data, weight):
        super().__init__(data)
        self.weight = weight