# Problem: Rearrange the given array into the next lexicographically greater permutation. If no such permutation exists, rearrange it to the lowest possible order.


class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # Step 1: Find the first decreasing element
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: Find the next greater element
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the remaining elements
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums


# Example
nums = [1, 2, 3]
solution = Solution()
print(solution.nextPermutation(nums))
