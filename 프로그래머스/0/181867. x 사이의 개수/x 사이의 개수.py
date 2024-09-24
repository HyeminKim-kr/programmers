def solution(myString):
    answer = myString.split('x')
    return [len(part) for part in answer]