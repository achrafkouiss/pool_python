from functools import reduce
from operator import add, mul

def spell_reducer(spells: list[int], operation: str) -> int:
    def combine():
        if operation == "add":
            result = reduce(add, spells)
        elif operation == "multiply":
            result = reduce(mul, spells)
        elif operation == "max":
            result = reduce(max, spells)
        elif operation == "min":
            result = reduce(min, spells)
        return result
    return combine


a = spell_reducer([1, 2, 3, 4, 5], "min")
print(a())
# list_of_strings = ["Python", " is", " powerful", " with", " lambdas"]

# # The lambda function concatenates two strings at a time (x + y)
# joined_string = reduce(lambda x, y: x + y, list_of_strings)

# print(joined_string)



# def sum(a, y):
#     return a + y

# a = sum(2, 3)
# print(a)

