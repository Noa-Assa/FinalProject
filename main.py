from data_analysis.knn_algorithm import knn
from data_structures.stack import SortedStack
from utilities import files_functions as ff
from data_analysis.app_store_analysis import AppStoreAnalysis
from utilities.menu_utilities import show, show_object, is_choice_valid
from data_structures.student import Student


def menu(methods, text):
    def func():
        while True:
            num_choices = len(methods)+1
            try:
                user_input = is_choice_valid(input(text), num_choices)
                if user_input == num_choices:
                    break
                methods[user_input-1]()
            except Exception as e:
                print(e)
    return func


def main():
    app_store = AppStoreAnalysis()
    students_stack = SortedStack()
    cities_graph = ff.load_graph_from_json('resources/weighted_graph.json')

    menu_ml = menu([knn], """
                This part applies KNN Algorithm on the 2 DataSets that was used for the data analysis part.
                 It includes the Pre-Processing of the merged sets, and if you decide to run this code, it will
                 create a JSON file- 'allK_acc' - for the optional K's, their accuracy score, and the time it took to get it.

                 What would you like to do?
                 1. Run Knn Algorithm.
                 2. Back to previous menu.\n""")

    menu_sql = menu([app_store.apps.structure, app_store.reviews.structure, app_store.apps.category_analysis,
                     app_store.sentiment_analysis, app_store.apps.popularity_analysis, app_store.apps.extra_info], """
                This part contains 2 different DataSets - Application and User reviews, which displays apps
                in GooglePlay store and user reviews about those apps.

                What would you like to see?
                1 - View application table structure.
                2 - View user reviews table structure.
                3 - View application categories analysis.
                4 - View application sentiment analysis.
                5 - View application popularity analysis.
                6 - View applications sizes.
                7 - Back to previous menu\n""")

    menu_graph = menu([show_object(cities_graph), show(cities_graph.get_vertices), show(cities_graph.get_edges),
                       cities_graph.add_vertex, cities_graph.delete_vertex, show(cities_graph.bfs),
                       show(cities_graph.shortest_path), cities_graph.save_graph], """
                        What would you like to do?
                        1 - View graph.
                        2 - Show all cities in graph.
                        3 - Show connections between cities.
                        4 - Add city and connections
                        5 - Delete city.
                        6 - Get all possible routs between 2 cities.
                        7 - Get the shortest way between 2 cities.
                        8 - Save graph to JSON file.
                        9 - Back to previous menu.\n""")

    def menu_prep(): students_stack.push(Student())
    menu_stack = menu([menu_prep, show(students_stack.pop), show(students_stack.top), show(students_stack.size),
                       show_object(students_stack)], """
                        What would you like to do?
                        1 - PUSH - Add new student.
                        2 - POP - take out and show highest grade student.
                        3 - TOP - Take a look at the student with the highest average.
                        4 - Size - check how many students are in stack.
                        5 - Print all stack.
                        6 - Back to previous menu.\n""")

    menu_data_structure = menu([menu_stack, menu_graph], """
                Choose the program you are interested in:
                1 - A generic stack that keeps students information ordered by their grades.
                2 - Weighted graph which displays best route between cities.
                3 - Back to previous menu.\n""")

    menu_main = menu([menu_data_structure, menu_sql, menu_ml], """
        Hello ! Please choose an option:
        1 - Data structure & Algorithms.
        2 - SQL & Data Analysis.
        3 - Machine Learning.
        4 - Exit\n""")

    menu_main()


if __name__ == "__main__":
    main()

