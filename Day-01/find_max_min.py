"""
Given an array of integers, find the maximum and minimum elements present in the array.

"""

def find_max_min(arr):
    # Assume the first element is both maximum and minimum
    maximum = arr[0]
    minimum = arr[0]

    # Traverse the array
    for num in arr:
        if num > maximum:
            maximum = num

        if num < minimum:
            minimum = num

    return maximum, minimum


# Example
arr = [12, 45, 7, 89, 23]

max_element, min_element = find_max_min(arr)

print("Maximum Element:", max_element)
print("Minimum Element:", min_element)
