import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def solution(n):
    return lcm(6, n) // 6
