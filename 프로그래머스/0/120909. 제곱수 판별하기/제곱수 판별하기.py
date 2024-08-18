# def solution(n):
#     i = 1
#     while i * i <= n:
#         if i * i == n:
#             return 1
#         i += 1
#     else:
#         return 2
    
def solution(n):
    return 1 if (n**0.5) % 1 == 0 else 2