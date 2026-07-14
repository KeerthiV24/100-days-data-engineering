# Problem: Search in Rotated Sorted Array
#
# You are given a sorted array that has been rotated at an unknown position
# and a target value.
#
# Find the index of the target element in the array.
# If the target is not found, return -1.
#
# Example:
# Input:  arr = [4, 5, 6, 7, 0, 1, 2], target = 0
# Output: 4





def search_rotated_array(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[left] <= arr[mid]:

            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:

            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


arr = [4, 5, 6, 7, 0, 1, 2]
target = 0

print("Target Index:", search_rotated_array(arr, target))
