def solution(n):
    area = 1
    for i in range(1,n):
        area += 4*i
    return area

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))