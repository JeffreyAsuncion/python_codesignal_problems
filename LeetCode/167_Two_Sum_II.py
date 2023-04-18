"""
167. Two Sum II - Input Array Is Sorted
Medium
8.1K
1.1K
company
Amazon
company
Adobe
company
Apple
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
"""

def twoSum(numbers, target):
    # for i in range(len(numbers)):
    #     for j in range(len(numbers)):
    #         if i != j:
    #             if numbers[i]+numbers[j] == target:
    #                 return[i+1,j+1]
            # initial left and right
    left = 0
    right = len(numbers)-1

    # converge on solution with left < right
    while left < right:
        
        # check base case 
        sum_lr = numbers[left] + numbers[right]
        if sum_lr == target:
            return [left+1,right+1]

        # fine tune the sum 
        if sum_lr > target:
            # sum too large reduce right
            right -= 1
        else:
            # sum too small increase left
            left += 1
                    

numbers = [2,3,4]
target = 6
# Output: [1,3]
print(twoSum(numbers,target))

numbers = [2,7,11,15]
target = 9
# Output: [1,2]
print(twoSum(numbers,target))