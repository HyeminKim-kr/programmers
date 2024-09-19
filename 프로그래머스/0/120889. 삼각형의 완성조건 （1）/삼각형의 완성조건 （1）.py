def solution(sides):
    three = sorted(sides)
    return 1 if three[2] < three[0] + three[1] else 2