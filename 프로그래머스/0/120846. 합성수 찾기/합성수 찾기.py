def solution(n):
    def count_divisors(x):
        count = 0
        for i in range(1, x + 1):
            if x % i == 0:
                count += 1
        return count

    answer = 0
    for num in range(1, n + 1):
        if count_divisors(num) >= 3:
            answer += 1

    return answer
