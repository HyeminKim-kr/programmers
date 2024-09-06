def solution(num_list):
    sum = 0
    product = 1
    for num in num_list:
        product *= num
        sum += num
    return 1 if product < sum**2 else 0