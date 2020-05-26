

def is_choice_valid(chosen_number, max):
    if chosen_number.isnumeric():
        chosen_number = int(chosen_number)
        if (chosen_number <= max) and (chosen_number >= 1):
            return chosen_number
    return None


def show(method):
    def inner():
        print()
        print(method())
    return inner


def show_object(object):
    def inner():
        print()
        print(object)
    return inner





