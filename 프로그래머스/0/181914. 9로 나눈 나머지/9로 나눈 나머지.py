def solution(number):
    # return int(number) % 9
    return sum(int(digit) for digit in number) % 9