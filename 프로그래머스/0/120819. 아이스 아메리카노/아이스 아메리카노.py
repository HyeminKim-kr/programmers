def solution(money):
    price_per_cup = 5500
    max_cups = money // price_per_cup
    remaining_money = money % price_per_cup
    answer = [max_cups, remaining_money]
    return answer