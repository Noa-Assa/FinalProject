import files_functions as ff


# method that implement loading file
new_graph = ff.load_graph_from_json('weighted_graph.json')

print(new_graph)

# list of graph vertices:
print(new_graph.get_vertices())

# list of graph edges:
print(new_graph.get_edges())

# add vertex to graph:
new_graph.add_vertex('London', [['Tel-Aviv', 50], ['Oxford', 3]])
print(new_graph)

# delete vertex from graph:
new_graph.delete_vertex('London')
print(new_graph)

# BFS and Shortest path:
print(new_graph.bfs('Tel-Aviv', 'Holon'))
print(new_graph.shortest_path('Tel-Aviv', 'Holon'))

# save to json + serialize:
ff.save_graph_to_json(new_graph, 'new_json.json')