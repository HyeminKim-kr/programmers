def solution(numbers):
    largest_two = sorted(numbers, reverse=True)
    answer = largest_two[0] * largest_two[1]
    return answer