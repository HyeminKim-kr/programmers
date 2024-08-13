def solution(num_list):
    onezeros = [0 if i%2 == 0 else 1 for i in num_list]
    ones = onezeros.count(1)
    zeros = onezeros.count(0)
    answer = [zeros, ones]
    return answer