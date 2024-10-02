def solution(age):
    alphabet = 'abcdefghij'
    return ''.join(alphabet[int(digit)] for digit in str(age))
