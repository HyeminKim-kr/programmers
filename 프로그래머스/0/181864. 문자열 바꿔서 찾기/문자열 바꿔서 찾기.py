def solution(myString, pat):
    trans_string = myString.replace('A', 'x').replace('B', 'A').replace('x', 'B')
    return 1 if pat in trans_string else 0