def solution(myString):
    til_l = 'abcdefghijk'
    for s in myString:
        if s in til_l:
            myString = myString.replace(s, 'l')
    return myString
            