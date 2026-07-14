""" ## 📝 Problem Statement

You are given an array of chocolate packets, where each packet contains some chocolates.

Distribute chocolates to **m students** by giving **one packet to each student**.

Find the **minimum difference** between the packet with the most chocolates and the packet with the least chocolates among the selected packets.
"""



def chocolate_distribution(arr, m):

    if m == 0 or len(arr) == 0:
        return 0

    arr.sort()

    min_difference = float('inf')

    for i in range(len(arr) - m + 1):

        difference = arr[i + m - 1] - arr[i]

        if difference < min_difference:
            min_difference = difference

    return min_difference


arr = [7, 3, 2, 4, 9, 12, 56]
m = 3

print("Minimum Difference:", chocolate_distribution(arr, m))
