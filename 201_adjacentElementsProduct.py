"""
Given an array of integers, 
find the pair of adjacent elements 
that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.
"""
def solution(inputArray):
    max_product = 0.0000000000000001
    for i in range(len(inputArray)-1):
        product = inputArray[i] * inputArray[i+1]
        if product > max_product:
            max_product = product
    return max_product



inputArray = [3, 6, -2, -5, 7, 3]
print(solution(inputArray))