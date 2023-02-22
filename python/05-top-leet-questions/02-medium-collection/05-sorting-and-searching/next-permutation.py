from collections import Counter
from typing import List, Set


# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
# More formally, if all the permutations of the array are sorted in one container according to their lexicographical
# order, then the next permutation of that array is the permutation that follows it in the sorted container. If such
# arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending
# order).


class Solution:
    # Time Complexity: O(n) [1 pass]
    # Space Complexity: O(1)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find first decrease
        i = len(nums) - 1
        while i >= 1 and nums[i - 1] >= nums[i]:  # consider equality
            i -= 1

        if i < 1:
            self.reverse(nums, 0, len(nums) - 1)  # reverse whole list
            return

        val = nums[i - 1]
        j = len(nums) - 1
        while j > i - 1 and nums[j] <= val:
            j -= 1

        # i-1 => first decrease; j = smallest element on rightside that is larger than nums[i-1]
        # swap i-1 and j
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # reverse from i to end
        self.reverse(nums, i, len(nums) - 1)

    def reverse(self, nums: List[int], start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    sol.nextPermutation(nums)
    print(nums)

    nums = [3, 1, 2, 4, 5, 6]
    sol.nextPermutation(nums)
    print(nums)

    nums = [5, 1, 1]
    sol.nextPermutation(nums)
    print(nums)
