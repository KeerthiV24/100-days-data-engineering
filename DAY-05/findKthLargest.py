""" Kth Largest Element in an Array
Problem Statement

Given an integer array nums and an integer k, return the kth largest element in the array.

Note: It is the kth largest element in sorted order, not the kth distinct element. """

def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]


# Example
nums = [3, 2, 1, 5, 6, 4]
k = 2

print(findKthLargest(nums, k))
