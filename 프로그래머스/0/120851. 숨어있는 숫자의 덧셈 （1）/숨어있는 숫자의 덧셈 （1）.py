def solution(my_string):
    integers = [int(item) for item in my_string if item.isdigit()]
    return sum(integers)