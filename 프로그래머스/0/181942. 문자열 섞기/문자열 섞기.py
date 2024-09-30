def solution(str1, str2):
    answer = ''
    for num in range(len(str1)):
        answer += str1[num]
        answer += str2[num]
    return answer