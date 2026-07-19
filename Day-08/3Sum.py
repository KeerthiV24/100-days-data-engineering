"""
Problem: Find Pair with Sum in Sorted & Rotated Array

Problem Statement:
Given a sorted and rotated array and a target value, find whether there
is a pair of numbers whose sum is equal to the target.

Return True if a pair exists, otherwise return False.

Example:
Input:
arr = [11, 15, 6, 8, 9, 10]
target = 16

Output:
True
"""


def three_sum(nums):
    nums.sort()
    result = []

    n = len(nums)

    for i in range(n - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return result


# Example
nums = [-1, 0, 1, 2, -1, -4]

print(three_sum(nums))
