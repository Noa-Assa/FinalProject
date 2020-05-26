from data_structures.sortable import Sortable


class Student(Sortable):
    def __init__(self, id=None, first_name=None, last_name=None, age=None, gender=None, average=None):
        self.id = self.set_id(id if id is not None else input("Enter ID: "))
        self.first_name = first_name if first_name is not None else input("Enter first name: ")
        self.last_name = last_name if last_name is not None else input("Enter last name: ")
        self.age = self.set_age(age if age is not None else int(input("Enter age: ")))
        self.gender = self.set_gender(gender if gender is not None else int(input("Enter gender: 0 - female, 1 - male: ")))
        self.average = self.set_average(average if average is not None else int(input("Enter average: ")))

    def __str__(self):
        return """
            ID: {}
            First name: {}
            Last name: {}
            Age: {}
            Gender: {}
            Average: {}
                """.format(self.id, self.first_name, self.last_name, self.age, self.get_gender(), self.average)

    def get_sort_value(self):
        return self.average

    def get_gender(self):
        if self.gender == 0:
            return "Female"
        return "Male"

    # Decision to work with Exception to make sure student is not added incorrectly.
    @staticmethod
    def set_id(id):
        if len(str(id)) != 9:
            raise Exception('Invalid Input: ID MUST contain 9 digits')
        return id

    @staticmethod
    def set_age(age):
        if age < 0:
            raise Exception('Invalid Input: age MUST be a positive number')
        return age

    @staticmethod
    def set_gender(gender):
        if (gender != 0) and (gender != 1):
            raise Exception('Invalid Input: gender = 0 - for female, 1 - for male')
        return gender

    @staticmethod
    def set_average(average):
        if (average < 0) or (average > 100):
            raise Exception('Invalid Input: average MUST be between 0-100')
        return average


