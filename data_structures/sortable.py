from abc import ABC, abstractmethod


class Sortable(ABC):

    @abstractmethod
    def get_sort_value(self):
        pass

