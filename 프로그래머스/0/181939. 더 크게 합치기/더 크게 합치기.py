def solution(a, b):
    aplusb = int(str(a) + str(b))
    bplusa = int(str(b) + str(a))
    return aplusb if aplusb >= bplusa else bplusa