import json
import pandas as pd
from graph import WeightedGraph


def save_graph_to_json(graph, file_name):
    serialized_graph = graph.serialize()
    try:
        with open('{}.json'.format(file_name), 'w') as saved_graph:
            json.dump(serialized_graph, saved_graph)
        saved_graph.close()
    except:
        print("Error while trying to open file")


def load_graph_from_json(file_name):
    try:
        with open(file_name, 'r') as loaded_graph:
            data = WeightedGraph(json.load(loaded_graph))
    except:
        print("Error while handling file: ", file_name)
        data = None
    return data


def load_csv_file(file_name):
    data = None
    try:
        data = pd.read_csv(file_name)
    except:
        print("Error while handling file")
    finally:
        return data


def save_to_json(data, file_name):
    try:
        with open('{}.json'.format(file_name), 'w') as saved_json:
            json.dump(data, saved_json)
        saved_json.close()
    except:
        print("Error while trying to open file")


def load_from_json(file_name):
    try:
        with open(file_name, 'r') as loaded_json:
            data = {json.load(loaded_json)}
    except:
        print("Error while handling file: ", file_name)
        data = None
    return data
