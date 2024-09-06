def solution(a, b):
    concat_value = int(str(a) + str(b))
    multiply_value = 2 * a * b
    return concat_value if concat_value >= multiply_value else multiply_value