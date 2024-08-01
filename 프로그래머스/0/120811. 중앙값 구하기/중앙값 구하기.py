def solution(array):
    array.sort()
    length = len(array)
    middle_index = length // 2
    return array[middle_index]