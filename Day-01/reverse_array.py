""" 
Given an array of integers, reverse the order of its elements.
"""

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap elements
        arr[left], arr[right] = arr[right], arr[left]

        # Move pointers
        left += 1
        right -= 1

    return arr


# Example
arr = [10, 20, 30, 40, 50]

print("Original Array:", arr)

reversed_array = reverse_array(arr)

print("Reversed Array:", reversed_array)
