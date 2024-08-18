def solution(my_string):
    each = list(my_string)
    integers = [int(item) for item in each if item.isdigit()]
    return sum(integers)