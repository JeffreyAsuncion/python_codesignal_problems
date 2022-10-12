def solution(inputString):
    return inputString == inputString[::-1]

print(solution("kayak"))
print(solution("tacocat"))
print(solution("dog"))