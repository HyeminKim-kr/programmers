def solution(money):
    max_cups = money // 5500
    rest_money = money % 5500
    return [max_cups, rest_money]