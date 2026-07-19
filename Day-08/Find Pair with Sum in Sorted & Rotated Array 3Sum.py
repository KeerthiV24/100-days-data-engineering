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
