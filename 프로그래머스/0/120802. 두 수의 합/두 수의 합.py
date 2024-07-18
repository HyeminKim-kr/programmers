def solution(num1, num2):
    if -50000 <= num1 <= 50000 and -50000 <= num2 <= 50000:
        answer = num1 + num2
    else:
        raise ValueError("Input numbers has to be within the range -50,000 to 50,000")
    return answer