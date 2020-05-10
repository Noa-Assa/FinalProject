from collections import deque
from linkedList import WeightedLinkedList


class WeightedGraph:
    def __init__(self, dict):
        self.dict = dict
        for vertex in self.dict:
            neighbors = WeightedLinkedList()
            for neighbor in self.dict[vertex]:
                neighbors.add_new_head(neighbor[0], neighbor[1])
            self.dict[vertex] = neighbors

    def __str__(self):
        graph_as_string = ''
        for vertex in self.dict:
            graph_as_string += str(vertex) + ' -> '
            graph_as_string += self.dict[vertex].__str__() + '\n'
        return graph_as_string

    def get_vertices(self):
        return list(self.dict)

    def get_edges(self):
        all_edges = []
        for vertex in self.dict:
            temp_vertex = self.dict[vertex].head
            while temp_vertex is not None:
                if {vertex, temp_vertex.data, temp_vertex.weight} not in all_edges:
                    all_edges.append({vertex, temp_vertex.data, temp_vertex.weight})
                temp_vertex = temp_vertex.next
        return all_edges

    def add_vertex(self, vertex, connections):
        new_connections = WeightedLinkedList()
        for connection in connections:
            neighbor = connection[0]
            weight = connection[1]
            if neighbor not in self.dict:
                self.dict.update({neighbor: WeightedLinkedList()})
                self.dict[neighbor].add_new_head(vertex, weight)
            else:
                self.add_missing_node(neighbor, vertex, weight)
            if vertex not in self.dict:
                new_connections.add_new_head(neighbor, weight)
            else:
                self.add_missing_node(vertex, neighbor, weight)
        if new_connections.head is not None:
            self.dict.update({vertex: new_connections})

    def add_missing_node(self, vertex, neighbor, weight):
        current_node = self.dict[vertex].head
        while current_node is not None:
            if current_node.data == neighbor:
                break
            current_node = current_node.next
        if current_node is None:
            self.dict[vertex].add_new_head(neighbor, weight)

    def delete_vertex(self, vertex):
        if vertex not in self.dict:
            return
        connection = self.dict[vertex].head
        while connection is not None:
            self.dict[connection.data].delete_node(vertex)
            connection = connection.next
        del self.dict[vertex]

    def get_all_connections(self, vertex):
        dict_of_connections = {}
        current_node = self.dict[vertex].head
        while current_node is not None:
            dict_of_connections[current_node.data] = current_node.weight
            current_node = current_node.next
        return dict_of_connections

    def bfs(self, source, target):
        if source not in self.dict:
            return print('the vertex ' + source + ' not in vertex keys')
        if target not in self.dict:
            return print('the vertex ' + target + ' not in vertex keys')
        if source == target:
            return print('start point and end point are similar')
        initial_weight = 0
        index = (source, [source], initial_weight)
        queue = deque()
        queue.append(index)
        results = []
        while queue:
            (vertex, connections, weight) = queue.popleft()
            temp_dict = self.get_all_connections(vertex)
            for item in set(temp_dict.keys()) - set(connections):
                if item == target:
                    results.append((connections + [item], weight + temp_dict[item]))
                else:
                    queue.append((item, connections + [item], weight + temp_dict[item]))
        return results

    def shortest_path(self, source, target):
        results = self.bfs(source, target)
        shortest_paths = []
        if not not results:
            min_weight = results[0][1]
            for path in results:
                if path[1] == min_weight:
                    shortest_paths.append(path)
                if path[1] < min_weight:
                    min_weight = path[1]
                    shortest_paths.clear()
                    shortest_paths.append(path)
        return shortest_paths

    def get_all_in_list(self, vertex):
        list = []
        current_node = self.dict[vertex].head
        while current_node is not None:
            list.append([current_node.data, current_node.weight])
            current_node = current_node.next
        return list

    def serialize(self):
        serialized = {}
        for vertex in self.dict:
            neighbors = self.get_all_in_list(vertex)
            serialized[vertex] = neighbors
        return serialized

    @staticmethod
    def deserialize(dict):
        graph_object = WeightedGraph(dict)
        return graph_object

