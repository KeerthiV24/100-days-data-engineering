"""
Problem: 3Sum

Problem Statement:
Given an array of integers, find all unique triplets whose sum is equal
to 0.

Return the list of unique triplets.

Example:
Input:
nums = [-1, 0, 1, 2, -1, -4]

Output:
[[-1, -1, 2], [-1, 0, 1]]
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
