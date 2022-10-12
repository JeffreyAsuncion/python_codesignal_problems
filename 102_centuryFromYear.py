import math

def solution(year):
    century = math.ceil(year/100)
    return century


print(solution(2022))