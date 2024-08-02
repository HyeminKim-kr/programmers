def solution(price):
    if price >= 500000:
        discounted_price = price * 0.8
    elif price >= 300000:
        discounted_price = price * 0.9
    elif price >= 100000:
        discounted_price = price * 0.95
    else:
        discounted_price = price
    
    answer = int(discounted_price)
    return answer