""" Problem: Repeat and Missing Number Array
Problem Statement

You are given an array arr of size n containing numbers from 1 to n.

One number appears twice (repeating number).
One number is missing from the array.

Your task is to find:

The repeating number.
The missing number.

Return them as [repeating, missing].  """

def findRepeatAndMissing(arr):
    n = len(arr)

    visited = [False] * (n + 1)

    repeating = -1
    missing = -1

    for num in arr:
        if visited[num]:
            repeating = num
        else:
            visited[num] = True

    for i in range(1, n + 1):
        if not visited[i]:
            missing = i
            break

    return [repeating, missing]


# Example
arr = [3, 1, 2, 5, 3]
print(findRepeatAndMissing(arr))
