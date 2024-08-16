def solution(array):
    max_value = max(array)       # 배열에서 가장 큰 값을 찾음
    max_index = array.index(max_value)  # 그 값의 인덱스를 찾음
    return [max_value, max_index]
