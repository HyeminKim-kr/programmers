def solution(rsp):
    wins = {
        2: 0,
        0: 5,
        5: 2
    }
    return ''.join(str(wins[int(char)]) for char in rsp)