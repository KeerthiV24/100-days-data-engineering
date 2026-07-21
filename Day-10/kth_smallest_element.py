""" Problem Statement

Find the Kth smallest element in an unsorted array.  """



def kth_smallest(arr, k):
    arr.sort()
    return arr[k - 1]

# Example
arr = [7, 10, 4, 3, 20, 15]
k = 3

print("Kth Smallest Element:", kth_smallest(arr, k))
