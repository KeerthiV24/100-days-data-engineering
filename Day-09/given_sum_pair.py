""" 📝 Problem Statement

Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

Example
Input:
nums = [2,7,11,15]
target = 9

Output:
[0,1]

""""

def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []


# Example
nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))
