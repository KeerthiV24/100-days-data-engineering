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


def pair_in_sorted_rotated(arr, target):
    n = len(arr)

    # Find pivot (largest element)
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            break

    left = (i + 1) % n   # Smallest element
    right = i            # Largest element

    while left != right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True

        elif current_sum < target:
            left = (left + 1) % n

        else:
            right = (n + right - 1) % n

    return False


# Example
arr = [11, 15, 6, 8, 9, 10]
target = 16

print(pair_in_sorted_rotated(arr, target))
