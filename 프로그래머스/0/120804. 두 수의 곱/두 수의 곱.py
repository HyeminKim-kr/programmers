def solution(num1, num2):
    if 0 <= num1 <= 100 and 0 <= num2 <= 100:
        answer = num1 * num2
    else:
        answer = 'Numbers must be between 0 and 100.'
    return answer
